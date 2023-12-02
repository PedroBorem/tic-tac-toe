# tic-tac-toe
Inatel-AG002-Trabalho Prático

## 1. Estrutura
<pre>
> project
|   |> data
|   |   //Data files go here.
|   |> orig
|   |   //Original files go here.
|   |> output
|   |   //Output files go here. (Classifier)
|01-Import.ipynb    //Notebook for importing data;
|02-EDA.ipynb   //Notebook for exploratory data analysis
|03-Baseline.ipynb  //Notebook for baseline model
|interface.ipynb    //Notebook for the interface
README.md   //Project documentation
</pre>

## 2. Project Brief
#### 2.1 `01-Import`
- Foram importados os dados originais e feito a organização dos nomes das colunas e dos valores.

#### 2.2 `02-EDA`
- Foi feita uma análise em busca de Missing_Values e Dados Inconsistentes. 
- E fizemos alguns comentários sobre os dados que tínhamos.
- Levantamos uma segunda abordagem na geração dos dados, para termos além de posições finais, posições iniciais do jogo.
- Foi feita uma comparação na distribuição dos dados propostos com os dados obtidos na nossa geração de Posições no Tabuleiro.
- Unimos os dois Dataframes e ficamos com um dataset mais completo.

#### 2.3 `03-Baseline`
- Separamos as Features do Target.
- Dividimos os dados em Train/Test.
- Avaliamos o treinamento e teste para KNN, DT, Perceptron.
###### 2.3.1 Para o Dataset proposto:
- Obtivemos uma ótima precisão, sem necessidade para Hyperparameter Tunning.

###### 2.3.2 Para o nosso Dataset:
- A precisão obtida foi menor.
- Fizemos Hyperparameter Tunning com GridSearch.
- Melhoramos os resultados.

## 3. Interface
A interface foi feita usando a biblioteca `customtkinter`.

*No notebook é possível escolher qual classificador será utilizado para avaliação das posições.*
- Trocar no código.
```python
# model = joblib.load(f"{ROOT}/output/tic-tac-toe-model-data.joblib") # Treinado com o Dataset Original
model = joblib.load(f"{ROOT}/output/tic-tac-toe-model-data2.joblib")  # Treinado no Dataset Modificado, melhor predict para posições iniciais
```

#### 3.1 Usage
Rodando o notebook, irá abrir a janela da interface com um `Grid 3x3` e dois botões, `Confirmar` e `Reset`.

No Grid 3x3, ao clicar nos campos do jogo da velha você irá preencher com `X` e `O` alternadamente.

Quando quiser avaliar se a posição é vencedora ou não para X, clique no botão `Confirmar` e use o botão `Reset` para limpar o `Grid 3x3`.

