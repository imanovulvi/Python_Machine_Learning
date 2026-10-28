#5_PolynomialRegresion
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x=[1,2,3,4,5,6,7,8,9,10,11,12] #masinin kecme saati
y=[100,95,87,79,60,50,65,68,70,75,75,90]# masinin sureti

fit=np.polyfit(x,y,3)# burada 3 yeni 3 cu deyereceden hesablamaga basla y = ax^3 + bx^2 + cx + d

func=np.poly1d(fit)
print(func(7.3))#ozumuz x deyerin veririk ki masin ehtimal etsin
r2=r2_score(y,func(x))#burada polyominal ne qeder bir birine bagliligin yoxlayir
#r2 eger 0 olarsa hec bir mentiqi uygunluq yoxdur
# 1.0	Model real nəticələrə tam uyğun gəlir.
# 0.9	Model məlumatlardakı dəyişkənliyi yaxşı izah edir.
# 0.7	Model müəyyən qədər yaxşı izah edir.
# 0.0	Model orta qiyməti proqnozlaşdırmaqdan daha yaxşı deyil.
# -0.5	Model orta qiymətdən istifadə edən sadə proqnozdan daha pis nəticə göstərir.
print(r2)
plt.plot(x,y)
plt.scatter(x,y)
plt.show()
