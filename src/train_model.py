from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from generate_data import transformar_em_csv
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
import joblib

transformar_em_csv("data/transacoes.csv",10000)

df = pd.read_csv("data/transacoes.csv")
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


#Divide os dados de treino e teste em 80/20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)

#Treina o modelo
model = LogisticRegression(random_state=42,class_weight='balanced')
model.fit(X_train, y_train)

#Tenta prever um valor
y_pred = model.predict(X_test)

#Exiibire as métricas
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))

joblib.dump(model, "modelo.pkl")
joblib.dump(scaler, "scaler.pkl")



