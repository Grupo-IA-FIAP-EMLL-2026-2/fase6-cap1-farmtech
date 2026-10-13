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

A **base v2 corrigida** contém 40 fotos de cada classe: 32 para treino, 4 para validação e 4 para teste por classe, totalizando 64/8/8. Quatro fotos repetidas foram substituídas pelas novas fotos enviadas pelo grupo. As novas caixas foram importadas, conferidas e exportadas no Make Sense IA. A [preparação e a revisão da base](docs/BASE_DE_DADOS.md) registram as alterações e as limitações.

Os três notebooks foram **executados novamente** com esta versão. A base congelada e os modelos estão na [publicação base-v2](https://github.com/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/releases/tag/base-v2), com arquivos e hashes para reprodução. Os resultados da versão anterior estão identificados no [histórico](docs/historico/README.md).

## 📁 Estrutura de pastas

```text
fase6-cap1-farmtech/
├── assets/logo-fiap.png
├── data/
│   ├── dataset.yaml
│   ├── manifesto.csv
│   ├── correcao_base_v2.json
│   └── revisao_makesense_base_v2.json
├── docs/
│   ├── BASE_DE_DADOS.md
│   ├── RESULTADOS_FRENTE1.md
│   ├── REVISAO_ENTREGA.md
│   ├── ROTEIRO_VIDEO.md
│   ├── historico/
│   ├── figuras/
│   └── resultados/
├── notebooks/
│   └── LucasCarvalhoCordeiro_rm570388_pbl_fase6.ipynb
├── EltonModestoDeSouzaDias_rm572530_pbl_fase6.ipynb
├── MatheusFontes_rm570457_pbl_fase6.ipynb
├── scripts/auditar_base.py
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

A publicação base-v2 contém as 80 fotos corrigidas, 80 marcações, pesos dos dois experimentos e o modelo da CNN. Os notebooks, gráficos, previsões e tabelas atuais estão neste repositório. O Colab monta o Drive pessoal e prepara uma pasta própria para a versão v2.

## 📎 Links e Observações

### 🔗 Links do Projeto

| Material | Acesso | Situação |
| --- | --- | --- |
| Entrega 1 — YOLO customizada | [Notebook executado](https://github.com/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/blob/main/notebooks/LucasCarvalhoCordeiro_rm570388_pbl_fase6.ipynb) · [Abrir no Colab](https://colab.research.google.com/github/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/blob/main/notebooks/LucasCarvalhoCordeiro_rm570388_pbl_fase6.ipynb) | Reexecutada na base v2; 30 e 60 épocas, seleção pela validação e teste reservado |
| Entrega 2 — CNN do zero | [Notebook executado](MatheusFontes_rm570457_pbl_fase6.ipynb) · [Abrir no Colab](https://colab.research.google.com/github/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/blob/main/MatheusFontes_rm570457_pbl_fase6.ipynb) | Reexecutada do zero na base v2, com resultados e imagens classificadas |
| Entrega 2 — YOLO padrão e comparação | [Notebook executado](EltonModestoDeSouzaDias_rm572530_pbl_fase6.ipynb) · [Abrir no Colab](https://colab.research.google.com/github/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/blob/main/EltonModestoDeSouzaDias_rm572530_pbl_fase6.ipynb) | Reexecutada na base v2; caixas e comparação dos três modelos |
| Base v2, marcações e modelos | [Arquivos publicados](https://github.com/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/releases/tag/base-v2) | Versão corrigida usada nos três novos experimentos |
| Drive do grupo | [Pasta compartilhada](https://drive.google.com/drive/folders/1T-mHMYGu8Nj33VuK808TOb8hT5D6Q5OT) | Pasta original; a versão corrigida está na publicação base-v2 |
| Resumo da YOLO para comparação | [Resultados da Frente 1](https://github.com/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech/blob/main/docs/RESULTADOS_FRENTE1.md) | Métricas, durações, protocolo e caminhos registrados |
| Revisão dos requisitos | [Revisão da entrega](docs/REVISAO_ENTREGA.md) | Evidências e itens que faltam para concluir o trabalho |
| Vídeo demonstrativo | Link ainda não publicado · [Roteiro de gravação](docs/ROTEIRO_VIDEO.md) | Gravar com os resultados da base v2; YouTube não listado, até cinco minutos |

### 🧠 Decisões Técnicas

- **Base comum:** preservar as mesmas imagens de treino, validação e teste nas três abordagens. Uma foto pode conter vários objetos da mesma classe.
- **YOLO customizada:** ajustar a YOLOv5s a partir de pesos pré-treinados, comparar 30 e 60 épocas na validação e avaliar o modelo escolhido no teste reservado.
- **CNN:** treinar uma rede em Keras do zero, classificando a foto inteira. YOLO também localiza os objetos por meio das caixas.
- **Avaliação:** apresentar métricas de detecção e acerto por foto separadamente. Na comparação de tempos, informar hardware, tamanho da entrada, lote e etapas medidas; as três novas execuções utilizaram a CPU Intel Core 7 150U. O tempo da YOLO inclui etapas diferentes do tempo da CNN, conforme a tabela de condições.

### 📊 Resultados atuais — base v2

A comparação abaixo mede **classe correta por foto**, usando as mesmas oito fotos de teste. Ausência de caixa na YOLO é erro; havendo caixas, escolhe-se a classe da maior confiança a partir de 0,25.

| Abordagem | Acertos no teste | Acerto por foto |
| --- | ---: | ---: |
| YOLO customizada — 60 épocas | 7/8 | 87,50% |
| YOLO padrão COCO | 5/8 | 62,50% |
| CNN do zero | 8/8 | 100,00% |

A YOLO customizada obteve **mAP@50 de 78,53%** e **mAP@50–95 de 51,95%** no teste. mAP avalia detecções e caixas; não equivale à acurácia da CNN. O teste é pequeno e contém cenas próximas, portanto os resultados não comprovam desempenho geral em novas condições. [Tabelas e comparação por foto](docs/resultados/base_v2/yolo_padrao/comparacao_por_foto.csv).

### 📢 Observações Gerais

A substituição das fotos, o manifesto, os dois treinamentos da YOLO, a CNN e a comparação foram concluídos e registrados nesta versão. A gravação e publicação do vídeo ficam a cargo do grupo. O [roteiro](docs/ROTEIRO_VIDEO.md) utiliza os resultados atuais.

**Prazo informado pelo grupo: 13/10/2026.** Antes da submissão, conferir o link do vídeo e os acessos. Após a entrega no portal, manter a versão entregue congelada, conforme o enunciado. A [revisão](docs/REVISAO_ENTREGA.md) distingue o que foi verificado e os itens de submissão.

## 🔧 Como executar o código

1. Abra o notebook desejado pelo link **Abrir no Colab** da tabela acima.
2. Para treinar a YOLO, selecione GPU no Colab. As execuções salvas desta versão foram feitas em CPU; uma nova execução terá outros tempos.
3. Execute as células em ordem e autorize a montagem do seu Google Drive quando solicitado.
4. O notebook baixa a base v2 da publicação, confere o SHA-256 e os 80 arquivos, e organiza a pasta `/content/drive/MyDrive/FIAP_fase6_grupo21_base_v2/dataset_yolo/organizado`.
5. Os resultados são salvos em `/content/drive/MyDrive/FIAP_fase6_grupo21_base_v2/resultados_farmtech_v2`. Salve também o notebook executado.

A pasta pessoal v2 permite reproduzir a versão correta mesmo que a pasta compartilhada contenha a versão antiga. Para apenas consultar os resultados, use os notebooks já executados; não é necessário treinar novamente para gravar o vídeo.

```bash
git clone https://github.com/Grupo-IA-FIAP-EMLL-2026-2/fase6-cap1-farmtech.git
```

Na execução local, os notebooks aceitam `FARMTECH_DATASET_ROOT` apontando para a base v2 extraída e `FARMTECH_OUTPUT_ROOT` para o destino dos resultados. Utilizar Jupyter com TensorFlow/Keras, PyTorch/torchvision, NumPy, pandas, Matplotlib, scikit-learn, PyYAML, Pillow e os requisitos oficiais da YOLOv5. Python **3.12.3**, PyTorch **2.14.1+cpu**, TensorFlow **2.21.0** e Keras **3.15.1** foram registrados nesta execução. As [versões completas](docs/resultados/base_v2/pip_freeze_execucao.txt) e os ambientes dos modelos foram preservados. O código YOLO está fixado no commit `f9578796b8a64889aa9e66dc06914d19f40d338e`.

Para conferir uma cópia extraída:

```bash
python scripts/auditar_base.py /caminho/para/organizado
```

## 📋 Licença

Este README foi adaptado do [template da Fase 6](https://github.com/fiap-tutoria/FIAP-PORTFOLIO-AI/blob/master/1TIAO/FASE6/CAP-X-NOME-DA-ATIVIDADE-APRESENTADA-NO-PORTAL/README.md), disponibilizado pela [FIAP](https://www.fiap.com.br/) sob [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Atribuição referente ao modelo de documentação e ao material institucional utilizado nesta adaptação para o Grupo 21.
