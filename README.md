FarmTech — FIAP | Fase 6, Capítulo 1

Projeto acadêmico de visão computacional para detecção de bananas e garrafas PET utilizando YOLO.

Objetivo

Desenvolver uma solução de visão computacional capaz de identificar bananas e garrafas PET em imagens, utilizando um modelo de detecção de objetos YOLO.

Dataset

Foi preparado um conjunto de 80 imagens, distribuídas igualmente entre duas classes:

ID| Classe| Quantidade de imagens
0| "banana"| 40
1| "garrafa_pet"| 40
Total| | 80

Coleta e anotação

As imagens foram reunidas e anotadas manualmente na plataforma MakeSense.ai, utilizando caixas delimitadoras (bounding boxes) para identificar os objetos.

As anotações foram exportadas no formato YOLO, com arquivos ".txt" correspondentes às imagens. Uma mesma imagem pode conter mais de um objeto anotado.

Foi realizada a conferência das imagens, das anotações e da correspondência entre as classes:

- "0": banana
- "1": garrafa_pet

Divisão dos dados

O conjunto foi dividido de maneira estratificada entre treinamento, validação e teste.

Conjunto| Banana| Garrafa PET| Total
Treinamento| 32| 32| 64
Validação| 4| 4| 8
Teste| 4| 4| 8
Total| 40| 40| 80

A divisão foi realizada por meio de um script Python no Google Colab, utilizando a semente aleatória "42" para garantir reprodutibilidade.

Estrutura do dataset

Os arquivos foram organizados da seguinte maneira:

organizado/
├── data.yaml
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/

Cada imagem possui um arquivo de anotação com o mesmo nome-base.

O arquivo "data.yaml" contém a configuração das duas classes e os caminhos dos conjuntos de treinamento, validação e teste.

Observação: o arquivo gerado no Google Colab possui um caminho absoluto para o Google Drive de origem, que deverá ser ajustado conforme o ambiente utilizado no treinamento.

Preparação e validação

Foram realizadas as seguintes atividades:

1. Coleta e seleção de 80 imagens.
2. Anotação manual dos objetos no MakeSense.ai.
3. Exportação das anotações no formato YOLO.
4. Verificação da correspondência entre imagens e arquivos ".txt".
5. Conferência dos IDs das duas classes.
6. Separação dos dados em treinamento, validação e teste.
7. Organização das pastas e geração do arquivo "data.yaml".

O dataset está armazenado no Google Drive do projeto, em:

"FIAP_fase6_grupo21/dataset_yolo/organizado"

Próximas etapas

O conjunto de dados está preparado para o treinamento do modelo YOLO. As etapas de treinamento, avaliação das métricas e apresentação dos resultados serão documentadas conforme o desenvolvimento do projeto.

Contribuições

Larissa da Silva Marcelino: coleta e preparação das imagens, anotação manual no MakeSense.ai, validação das classes, organização do dataset YOLO e documentação dessa etapa.


Entrega 2: CNN treinada do zero

Uma CNN simples foi treinada do zero para classificar a imagem inteira como "banana" ou "garrafa_pet", usando a mesma divisão treino/validação/teste do dataset YOLO (32/4/4 por classe).

Notebook: [MatheusFontes_rm570457_pbl_fase6.ipynb](MatheusFontes_rm570457_pbl_fase6.ipynb) (código, saídas, métricas e análise crítica). Roda no Colab ou localmente; a seção 1.1 converte o dataset YOLO em pastas por classe, sem alterar o Drive.

Vídeo demonstrativo: (link do YouTube "não listado" a ser adicionado)

Contribuições (Entrega 2, CNN)

Matheus Fontes: implementação, treinamento e avaliação da CNN, e documentação dessa etapa.
