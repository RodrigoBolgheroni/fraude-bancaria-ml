import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from generate_data import transformar_em_csv

def load_and_preprocess_data(caminho_csv):
    df = pd.read_csv(caminho_csv)

    #Define Y
    y = df['Fraude']

    #Converte as variaveis categoricas pra 1 ou 0
    df = pd.get_dummies(df,columns=['Hora do Dia','Tipo de Transferência','Dispositivo','Localização'])

    #Aplica normalização na coluna Valor
    scaler = MinMaxScaler()
    X_raw = df.drop("Fraude", axis=1)
    X_scaled = scaler.fit_transform(X_raw)

    #Define X
    X = pd.DataFrame(X_scaled, columns=X_raw.columns)

    return X, y, scaler

def train_model(X_train, y_train):
    #Treina o modelo
    model = LogisticRegression(random_state=42,class_weight='balanced')
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    #Tenta prever um valor
    y_pred = model.predict(X_test)

    #Exiibire as métricas
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))

def main():
    transformar_em_csv("data/transacoes.csv",10000)

    X, y, scaler = load_and_preprocess_data("data/transacoes.csv")

    #Divide os dados de treino e teste em 80/20
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)

    joblib.dump(model, "modelo.pkl")
    joblib.dump(scaler, "scaler.pkl")
    joblib.dump(X.columns.tolist(), "colunas.pkl")


if __name__ == "__main__":
    main()
