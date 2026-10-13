"""Confere manifesto, marcações e cópias perceptuais. Uso: python scripts/auditar_base.py BASE."""
import csv,hashlib,itertools,json,sys
from pathlib import Path
import numpy as np
from PIL import Image,ImageOps
from scipy.fft import dctn
base=Path(sys.argv[1]);rows=list(csv.DictReader((base/'manifesto.csv').open(newline='')))
assert len(rows)==80
assert hashlib.sha256((base/'manifesto.csv').read_bytes()).hexdigest()=='a1e2b05d9dccde76b97a04ceee1f983ca7ad987ab0b795e6171eb281227225ba', 'Manifesto diferente da base v2 congelada.'
for split in ['train','val','test']:
 assert {p.name for p in (base/'images'/split).iterdir() if p.suffix.lower() in {'.jpg','.jpeg','.png'}}=={r['arquivo'] for r in rows if r['conjunto']==split}
 assert {p.name for p in (base/'labels'/split).glob('*.txt')}=={r['marcacao'] for r in rows if r['conjunto']==split}
hashes=[]
for r in rows:
 p=base/'images'/r['conjunto']/r['arquivo'];assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256_imagem'],p.name
 linhas=(base/'labels'/r['conjunto']/r['marcacao']).read_text().strip().splitlines()
 assert len(linhas)==int(r['quantidade_caixas'])
 for s in linhas:
  cid,x,y,w,h=map(float,s.split());assert cid==int(cid)==int(r['classe_id']) and 0<=x<=1 and 0<=y<=1 and 0<w<=1 and 0<h<=1
  assert min(x-w/2,y-h/2)>=-1e-6 and max(x+w/2,y+h/2)<=1+1e-6
 im=ImageOps.exif_transpose(Image.open(p)).convert('L');v=np.asarray(im.resize((32,32),Image.Resampling.LANCZOS),dtype=float);c=dctn(v,norm='ortho')[:8,:8].flatten();ph=c>np.median(c[1:]);a=np.asarray(im.resize((9,8),Image.Resampling.LANCZOS));dh=(a[:,1:]>a[:,:-1]).flatten()
 hashes.append((r['arquivo'],r['conjunto'],ph,dh))
for split,n in [('train',32),('val',4),('test',4)]:
 for cid in [0,1]:assert sum(r['conjunto']==split and int(r['classe_id'])==cid for r in rows)==n
assert len({r['sha256_imagem'] for r in rows})==80
pares=[]
for a,b in itertools.combinations(hashes,2):
 dp=int(np.count_nonzero(a[2]!=b[2]));dd=int(np.count_nonzero(a[3]!=b[3]))
 if dp<=4 and dd<=4:pares.append({'a':a[0],'b':b[0],'conjunto_a':a[1],'conjunto_b':b[1],'phash':dp,'dhash':dd})
assert not [p for p in pares if p['phash']==0 and p['dhash']==0],pares
print(json.dumps({'imagens':80,'sha256_distintos':80,'pares_semelhantes_para_revisao_visual':pares},ensure_ascii=False,indent=2))
