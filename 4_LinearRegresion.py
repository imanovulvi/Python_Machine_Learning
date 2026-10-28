# y=ax+b
# a=> bizə X bir vahid artdıqda Y-nin orta hesabla nə qədər dəyişdiyini göstərir.
# x=>asili olmayan teref
# y=>asili olan teref
# b=>X sıfır olduqda modelin proqnozlaşdırdığı Y qiymətidir.
from scipy import stats
import matplotlib.pyplot as plt



x=[1,2,3,4,5,6,7,8,9]
y=[100,90,80,70,60,50,40,30,20]


a,b,r,p,std_err=stats.linregress(x,y)
###### r=> X ilə Y arasındakı xətti əlaqənin istiqamətini və gücünü göstərir.
#-1 ile 1 arasinda olur
# 1	Mükəmməl müsbət xətti əlaqə
# 0.9	Güclü müsbət xətti əlaqə
# 0.5	Müsbət, orta səviyyəli xətti əlaqə
# 0	Xətti əlaqə yoxdur
# -0.5	Mənfi, orta səviyyəli xətti əlaqə
# -0.9	Güclü mənfi xətti əlaqə
# -1	Mükəmməl mənfi xətti əlaqə

######p=> müşahidə etdiyimiz xətti əlaqənin təsadüfi dəyişkənliklə izah oluna bilməsi barədə statistik qiymətləndirmə aparmağa kömək edir.
#p deyeri 0.05 kicik olarsa x ve y arasinda mentiqi elaqe yaxsidir

#######std_err — Standard Error (Meyillilik əmsalının standart xətası)
# std_err, a meyillilik əmsalının statistik qeyri-müəyyənliyini ölçür.

# Başqa sözlə, hesablanmış meyillilik əmsalının nə qədər dəqiq qiymətləndirildiyini anlamağa kömək edir.
#yeni meyillik xetasi ne qeder boyuk olsa o qeder eyimlik pisdir

print("a:",a)
print("b:",b)
print("r:",r)
print("p:",p)
print("std_err:",std_err)

def myFunc(x):
    return (a*x)+b

print(myFunc(10))

result=list(map(myFunc,x))
plt.plot(x,result)
plt.scatter(x,y)
plt.show()


# novbeti program

import pandas as pd

ds=pd.read_csv("Files/Student_Performance.csv")
x=ds["Hours Studied"]
y=ds["Performance Index"]
a,b,r,p,std_err=stats.linregress(x,y)
print("a:",a)
print("b:",b)
print("r:",r)
print("p:",p)
print("std_err:",std_err)
def myFunc2(x):
    return a*x+b

result2=list(map(myFunc2,x))
plt.scatter(x,result2)
plt.plot(x,result2)
plt.show()