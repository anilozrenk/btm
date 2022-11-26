import magpylib as magpy
import numpy as np
import matplotlib.pyplot as plt
import coil as co
import plotly.graph_objects as go

dl=np.linspace(0,10,100)
vertices=np.c_[np.cos(2*np.pi*dl),np.sin(2*np.pi*dl),dl+10]
coil1 = magpy.current.Line(
    current=1,
    vertices=vertices
)


# x_res=y_res=z_res=5
# x_max=y_max=z_max=10
# ax_res=[x_res,y_res,z_res]
    
# x = np.linspace(-x_max, x_max, x_res)
# y = np.linspace(-y_max, y_max, y_res)
# z = np.linspace(-z_max, z_max, z_res)

# Y,X,Z=np.meshgrid(x,y,z)

# dl=np.linspace(0,10,10)
# vertices=np.c_[np.cos(2*np.pi*dl),np.sin(2*np.pi*dl),dl+10]
# current=np.c_[np.cos(2*np.pi*dl),np.sin(2*np.pi*dl),dl+10]

# coil=co.Coil(X,Y,Z,vertices,vertices)
# vector=coil.get_b()
# print(vector)
# print("="*10)
# vector2=vector/np.linalg.norm(vector)
# print(vector2)
