# Multiple Linear Regression


import pandas as pd
from sklearn import linear_model

df=pd.read_excel("Files/car_data2.xlsx")
X=df[["Volume","Weight"]]
y=df["CO2"]

lm=linear_model.LinearRegression()
f=lm.fit(X,y)
df2=pd.DataFrame([[1700,1600]],columns=["Volume","Weight"])
print("Dot Scale ",f.predict(df2))
"""
Multi linear regresia dusuturu asagdakidir .Bu dustur vasitesi ile biz verdiyimiz deyerlere uygun ehtimal edir.
CO_2 = a * Volume + b * Weight + c
c= f.coef_
a ve b = f.intercept_

"""
####Scale 2 novu var. MinMaxScaler ve Standart Scale
"""
Scale nedir musteqil data arasinda miqyas ferqi varsa yeni Value 1 ve Weight 2000 dirse 
burada masin oyrenende sehv ede biler ona gore de biz buna standar halina getirirk ki iki deyer arasin cox ferq olmasin

1.MinMaxScaler nədir?
MinMaxScaler məlumatları standart halda 0 ilə 1 arasına gətirir.
X=X-Xmin/Xmax-Xmin
yeni verilen arrayden 
x = [1000, 1500, 2000, 2500] min ve max deyerleri dusturda yerine qoyub standar hala getiririk
"""
from sklearn.preprocessing import MinMaxScaler
df=pd.read_excel("Files/car_data.xlsx")
X=df[["Volume","Weight"]]
y=df["CO2"]
mn=MinMaxScaler()
scalX=mn.fit_transform(X)
l=linear_model.LinearRegression()
f=l.fit(scalX,y)
df=pd.DataFrame([[2,700]],columns=["Volume","Weight"])
trans=mn.transform(df)
pr=f.predict(trans)
print("Max Min Scale",pr)
"""
2.Standart scale
StandardScaler nədir?
StandardScaler məlumatları elə çevirir ki, nəticələrin orta qiyməti təxminən 0, standart kənarlaşması isə 1 olsun.
Dustur
z=X-  mean (ortalama) / standard deviation
"""

from sklearn.preprocessing import StandardScaler
df=pd.read_excel("Files/car_data.xlsx")
X=df[["Volume","Weight"]]
y=df["CO2"]
sd=StandardScaler()
scaleX=sd.fit_transform(X)
l=linear_model.LinearRegression()
f=l.fit(scaleX,y)
df=pd.DataFrame([[2,700]],columns=["Volume","Weight"])
trans=sd.transform(df)
pr=f.predict(trans)
print("Standart Scale",pr)