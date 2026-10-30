import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df=pd.read_excel("Files/car_data2.xlsx")
X=df[["Volume","Weight"]]
y=df["CO2"]
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)

linear=LinearRegression()
f=linear.fit(X_train,y_train)
y_pred=f.predict(X_test)

print("r2: ",r2_score(y_test,y_pred))
df=pd.DataFrame({"y_test":y_test,"y_pred":y_pred})
print(df)



