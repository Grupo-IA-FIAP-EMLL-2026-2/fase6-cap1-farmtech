# Revisão da entrega — Fase 6, Grupo 21

**Versão v2 revisada em 13/10/2026**, após substituir quatro fotografias repetidas. Referência: enunciado fornecido pelo grupo e template FIAP indicado no README.

Os três notebooks foram executados novamente, com saídas reais e sem células de erro. A parte técnica está disponível para a gravação; publicar o vídeo e submeter no portal ainda são ações do grupo.

## Entrega 1

- [YOLO customizada](../notebooks/LucasCarvalhoCordeiro_rm570388_pbl_fase6.ipynb): base com 40 fotos por classe, divisão 32/4/4 por classe, manifesto congelado e marcações revisadas.
- Dois treinamentos independentes, exatamente 30 e 60 épocas. O experimento de 60 épocas foi escolhido pela validação antes de avaliar o teste.
- Teste: 7/8 classes corretas por foto; mAP@50 78,53%; mAP@50–95 51,95%.
- Curvas, métricas, caixas, previsões individuais, tempos e condições estão no notebook e em [resultados](RESULTADOS_FRENTE1.md).

## Entrega 2

- [YOLO padrão e comparação](../EltonModestoDeSouzaDias_rm572530_pbl_fase6.ipynb): inferência COCO reexecutada nas oito fotos da base v2, 5/8 classes corretas. Não foi treinada na base do grupo.
- [CNN](../MatheusFontes_rm570457_pbl_fase6.ipynb): arquitetura própria inicializada aleatoriamente, treinada novamente por 30 épocas; 8/8 classes corretas.
- A [comparação](resultados/base_v2/yolo_padrao/comparacao_acertos_teste.csv) usa o mesmo teste e previsões efetivas dos três modelos. [Resultado por foto](resultados/base_v2/yolo_padrao/comparacao_por_foto.csv) e [tempos/condições](resultados/base_v2/yolo_padrao/comparacao_tempos_condicoes.csv) estão registrados.
- A análise cobre integração, qualidade, treinamento, inferência, detecção versus classificação e limitações do teste. Todos os tempos atuais são da nova execução em CPU, com diferenças de resolução, lote e etapas explícitas.

## Identificação e submissão

| Item | Estado |
| --- | --- |
| Repositório público | Organização do grupo, notebooks e evidências da base v2 |
| Integrantes e RMs | Lucas 570388; Larissa 571790; Elton 572530; Matheus 570457 |
| Tutora | Nicolly Candida |
| Nomes de notebooks | Nomes completos, RM e sufixo pbl_fase6.ipynb |
| README | Template FIAP, apresentação, estrutura, links e execução atualizados |
| Dados/modelos | Publicação base-v2 com arquivos, hashes e manifesto |
| Drive compartilhado | Consultar situação real no README; Colab prepara a cópia pessoal v2 |
| Vídeo | Gravar com os resultados novos, publicar no YouTube não listado, até cinco minutos e inserir o link no README |
| Prazo | Informado pelo grupo: 13/10/2026; congelar a versão após submeter |

O barema atribui 3,0 ao notebook, 2,0 ao README, 2,0 ao vídeo, 1,5 ao repositório e 1,5 à organização. Os módulos Ir Além são opcionais e não compõem a nota obrigatória.

O enunciado pede nome do grupo no nome do repositório. O Grupo 21 está identificado no README e na organização, mas o repositório mantém `fase6-cap1-farmtech`; esse detalhe literal deve ser confirmado antes da submissão. A YOLO padrão é a versão da contribuição original; o material do capítulo 3 não foi fornecido para confirmar a variante da turma. A execução atual foi em CPU local; os notebooks incluem montagem do Drive e reprodução no Colab, e a primeira execução Colab/T4 foi preservada no histórico. Não se afirma que a nova execução ocorreu numa GPU.

Antes da entrega: conferir o vídeo e seus acessos, confirmar os dois detalhes do enunciado acima e submeter o link correto no portal. A publicação no GitHub não equivale à submissão. Oito fotos de teste e cenas próximas limitam a generalização; remover cópias não elimina todas as semelhanças entre fotografias.
