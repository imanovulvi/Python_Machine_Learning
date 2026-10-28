import numpy as np
import matplotlib.pyplot as plt

data=[10,20,30,40,50,60,70,80,90,100]

print("20%: ",np.percentile(data,20))
print("50%: ",np.percentile(data,50))
print("90%: ",np.percentile(data,90))

d=np.random.uniform(0.0,5.0,250)#bu metow baslangic ve son deyer verilerek eyni araliqda deyerler cretae edir verdiyiiz saya uygun

# plt.hist(d,5)
# plt.show()

d2=np.random.normal(7,1,100000)# normal metodu 7 ortalama deyerde 1 standar deviation kenarlasma olan 100000 deyer uret

plt.hist(d2,1000)
plt.show()