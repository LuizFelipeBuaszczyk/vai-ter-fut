import pandas as pd
from sklearn import tree

# Dataset
dados_entrada = {
    'temperatura': [30, 25, 16, 23, 35, -3, 10, 28, 22, 18, 5, 32, 26, 12, -1, 29, 21, 37, 15, 24],
    'esta_chovendo': [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    'percentual_umidade': [45, 85, 50, 90, 40, 15, 60, 55, 95, 62, 70, 35, 80, 58, 85, 50, 65, 88, 45, 75],
    'pode_jogar': [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(dados_entrada)

X = df.iloc[:,:3]
Y = df.iloc[:,-1] 

## Treina
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

## Predição - temperatura, esta_chovendo, percentual_umidade
result = clf.predict([[10, 0, 50]])

print(result)
