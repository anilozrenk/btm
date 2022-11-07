
import numpy as np
import magpylib as magpy
import matplotlib.pyplot as plt
import pyvista as pv


# ts = np.linspace(-5, 5, 5)
# space = np.array([[[(x,y,z) for x in ts]for y in ts] for z in ts])

coil1 = magpy.Collection()
for z in np.linspace(0, 5, 10):
    winding = magpy.current.Loop(
        current=100,
        diameter=10,
        position=(0,0,z),
        
    )
    
    coil1.add(winding)
    
dl=np.linspace(0,10,100)
vertices=np.c_[np.cos(2*np.pi*dl),np.sin(2*np.pi*dl),dl+10]
coil3 = magpy.current.Line(
    current=1,
    vertices=vertices
)


coil2 = magpy.Collection()
for z in np.linspace(10, 15, 10):
    winding = magpy.current.Loop(
        current=100,
        diameter=10,
        position=(0,0,z),
        
    )
    coil2.add(winding)


dl=np.linspace(0,1,10)
where= np.c_[5*np.cos(2*dl*np.pi),5*np.sin(2*dl*np.pi),dl*0+10]
vector= np.c_[np.sin(2*dl*np.pi),-np.cos(2*dl*np.pi),dl*0]
# print(where)    
grid = pv.UniformGrid(
    dims=(41, 41, 41),
    spacing=(2, 2, 2),
    origin=(-40, -40, -40),
)

# compute B-field and add as data to grid
B = coil1.getB(coil3.vertices)
#print(vector)
print("-"*50)
print(B)
print("-"*50)

#force=np.cross(vector,B)
#print(force)

# Bamp /= np.amax(Bamp)
# print
# print('-'*10)
# print(B)

""" # compute field lines
seed = pv.Disc(inner=1, outer=5.2, r_res=3, c_res=12)
strl = grid.streamlines_from_source(
    seed,
    vectors='B',
    max_time=180,
    initial_step_length=0.01,
    integration_direction='both',
)

# create plotting scene
pl = pv.Plotter()

magpy.show(coil1, canvas=pl, backend='pyvista')
# add streamlines
pl.add_mesh(
    strl.tube(radius=.2),
    cmap="bwr",
    
)
# display scene
pl.camera.position=(160, 10, -10)
pl.set_background("white")
pl.show() """
""" turn=5
ts = np.linspace(-turn/2, turn/2, 10)
len = 1 
ts_len = ts*len/turn
dia=1
vertices = np.c_[dia*np.cos(ts*2*np.pi), dia*np.sin(ts*2*np.pi), ts_len]
coil2 = magpy.current.Line(
    current=1,
    vertices=vertices
)
turn=5
ts = np.linspace(-turn/2, turn/2, 10)
len = 1 
ts_len = ts*len/turn
dia=1
vertices = np.c_[dia*np.cos(ts*2*np.pi), dia*np.sin(ts*2*np.pi), ts_len]
coil3 = magpy.current.Line(
    current=1,
    vertices=vertices
)
coil3.move((0,0,5))
ts = np.linspace(4, 4.5, 10)
vertices = np.c_[5*np.cos(ts*2*np.pi), 5*np.sin(ts*2*np.pi), ts]
coil3 = magpy.current.Line(
    current=100,
    vertices=vertices
) """

#rotate upside down   
#coil1.rotate_from_euler(180,'x')

""" 
ts = np.linspace(-20, 20, 40)
grid = np.array([[(x,0,z) for x in ts]for z in ts])

B = magpy.getB(coil1, grid)
Bamp = np.linalg.norm(B, axis=2)
Bamp /= np.amax(Bamp)
print(Bamp)
sp = plt.streamplot(
    grid[:,:,0], grid[:,:,2], B[:,:,0], B[:,:,2],
    density=2,
    color=Bamp,
    linewidth=np.sqrt(Bamp)*3,
    cmap='coolwarm',
)
plt.colorbar(sp.lines, label='[mT]')
#plt.show()
"""
coils=magpy.Collection(coil1,coil3)

coils.show()

#print(magpy.getB(coil1,coil2.position))