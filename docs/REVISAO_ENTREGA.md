# Revisão da entrega — Fase 6, Grupo 21

**Revisão documental e estrutural em 12/10/2026.** Referências: enunciado fornecido pelo grupo, [template da Fase 6 da FIAP](https://github.com/fiap-tutoria/FIAP-PORTFOLIO-AI/blob/master/1TIAO/FASE6/CAP-X-NOME-DA-ATIVIDADE-APRESENTADA-NO-PORTAL/README.md), notebooks executados e arquivos publicados.

**Parecer:** o projeto está no caminho certo. Há base preparada, YOLO customizada executada e CNN do zero executada. A entrega obrigatória ainda está incompleta porque faltam a YOLO padrão, a comparação das três abordagens e o vídeo, além da integração dos arquivos no repositório final.

## Entrega 1 — YOLO customizada

| Exigência | Evidência e situação |
| --- | --- |
| Duas classes distintas, 40 imagens de cada | Banana e garrafa PET; base com 80 fotos e marcações |
| Divisão 32/4/4 por classe | Confirmada nas contagens e no manifesto da base |
| Drive e marcação no Make Sense IA | Descrição da preparação registrada pelo grupo e estrutura de imagens/labels no Drive |
| Colab com treinamento, validação e teste | [Notebook de Lucas](https://github.com/lucas-crvlh/fase6-cap1-farmtech/blob/main/notebooks/LucasCarvalhoCordeiro_rm570388_pbl_fase6.ipynb), com 13 células de código executadas e nenhuma saída de erro registrada |
| Dois experimentos com épocas distintas | Treinamentos independentes de 30 e 60 épocas, confirmados nos CSVs dos experimentos |
| Escolha e avaliação final | Escolha de `best.pt` do experimento de 60 épocas pela validação; teste reservado executado |
| Imagens processadas e conclusões | Referências, previsões, matriz, curvas e interpretações preservadas no notebook |
| Acesso na entrega do grupo | Link direto no README; arquivo ainda publicado no repositório de Lucas, a incorporar à integração do grupo |

Na validação, o mAP@50–95 foi de 41,23% no experimento de 30 épocas e de 66,17% no de 60 épocas. O modelo escolhido obteve mAP@50–95 de 55,63% no teste e acertou a classe de 7/8 fotos (87,50%), conforme a regra de classificação por foto documentada.

## Entrega 2 — comparação das abordagens

| Parte | Situação |
| --- | --- |
| YOLO customizada | Resultados disponíveis para comparar |
| YOLO padrão, conforme capítulo 3 | Contribuição ainda não disponível na `main` consultada |
| CNN do zero | [Notebook de Matheus](../MatheusFontes_rm570457_pbl_fase6.ipynb) integrado, com 10 células executadas, 30 épocas, nenhum erro registrado e 8/8 fotos corretas no teste |
| Comparação crítica das três | Aguarda a YOLO padrão e a consolidação das avaliações |

A arquitetura da CNN é criada em Keras sem carregar uma rede pré-treinada. O código preserva as pastas de treino, validação e teste da base YOLO e lê os labels para organizar a cópia por classe. Curvas, matriz de confusão e as oito fotos classificadas estão presentes.

Para concluir a comparação:

1. Aplicar a YOLO padrão indicada pelo material do capítulo 3 e registrar seus resultados nas mesmas fotos.
2. Comparar facilidade de uso e integração, qualidade, treinamento/customização quando aplicável e inferência.
3. Usar uma medida comum de acerto por foto para comparar com a CNN; manter mAP e demais métricas de detecção em uma leitura separada.
4. Registrar hardware, resolução, lote e escopo dos tempos. A CNN registrou 15,6 s de treinamento e 9,4 ms/foto em CPU local, com imagens 128×128 e medição de `predict` sobre o teste em lote de 8. A YOLO registrou cálculo da rede de 17,30 ms/foto em Tesla T4, lote 1, tamanho configurado 640, separando preparação e NMS. Esses números não permitem concluir qual arquitetura é mais rápida sob as mesmas condições.
5. Explicar os acertos, erros e limites de cada abordagem. A CNN acertou oito fotos, mas isso não demonstra desempenho universal. Uma mudança de um acerto nesta amostra corresponde a 12,5 pontos percentuais.

A síntese da CNN deve deixar claro que ela assume uma classe alvo por foto, podendo haver vários objetos dessa classe. Na galeria, o valor exibido entre parênteses é a saída sigmoid para garrafa PET; valores próximos de zero nas fotos de banana não significam baixa confiança na previsão de banana.

## Repositório, identificação, README e vídeo

| Item | Situação e ação necessária |
| --- | --- |
| Repositório público | O repositório da organização está público |
| Nome do grupo | Grupo 21 identificado no README; para cumprir literalmente o pedido de nome do grupo no repositório, incluir `grupo21` na nomenclatura final e atualizar os links correspondentes |
| Integrantes e RMs | Os quatro nomes e RMs foram confirmados pelo grupo e registrados no README |
| Nome dos notebooks | Lucas e Matheus usam nome, RM e `pbl_fase6.ipynb`; verificar a identificação dos próximos arquivos |
| Template FIAP | README adaptado às seções do modelo da Fase 6, com logo, integrantes, professores, descrição, estrutura real, links, decisões, execução e atribuição |
| Identificação do tutor | Nome ainda não informado; confirmar no portal e completar |
| Notebook final e links | Reunir as contribuições no repositório do grupo; confirmar acesso a cada notebook e aos dados |
| Vídeo | Ainda não publicado; gravar após a comparação completa, até cinco minutos, YouTube não listado, com link direto no README |
| Prazo | Informado pelo grupo como 13/10/2026; registrar a submissão e congelar a versão entregue |

O template permite adaptar as pastas ao projeto. O README descreve os arquivos existentes, sem apresentar diretórios vazios como implementações. A documentação detalhada da base foi preservada em [BASE_DE_DADOS.md](BASE_DE_DADOS.md).

## Ordem recomendada para finalizar

1. Incorporar a contribuição de Lucas ao repositório do grupo, preservando código, saídas e resultados.
2. Receber a YOLO padrão e a comparação executadas de Elton.
3. Consolidar os notebooks e as conclusões, com identificação completa da equipe e acesso reproduzível aos dados.
4. Conferir a versão integrada por execução completa no ambiente escolhido.
5. Gravar e publicar o vídeo, revisar os links e as identificações e submeter no prazo.

O barema reserva 3,0 pontos ao notebook, 2,0 ao README, 2,0 ao vídeo, 1,5 ao repositório e 1,5 à organização. Adaptar o README melhora a apresentação, mas não substitui os itens técnicos e o vídeo que ainda faltam. Os módulos “Ir Além” são opcionais e não compõem a nota das entregas obrigatórias.

## Limites desta revisão

A revisão conferiu os arquivos e as saídas salvas, a sintaxe e a estrutura dos notebooks, as configurações e os registros dos experimentos. O merge da CNN preservou o arquivo revisado. Os treinamentos não foram reexecutados nesta revisão; a versão consolidada ainda depende das contribuições restantes e de uma execução de conferência.
