"""
1. Model əvvəl Rank sütunundakı qiymətlərə baxır
Bizim məlumatlar:

9, 4, 6, 4, 8, 5, 7, 9, 7, 9, 5, 7

Model bunları sıralayır:

4, 4, 5, 5, 6, 7, 7, 7, 8, 9, 9, 9
2. Fərqli qiymətləri tapır
Təkrarlananları çıxarır:

4, 5, 6, 7, 8, 9
3. Ardıcıl qiymətlərin ortasını tapır
Qiymətlər	Orta	Yaranan şərt
4 və 5	4.5	Rank <= 4.5
5 və 6	5.5	Rank <= 5.5
6 və 7	6.5	Rank <= 6.5
7 və 8	7.5	Rank <= 7.5
8 və 9	8.5	Rank <= 8.5

Niyə orta qiyməti götürür?

Çünki 4 ilə 5 arasındakı sərhədi tapmaq istəyir. 4.5 yazanda:
- 4 və ondan kiçiklər sola gedir.
- 5 və ondan böyüklər sağa gedir.
Beləliklə, heç bir mövcud Rank qiyməti iki qrupa bölünmür.
4. Model bu şərtlərin hamısını yoxlayır
Məsələn:
Rank <= 4.5
Rank <= 5.5
Rank <= 6.5
Rank <= 7.5
Rank <= 8.5

Hər şərt üçün Gini azalmasını hesablayır.
Gini deyer hemise 0 ile 0.5 arasinda olur.eger 0-sa gini safdir,
eger 0.5 ise gini qarisiqdir.
Qisa bele izah verim eger butun cavablar Yes ise gini sifir ve safdir.eger yari yari 
olarsa gini deyeri 0.5 olacaq ve gini qarisiqdir. 

Ən böyük azalma hansı şərtdədirsə, onu seçir.

Gini dusturu:

Gini=1-(P_YES/n)^2-(P_NO/n)^2

P_YES=>Yeslerin sayi
P_NO => Nolarin sayi
n => umumi say

"""

import pandas as pd
from sklearn.tree import ExtraTreeClassifier,plot_tree
import matplotlib.pyplot as plt

df=pd.read_excel("Files/actor.xlsx")
feature=["Age","Experience","Rank","Nationality"]
nat={"UK":0,"USA":1,"TR":2}
df["Nationality"]=df["Nationality"].map(nat)
go={"YES":1,"NO":0}
df["Go"]=df["Go"].map(go)
X=df[feature]
y=df["Go"]
tree=ExtraTreeClassifier()
tree.fit(X,y)
new_data=pd.DataFrame([[36,21,8,1]],columns=feature)
print(tree.predict(new_data))

#Agac yapisi
plt.figure(figsize=(15,9))
plot_tree(tree,feature_names=feature)
plt.show()