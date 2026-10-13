# Roteiro do vídeo — Grupo 21, base v2

**Matheus:** use os notebooks da versão atual do repositório. Não é preciso treinar novamente para gravar. Duração total sugerida: 4 minutos e 40 segundos. Publicar no YouTube como **não listado** e inserir o link correto na linha de vídeo do README.

| Tempo | O que mostrar e explicar |
| --- | --- |
| 0:00–0:25 | README: Grupo 21, integrantes e objetivo de reconhecer banana e garrafa PET. |
| 0:25–1:00 | Base: 40 fotos por classe, 32/4/4, caixas no Make Sense e quatro fotos repetidas substituídas. Mostrar a revisão das caixas. |
| 1:00–2:00 | Notebook de Lucas: dois treinos, 30 e 60 épocas; escolha de 60 pela validação. Mostrar tabela e uma imagem do teste. |
| 2:00–2:50 | Notebook da CNN: rede do zero, 30 épocas, gráfico e matriz de confusão. Ela classifica a foto inteira. |
| 2:50–4:10 | Notebook de Elton: YOLO padrão sem treino nas fotos do grupo; mostrar previsões e tabela dos três modelos. Explicar integração, qualidade e condições dos tempos. |
| 4:10–4:40 | Conclusão: teste pequeno, mAP diferente de acurácia, dados/modelos/notebooks disponíveis e possibilidade de ampliar cenários. |

## Números atuais para falar

- YOLO customizada: **7/8 (87,50%)** de classes corretas; mAP@50 **78,53%** e mAP@50–95 **51,95%**.
- YOLO padrão: **5/8 (62,50%)**.
- CNN: **8/8 (100,00%)**, treino **21,44 segundos**.

Dizer “neste conjunto de oito fotos”, evitando prometer o mesmo desempenho em qualquer fotografia. Os tempos novos foram medidos em CPU; os antigos tempos de Tesla T4 não pertencem a esta comparação. Cada modelo mede etapas diferentes, por isso não declarar o mais rápido apenas pela tabela.

Mostrar no mínimo uma previsão correta e, se houver, uma falha real. Uma classe correta por foto não garante que todas as caixas estão perfeitas. Deixar o README legível e esconder dados pessoais da tela que não façam parte da identificação acadêmica.

**Falha para mostrar:** `IMG-20261005-WA0044.jpg`. As duas YOLOs não detectaram a garrafa acima de 0,25; a CNN acertou a classe da foto. Mostre essa diferença e explique que classificar a foto não é localizar o objeto.
