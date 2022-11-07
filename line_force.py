import numpy as np

dl=np.linspace(0,1,10)

vertices=np.c_[0*dl,dl,0*dl]

B=np.zeros([dl.size,3])
B=np.insert(B,0,1,axis=1)
B=np.delete(B,3,axis=1)
print(B)
print(vertices)
dl_B=np.cross(vertices,B)
print(dl_B)
#print(dl_B.sum(axis=0)*(dl[-1]-dl[0])/dl.shape())