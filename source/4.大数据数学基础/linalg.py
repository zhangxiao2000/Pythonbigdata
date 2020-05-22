'''
Created on 2019年8月18日

@author: lingyulong
'''

import numpy as np

#求A的逆矩阵
A=np.array([[1,-1],
            [1,1]])

Av=np.linalg.inv(A)
print(Av)
print()
#验证A*Av=E
print(np.dot(A,Av))
print("*"*50)

#求A的广义逆矩阵
np.set_printoptions(suppress=True)
A=np.array([[1,-1],
            [1,1],
            [1,1]])

Av=np.linalg.pinv(A)
print("A的广义逆矩阵:\n",Av)
print()
#验证（1）A*Av*A=A  （2）Av*A*Av=Av  （3）(A*Av).T=A*Av (Av*A).T=Av*A
print("验证：A*Av*A=A:\n",A@Av@A)      #验证：A*Av*A=A
print("验证：Av*A*Av=Av:\n",Av@A@Av)   #验证：Av*A*Av=Av
print("验证：A*Av是对称阵\n",A@Av)        #验证：A*Av是对称阵
print("验证：A*Av是对称阵:\n",Av@A)        #验证：Av*A是对称阵
print("*"*50)

'''
#|A|
np.set_printoptions(suppress=True)
data=np.array([[1,-1],
               [1,1]])
data_det=np.linalg.det(data)
print(data_det)
print("*"*50)


#A=U*S*V
data=np.array([[1,2,3],
               [2,1,2],
               [1,3,3]])
u,s,v=np.linalg.svd(data)
print(u)
print(s)
print(v)
print()
#验证A=U*S*V
temp=np.dot(u,np.diag(s))
print(np.dot(temp,v))
print("*"*50)


#Ax=b
A=np.array([[1,2,3],
            [2,1,2],
            [1,3,3]])
b=np.array([2,1,4])
x=np.linalg.solve(A,b)
print("解为：",x)
#验证Ax=b
print("Ax:",np.dot(A,x))
print("*"*50)



#Ax=ax
A=np.array([[1,2],
            [2,1]])
a,x=np.linalg.eig(A)
print(a)
print(x)
print()
#验证Ax=ax
print("AX")
for i in range(len(a)):
    #print(x[i,:])
    #print(a[i]*x[i,:])
    print(np.dot(A,x[:,i]))
    
print()
print("aX")
for i in range(len(a)):
    print(np.dot(a[i],x[:,i]))    
  
print("*"*50)
'''

import numpy as np

#A=U*S*V
data=np.array([[1,2,3],
               [2,1,2],
               [1,3,3]])
u,s,v=np.linalg.svd(data)
print("u")
print(u)
print("s")
print(s)
print("v")
print(v)
print()
#验证A=U*S*V
temp=np.dot(u,np.diag(s))
print(np.dot(temp,v))






