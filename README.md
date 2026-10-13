# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" width="40%">
  </a>
</p>

# FarmTech Solutions — Visão Computacional

## Grupo 21 — Fase 6: O Começo da Rede Neural

## 👨‍🎓 Integrantes

| Integrante | RM | Responsabilidade |
| --- | --- | --- |
| [Lucas Carvalho Cordeiro](https://github.com/lucas-crvlh) | 570388 | YOLO customizada e integração das contribuições |
| [Larissa da Silva Marcelino](https://github.com/larilife) | 571790 | Organização das imagens, marcações e documentação |
| [Elton Modesto de Souza Dias](https://github.com/El1onDias193) | 572530 | YOLO padrão e comparação das abordagens |
| [Matheus Fontes](https://github.com/mthsfontes) | 570457 | CNN treinada do zero e montagem do vídeo |

## 👩‍🏫 Professores

### Tutora

Nicolly Candida.

### Coordenador(a)

[André Godoi Chiovato](https://www.linkedin.com/in/andregodoichiovato/), conforme a identificação apresentada no template da FIAP.

## 📜 Descrição

O projeto demonstra a um cliente fictício da FarmTech Solutions como reconhecer **bananas e garrafas PET em fotografias**. O objetivo é comparar uma **YOLO customizada**, uma **YOLO padrão** e uma **CNN treinada do zero**, considerando qualidade das previsões, facilidade de integração, treinamento e inferência.

A base contém **40 fotos de cada classe**, com **32 para treino, 4 para validação e 4 para teste por classe**, totalizando 64/8/8 imagens. As caixas foram marcadas no Make Sense IA, e os arquivos estão no Drive do grupo. A preparação está documentada em [Base de dados](docs/BASE_DE_DADOS.md).

O passo a passo, o código executado, os resultados e as conclusões estão nos notebooks vinculados abaixo. Este README apresenta o trabalho e orienta o acesso às contribuições.

## 📁 Estrutura de pastas

```text
fase6-cap1-farmtech/
├── assets/logo-fiap.png
├── data/
│   ├── dataset.yaml
│   └── manifesto.csv
├── docs/
│   ├── BASE_DE_DADOS.md
│   ├── RESULTADOS_FRENTE1.md
│   ├── REVISAO_ENTREGA.md
│   ├── figuras/
│   └── resultados/
├── notebooks/
│   └── LucasCarvalhoCordeiro_rm570388_pbl_fase6.ipynb
├── EltonModestoDeSouzaDias_rm572530_pbl_fase6.ipynb
├── MatheusFontes_rm570457_pbl_fase6.ipynb
├── .gitignore
└── README.md
```

- **`assets/`**: imagem institucional utilizada neste README.
- **`data/`**: configuração e manifesto da base, sem fotos originais.
- **`docs/`**: documentação, resultados e imagens processadas.
- **`notebooks/`**: implementação executada da YOLO customizada.
- **`EltonModestoDeSouzaDias_rm572530_pbl_fase6.ipynb`**: YOLO padrão e comparação das três abordagens.
- **`MatheusFontes_rm570457_pbl_fase6.ipynb`**: implementação e avaliação executadas da CNN.
- **`README.md`**: apresentação, identificação da equipe e links de acesso.

Fotos originais, marcações e pesos da YOLO permanecem no Drive. Os três notebooks, as evidências selecionadas e a comparação estão reunidos neste repositório do grupo.

## 📎 Links e Observações

### 🔗 Links do Projeto

| Material | Acesso | Situação |
| --- | --- | --- |
| Entrega 1 — YOLO customizada | [Notebook executado](https://github.com/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/blob/main/notebooks/LucasCarvalhoCordeiro_rm570388_pbl_fase6.ipynb) · [Abrir no Colab](https://colab.research.google.com/github/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/blob/main/notebooks/LucasCarvalhoCordeiro_rm570388_pbl_fase6.ipynb) | Integrada; experimentos de 30 e 60 épocas, teste reservado e resultados preservados |
| Entrega 2 — CNN do zero | [Notebook executado](MatheusFontes_rm570457_pbl_fase6.ipynb) · [Abrir no Colab](https://colab.research.google.com/github/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/blob/main/MatheusFontes_rm570457_pbl_fase6.ipynb) | Integrada à `main`, com resultados e imagens classificadas |
| Entrega 2 — YOLO padrão e comparação | [Notebook executado](EltonModestoDeSouzaDias_rm572530_pbl_fase6.ipynb) · [Abrir no Colab](https://colab.research.google.com/github/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/blob/main/EltonModestoDeSouzaDias_rm572530_pbl_fase6.ipynb) | Integrada; inferência reproduzida, caixas e comparação crítica |
| Dados, marcações e resultados da YOLO | [Google Drive do grupo](https://drive.google.com/drive/folders/1T-mHMYGu8Nj33VuK808TOb8hT5D6Q5OT) | Base comum e arquivos dos experimentos disponíveis |
| Resumo da YOLO para comparação | [Resultados da Frente 1](https://github.com/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/blob/main/docs/RESULTADOS_FRENTE1.md) | Métricas, durações, protocolo e caminhos registrados |
| Revisão dos requisitos | [Revisão da entrega](docs/REVISAO_ENTREGA.md) | Evidências e itens que faltam para concluir o trabalho |
| Vídeo demonstrativo | Link ainda não publicado | Resultados das três abordagens disponíveis para gravação; YouTube não listado, até cinco minutos |

### 🧠 Decisões Técnicas

- **Base comum:** preservar as mesmas imagens de treino, validação e teste nas três abordagens. Uma foto pode conter vários objetos da mesma classe.
- **YOLO customizada:** ajustar a YOLOv5s a partir de pesos pré-treinados, comparar 30 e 60 épocas na validação e avaliar o modelo escolhido no teste reservado.
- **CNN:** treinar uma rede em Keras do zero, classificando a foto inteira. YOLO também localiza os objetos por meio das caixas.
- **Avaliação:** apresentar métricas de detecção e acerto por foto separadamente. Na comparação de tempos, informar hardware, tamanho da entrada, lote e etapas medidas; a execução registrada da CNN utilizou CPU local, e a YOLO customizada utilizou Tesla T4.

### 📢 Observações Gerais

As três abordagens e a comparação estão integradas. A YOLO padrão foi reexecutada de ponta a ponta; os códigos e as saídas da YOLO customizada e da CNN foram preservados, com revisão das explicações. Falta publicar o vídeo e concluir a revisão de submissão descrita em [Revisão da entrega](docs/REVISAO_ENTREGA.md).

**Prazo informado pelo grupo: 13/10/2026.** Antes da submissão, revisar execução, nomes dos arquivos, acessos e conteúdo dos links. Após a entrega no portal, manter a versão entregue congelada, conforme a orientação do enunciado.

## 🔧 Como executar o código

1. Abra o [Drive do grupo](https://drive.google.com/drive/folders/1T-mHMYGu8Nj33VuK808TOb8hT5D6Q5OT) e adicione um atalho da pasta `FIAP_fase6_grupo21` em **Meu Drive**, ou copie a base preservando sua estrutura.
2. Abra o notebook desejado pelo link **Abrir no Colab** da tabela acima.
3. Para a YOLO customizada, selecione uma GPU no ambiente do Colab. A CNN pode executar em CPU; registrar o dispositivo é necessário para interpretar os tempos de uma nova execução.
4. Execute as células na ordem, autorize a montagem do Drive e ajuste o caminho da base se a sua cópia estiver em outro local. O caminho utilizado é `/content/drive/MyDrive/FIAP_fase6_grupo21/dataset_yolo/organizado`.
5. Confira as saídas e salve o notebook com os resultados. A YOLO customizada grava pesos e resultados no Drive; a YOLO padrão grava previsões e imagens em uma pasta de resultados; a CNN apresenta treinamento, gráficos e avaliação no próprio notebook.

Para baixar os arquivos deste repositório:

```bash
git clone https://github.com/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech.git
```

Na execução local da CNN, utilizar Jupyter e as bibliotecas TensorFlow, NumPy, Matplotlib, scikit-learn e PyYAML, com a base baixada e `YOLO_DIR` ajustado. A execução registrada da CNN utiliza Python 3.13.5; a versão completa das dependências não foi congelada. Os notebooks YOLO registram o commit do código utilizado. A reprodução da YOLO padrão também registra [ambiente e versões](docs/resultados/yolo_padrao/ambiente_execucao.json).

## 📋 Licença

Este README foi adaptado do [template da Fase 6](https://github.com/fiap-tutoria/FIAP-PORTFOLIO-AI/blob/master/1TIAO/FASE6/CAP-X-NOME-DA-ATIVIDADE-APRESENTADA-NO-PORTAL/README.md), disponibilizado pela [FIAP](https://www.fiap.com.br/) sob [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Atribuição referente ao modelo de documentação e ao material institucional utilizado nesta adaptação para o Grupo 21.
