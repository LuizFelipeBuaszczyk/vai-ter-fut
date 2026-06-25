import pandas as pd
from sklearn import tree

# Carrega o dataset
df = pd.read_csv('weatherHistory.csv')

# Pega a coluna original e cria a coluna temperatura
df['temperatura'] = df['Temperature (C)']

df['percentual_umidade'] = df['Humidity'] * 100

df['esta_chovendo'] = df['Precip Type'].apply(lambda x: 1 if x == 'rain' else 0)


# A regra de se pode jogar ou não
def regra_do_jogo(linha):
    condicao_temperatura = 15 <= linha['temperatura'] <= 32
    condicao_umidade = linha['percentual_umidade'] < 90
    sem_chuva = linha['esta_chovendo'] == 0
    
    if condicao_temperatura and condicao_umidade and sem_chuva:
        return 1 # Vai ter fut!
    else:
        return 0 # Sem fut :(

# aplica a regra pra todas linhas do arquivo
df['pode_jogar'] = df.apply(regra_do_jogo, axis=1)


# Separa os dados x,y
X = df[['temperatura', 'esta_chovendo', 'percentual_umidade']]
Y = df['pode_jogar']

# Treina a arvore de decisao, limitado a 5 para nao ficar muito complexa
clf = tree.DecisionTreeClassifier(criterion='gini', max_depth=5)
clf = clf.fit(X, Y)