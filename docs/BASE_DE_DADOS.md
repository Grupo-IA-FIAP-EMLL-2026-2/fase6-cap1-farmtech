# Base de dados — Grupo 21, versão v2

**Preparação original:** Larissa da Silva Marcelino — RM 571790. **Correção e integração:** Lucas Carvalho Cordeiro — RM 570388.

A base atual possui 80 fotos próprias do grupo. As classes são `0: banana` e `1: garrafa_pet`. Cada imagem tem um `.txt` YOLO de mesmo nome; uma foto pode ter várias caixas da mesma classe.

## Divisão preservada

| Conjunto | Banana | Garrafa PET | Total |
| --- | ---: | ---: | ---: |
| Treino | 32 | 32 | 64 |
| Validação | 4 | 4 | 8 |
| Teste | 4 | 4 | 8 |
| Total | 40 | 40 | 80 |

A divisão original, preparada com seed 42, foi mantida. Não houve sorteio de uma nova divisão depois de consultar os resultados. Todos os modelos usam exatamente os mesmos conjuntos da versão v2.

## Correção das fotografias

Quatro cópias redimensionadas identificadas na auditoria foram substituídas pelas novas fotos enviadas pelo grupo. Os nomes e conjuntos foram preservados:

| Arquivo | Conjunto | Foto nova enviada |
| --- | --- | --- |
| IMG-20261005-WA0108.jpg | Treino | WhatsApp Image (1).jpeg |
| IMG-20261005-WA0109.jpg | Treino | WhatsApp Image (2).jpeg |
| IMG-20261005-WA0111.jpg | Treino | WhatsApp Image .jpeg |
| IMG-20261005-WA0112.jpg | Teste | WhatsApp Image (3).jpeg |

O [registro da correção](../data/correcao_base_v2.json) contém os nomes completos da origem, hashes antigos e novos e coordenadas. Quatorze JPEGs de câmera tinham dados após o marcador final do JPEG; foram normalizados com orientação EXIF correta antes de criar o manifesto e treinar. Isso impede que a rotina da YOLO regrave as fotos silenciosamente. As caixas dessas imagens foram conferidas em uma [montagem](figuras/base_v2/marcacoes_camera_normalizadas.jpg).

## Marcação e revisão no Make Sense IA

As 76 marcações preservadas vieram da preparação original no Make Sense IA. As quatro novas caixas foram inicialmente definidas por coordenadas de pixels, importadas no Make Sense IA, conferidas visualmente e exportadas no formato YOLO. A operação ocorreu em um navegador local com a rede bloqueada após carregar a aplicação.

[Registro da revisão](../data/revisao_makesense_base_v2.json) e [capturas das quatro fotos](figuras/base_v2/makesense/revisao_1.png). O pacote de exportação está na publicação base-v2. O Make Sense exporta seis casas decimais; os arquivos congelados do treino mantêm oito casas, com diferença inferior a 0,001 pixel. A revisão não alterou a base enquanto os modelos treinavam.

## Manifesto e auditoria

O [manifesto atual](../data/manifesto.csv) registra arquivo, conjunto, classe, caixas e SHA-256. O [script de auditoria](../scripts/auditar_base.py) verifica os 80 pares, contagens, hashes, IDs, coordenadas e semelhança perceptual. A [auditoria após os treinos](resultados/base_v2/auditoria_base.json) confirma que os JPEGs não foram alterados durante a execução.

Não há imagens repetidas em bytes ou pares com pHash e dHash idênticos. Uma dupla de capturas visualmente próximas, `IMG-20261005-WA0051.jpg` e `IMG-20261005-WA0054.jpg`, permanece exclusivamente no treino. São fotos diferentes da mesma cena; essa proximidade é uma limitação documentada. Os limiares de hashes perceptuais são uma triagem, não uma prova de independência de todas as cenas.

## Arquivos e reprodução

A [publicação base-v2](https://github.com/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/releases/tag/base-v2) contém `dataset_farmtech_grupo21_v2.zip`, com 80 imagens, 80 arquivos de marcação, `data.yaml`, manifesto e registro da correção. Os hashes para download são publicados junto dos arquivos. A CNN converte essa estrutura em uma cópia local por classe com orientação EXIF, sem mudar os originais.

No Colab, os notebooks montam o Drive pessoal, baixam e conferem a versão correta e a armazenam nesta estrutura:

```text
FIAP_fase6_grupo21_base_v2/
├── dataset_yolo/organizado/
│   ├── data.yaml
│   ├── manifesto.csv
│   ├── images/{train,val,test}/
│   └── labels/{train,val,test}/
└── resultados_farmtech_v2/
```

[Drive original do grupo](https://drive.google.com/drive/folders/1T-mHMYGu8Nj33VuK808TOb8hT5D6Q5OT): a pasta compartilhada não deve ser confundida com a publicação v2. A situação real de sua atualização está indicada no README. Os resultados antigos ficam no [histórico da base v1](historico/README.md).
