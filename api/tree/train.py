import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree

# Dataset
df = pd.read_csv('./tree/data.csv')

X = df.iloc[:,:3]
Y = df.iloc[:,-1] 

## Treina
clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='gini', max_depth=3)
clf = clf.fit(X,Y)

## PDF da árvore
fig, ax = plt.subplots(figsize=(15, 10))

tree.plot_tree(
    clf,
    feature_names=X.columns.tolist(),
    class_names=['Nao_Jogar', 'Jogar'],
    filled=True,          
    fontsize=10,          
    ax=ax
)

# 4. Salvar diretamente em PDF
plt.savefig('arvore_decisao.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.close()
