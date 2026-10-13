# Resultados da Frente 1 — YOLO customizada, base v2

**Autor:** Lucas Carvalho Cordeiro — RM 570388. **Grupo 21. Tutora:** Nicolly Candida.

[Notebook executado](../notebooks/LucasCarvalhoCordeiro_rm570388_pbl_fase6.ipynb). Os resultados abaixo foram gerados novamente após corrigir a base; não são os valores antigos da Tesla T4.

## Protocolo da nova execução

YOLOv5s a partir dos pesos COCO; código oficial fixado no commit `f9578796b8a64889aa9e66dc06914d19f40d338e`. Dois treinamentos independentes de 30 e 60 épocas: imagem 640, lote 8, seed 42, cache RAM, workers 2 e parada antecipada desativada. O lote foi reduzido de 16 para 8 porque a nova execução usa CPU e o lote anterior excedeu a memória disponível. Os dois novos experimentos têm as mesmas condições.

A base v2 contém 40 fotos por classe, com 32/4/4. Quatro cópias foram substituídas; 14 JPEGs foram normalizados antes do manifesto para impedir a regravação automática pela YOLO. A [correção está documentada](../data/correcao_base_v2.json).

**Hardware:** Intel(R) Core(TM) 7 150U. **Ambiente:** Python 3.12.3, PyTorch 2.14.1+cpu, CPU. Os CSVs registram exatamente 30 e 60 épocas, iniciando em zero; `best.pt` pode ser de uma época anterior à última.

## Validação dos dois experimentos

| Épocas | Precisão (%) | Recall (%) | mAP@50 (%) | mAP@50–95 (%) | Duração (min) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 30 | 81,67 | 65,38 | 77,05 | 46,30 | 23,15 |
| 60 | 96,90 | 70,49 | 83,16 | 59,19 | 42,79 |

O modelo escolhido foi o **`best.pt` do experimento de 60 épocas**, pelo maior mAP@50–95 de validação. O teste foi avaliado apenas depois dessa escolha. Duração inclui o processo de treinamento, validações e gravação; exclui baixar pesos e preparar a base.

Fonte: [comparação de validação](resultados/base_v2/yolo_customizada/comparacao_validacao_yolo.csv).

## Teste reservado

| Precisão (%) | Recall (%) | mAP@50 (%) | mAP@50–95 (%) |
| ---: | ---: | ---: | ---: |
| 89,28 | 72,84 | 78,53 | 51,95 |

**Acerto da classe por foto: 7/8 = 87,50%.** A regra seleciona a caixa de maior confiança a partir de 0,25; ausência de detecção é erro. Esse indicador é usado na comparação com a CNN; mAP avalia caixas e não é acurácia de classificação.

Fontes: [teste](resultados/base_v2/yolo_customizada/resultado_teste_yolo.csv) e [previsões por foto](resultados/base_v2/yolo_customizada/exp_60_epocas_base_v2/predicoes_por_foto_base_v2/acertos_por_foto.csv).

## Tempo de inferência

| Etapa do detect.py | Média por foto |
| --- | ---: |
| Preparação do tensor | 0,70 ms |
| Cálculo da rede | 169,70 ms |
| NMS | 1,10 ms |

Lote 1, FP32, tamanho configurado 640, confiança 0,25 e IoU NMS 0,60. Entradas retangulares preservam proporção. Leitura completa, carregamento dos pesos e gravação das imagens não integram essa soma. A [comparação das três abordagens](../EltonModestoDeSouzaDias_rm572530_pbl_fase6.ipynb) informa os diferentes escopos dos tempos.

## Acesso aos dados e modelos

A [publicação base-v2](https://github.com/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/releases/tag/base-v2) reúne a base corrigida, os pesos de 30/60 épocas, o modelo escolhido e a CNN. O notebook baixa a base verificando o SHA-256; no Colab, monta o Drive pessoal e salva a versão v2 numa pasta própria, sem precisar escrever na pasta compartilhada antiga.

## Limitações

São apenas oito fotos de teste, com cenas e objetos de sessões próximas. A correção remove as cópias identificadas, mas não demonstra desempenho universal. Os resultados antigos ficam no [histórico da base v1](historico/README.md). Hardware e lote mudaram, portanto a diferença para as antigas execuções não pode ser atribuída somente às fotos substituídas.

## Exemplo de falha real

Na foto `IMG-20261005-WA0044.jpg`, a YOLO customizada e a padrão não encontraram uma caixa acima de confiança 0,25; a CNN classificou a foto como garrafa PET. A garrafa é transparente, está deitada e tem reflexos sobre uma superfície metálica de pouco contraste. Essas condições são hipóteses para investigar, não uma causa isolada pelo experimento. Uma melhoria seria coletar mais exemplos dessas condições e testar em novas cenas.

[Imagem processada da falha](resultados/base_v2/yolo_customizada/exp_60_epocas_base_v2/predicoes_por_foto_base_v2/IMG-20261005-WA0044.jpg).
