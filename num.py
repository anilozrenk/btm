import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as sd
# dl=np.linspace(0,10,5)
# delta=10/100
# vertices=np.c_[np.cos(2*np.pi*dl),np.sin(2*np.pi*dl),dl]
# distance=np.diff(vertices, axis=0)
# normed=np.linalg.norm(vertices,axis=0)
# print(normed)
# print("---"*50)
# print(distance)

points=[[1,0,0],
     [2,0,0],
     [3,0,0]]
points=np.array(points)
print(points)
print('---'*10)
dist=np.diff(points,axis=0)
print(dist)
sum=dist.sum(axis=0)
sum=np.asarray(sum)
print(sum)
#dist_norm=dist/np.linalg.norm(dist)
print()


# compute norm of vector
vec_norm =points/ np.linalg.norm(points)
 
print("Vector norm:")
print(vec_norm)

# fig=plt.figure()

# ax=fig.add_subplot(111,projection="3d")
# ax.plot(vertices[:,0],vertices[:,1],vertices[:,2])

# fig.show()