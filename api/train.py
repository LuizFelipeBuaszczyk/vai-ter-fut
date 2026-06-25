import pandas as pd
from sklearn import tree

# Dataset
dados_entrada = {
    'temperatura': [30, 25, 16, 23, 35, -3, 10, 28, 22, 18, 5, 32, 26, 12, -1, 29, 21, 37, 15, 24,11, 34, 8, 20, 19, 27, 36, 14, 17, 31, 33, 9, 3, 38, 25, 22, 16, 28, 30, 13],
    'esta_chovendo': [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1,0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'percentual_umidade': [45, 85, 50, 90, 40, 15, 60, 55, 95, 62, 70, 35, 80, 58, 85, 50, 65, 88, 45, 75,55, 40, 65, 85, 50, 60, 45, 70, 55, 90, 40, 75, 80, 50, 45, 95, 60, 50, 40, 65],
    'pode_jogar': [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0,0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0]
}

df = pd.DataFrame(dados_entrada)

X = df.iloc[:,:3]
Y = df.iloc[:,-1] 

## Treina
clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='gini')
clf = clf.fit(X,Y)

## Predição - temperatura, esta_chovendo, percentual_umidade
result = clf.predict([[10, 0, 50]])

print(result)
