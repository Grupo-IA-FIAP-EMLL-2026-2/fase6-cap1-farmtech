# Revisão da entrega — Fase 6, Grupo 21

**Revisão e integração em 12/10/2026.** Referências: enunciado fornecido pelo grupo, [template da Fase 6 da FIAP](https://github.com/fiap-tutoria/FIAP-PORTFOLIO-AI/blob/master/1TIAO/FASE6/CAP-X-NOME-DA-ATIVIDADE-APRESENTADA-NO-PORTAL/README.md) e evidências executadas dos três notebooks.

**Parecer:** as três abordagens e a comparação estão integradas ao repositório do grupo. Falta publicar o vídeo demonstrativo e concluir a conferência da submissão.

## Entrega 1 — YOLO customizada

- [Notebook de Lucas](../notebooks/LucasCarvalhoCordeiro_rm570388_pbl_fase6.ipynb) integrado com 13 células de código executadas, sem saídas de erro; código, saídas e contadores originais preservados.
- Base com 40 fotos por classe e divisão 32/4/4 por classe: 64/8/8 no total.
- Dois experimentos independentes, de 30 e 60 épocas; escolha pela validação antes do teste.
- Teste: 7/8 classes de fotos corretas, mAP@50 de 83,74% e mAP@50–95 de 55,63%.
- Imagens processadas, curvas, interpretação de erros, configurações e resultados disponíveis no notebook e nos documentos de apoio.

## Entrega 2 — YOLO padrão, CNN e comparação

- [Notebook de Elton](../EltonModestoDeSouzaDias_rm572530_pbl_fase6.ipynb) corrigido e executado de ponta a ponta nesta integração. Usa YOLOv5s pré-treinada no COCO, sem treino na base do grupo. O enunciado remete ao capítulo 3; o grupo deve confirmar se a variante prevista no material da turma corresponde a esta implementação.
- A reprodução verificou os hashes das oito imagens contra o manifesto, confirmou 5/8 acertos e gerou oito imagens com as previsões e uma galeria. O resultado original de Elton também foi preservado com link, hash e métricas.
- [Notebook de Matheus](../MatheusFontes_rm570457_pbl_fase6.ipynb) integrado: CNN própria em Keras, treinada do zero, 30 épocas, 8/8 fotos corretas. Foram revisadas somente explicações; o código, as saídas e os contadores originais permanecem iguais.
- A comparação utiliza acerto por foto no mesmo teste: YOLO customizada 87,50%, padrão 62,50% e CNN 100%. As métricas de detecção ficam separadas e a amostra pequena é explicitada.
- A análise discute facilidade de integração, qualidade, treinamento quando aplicável e inferência. Informa as diferenças de hardware, entrada, lote e etapas medidas, sem declarar um vencedor de velocidade a partir de condições distintas.

## Evidências da integração

- [Comparação dos acertos](resultados/yolo_padrao/comparacao_acertos_teste.csv).
- [Comparação por foto](resultados/yolo_padrao/comparacao_por_foto.csv).
- [Tempos e condições](resultados/yolo_padrao/comparacao_tempos_condicoes.csv).
- [Caixas previstas pela YOLO padrão](resultados/yolo_padrao/caixas_yolo_padrao.csv).
- [Galeria de teste](figuras/yolo_padrao/galeria_teste.png).
- [Origem da contribuição de Elton](resultados/yolo_padrao/origem_contribuicao.json) e [referências da comparação](resultados/yolo_padrao/referencias_comparacao.json).

## Identificação, README e submissão

| Item | Situação |
| --- | --- |
| Repositório público | Organização do grupo, com os três notebooks e evidências selecionadas |
| Integrantes e RMs | Lucas Carvalho Cordeiro 570388; Larissa da Silva Marcelino 571790; Elton Modesto de Souza Dias 572530; Matheus Fontes 570457 |
| Tutora | Nicolly Candida |
| Nome dos notebooks | Nomes completos, RM e sufixo pbl_fase6.ipynb; arquivo de Elton corrigido na integração |
| README FIAP | Apresentação introdutória, logo, integrantes, professores, estrutura real, links e execução |
| Nome do grupo no repositório | Grupo 21 identificado no README. O enunciado pede nome do grupo no repositório; revisar a nomenclatura final para cumprir literalmente esse item |
| Vídeo | Pendente: até cinco minutos, YouTube não listado, link direto no README |
| Prazo | Informado pelo grupo: 13/10/2026; não alterar a versão após a submissão |

Antes de enviar, conferir os acessos com a conta que fará a avaliação, confirmar a abordagem de YOLO do capítulo 3, conferir as execuções no ambiente escolhido, gravar o vídeo e revisar seu link. O material do capítulo 3 não foi fornecido nesta revisão; não se afirma conformidade de uma versão específica por inferência.

O barema reserva 3,0 pontos ao notebook, 2,0 ao README, 2,0 ao vídeo, 1,5 ao repositório e 1,5 à organização. Os módulos “Ir Além” são opcionais e não compõem a nota das entregas obrigatórias.

## Limites da revisão

A YOLO padrão e a consolidação das tabelas foram realmente executadas nesta integração. Os treinamentos da YOLO customizada e da CNN não foram refeitos; a revisão preservou seus códigos e saídas e verificou a correspondência com as evidências. A base tem somente oito fotos de teste, sem avaliação independente adicional ou medição controlada de velocidade das três redes. A publicação no GitHub não equivale à submissão no portal da FIAP.
