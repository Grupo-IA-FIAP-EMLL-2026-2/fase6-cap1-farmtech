# Base de dados — Grupo 21

**Responsável pela preparação e documentação:** Larissa da Silva Marcelino — RM 571790.

Este documento reúne a descrição da base que estava no README do grupo antes da adaptação ao template da FIAP. Os experimentos devem preservar a divisão comum apresentada abaixo.

## Objetos e marcações

O conjunto contém 80 fotos, distribuídas entre banana e garrafa PET. As imagens foram reunidas pelo grupo e os objetos foram marcados manualmente no Make Sense IA com caixas delimitadoras.

As marcações foram exportadas no formato YOLO, com um arquivo `.txt` para cada imagem. Os IDs são `0: banana` e `1: garrafa_pet`. As coordenadas das caixas são normalizadas. Uma foto pode conter mais de um objeto anotado; na base utilizada, os objetos alvo de cada foto pertencem a uma mesma classe.

## Divisão dos dados

| Conjunto | Banana | Garrafa PET | Total |
| --- | ---: | ---: | ---: |
| Treino | 32 | 32 | 64 |
| Validação | 4 | 4 | 8 |
| Teste | 4 | 4 | 8 |
| **Total** | **40** | **40** | **80** |

A preparação registrada por Larissa informa uma separação estratificada por script no Colab, com seed 42. A execução da YOLO customizada e a conversão usada pela CNN confirmam as contagens 64/8/8.

## Armazenamento e estrutura

[Google Drive do grupo](https://drive.google.com/drive/folders/1T-mHMYGu8Nj33VuK808TOb8hT5D6Q5OT).

```text
FIAP_fase6_grupo21/
└── dataset_yolo/
    └── organizado/
        ├── data.yaml
        ├── images/
        │   ├── train/
        │   ├── val/
        │   └── test/
        └── labels/
            ├── train/
            ├── val/
            └── test/
```

Cada foto possui uma marcação com o mesmo nome-base. O `data.yaml` informa os nomes das classes e os caminhos dos conjuntos. Seu caminho absoluto deve ser ajustado se a base for copiada para outro ambiente.

## Preparação realizada

1. Coleta e seleção de 40 imagens de cada classe.
2. Marcação dos objetos no Make Sense IA.
3. Exportação dos arquivos no formato YOLO.
4. Conferência dos pares de imagens e marcações e dos IDs de classe.
5. Separação entre treino, validação e teste.
6. Organização das pastas e configuração do `data.yaml`.

O [manifesto da base usada na YOLO](../data/manifesto.csv) identifica arquivo, classe, conjunto, quantidade de caixas e hash da imagem. A conferência estrutural dessa base encontrou os 80 pares, as contagens exigidas e nenhuma imagem idêntica em bytes repetida. Isso não substitui uma revisão visual integral das caixas nem detecta fotografias apenas semelhantes.

A CNN converte essa estrutura em pastas por classe em uma cópia local, sem modificar o Drive. Todas as abordagens devem manter os conjuntos congelados para que a comparação use as mesmas imagens.
