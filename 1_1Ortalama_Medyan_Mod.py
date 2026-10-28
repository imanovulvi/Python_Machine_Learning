#Ortalama ,Medyan,Mode
import numpy as np
from scipy import stats
data=[2,3,4,12,6,76,2,33,22,54]
print(np.mean(data))#Ortalama: edeleri toplayib ededlerin sayina bolunur
print(np.median(data))#Medyan: Siraladiqdan sonra orta deyeri tapir Mes: [1,2,3]=2 ,[1,2,3,4]=burada 2+3 edir ve bolur 2 -ye
st=stats.mode(data)
print(st.count,st.mode) #Mode: bir arrayde en cox istifade olunan eded mode deyilir


