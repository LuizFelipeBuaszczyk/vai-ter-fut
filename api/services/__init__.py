import joblib

try:
    clf = joblib.load('./tree/tree.joblib')
except Exception:
    raise Exception("Modelo não encontrado, por favor execute train.py")
