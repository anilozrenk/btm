import numpy as cp
class Coil:
    def __init__(self, np_grid_x,np_grid_y,np_grid_z,vertex_list=[],cur_list=[],u_field=0,dl_total=1000):
        #assert len(vertex_list) != cur_list,"make sure vertexlist and current list adds up"
        self.grid_x=cp.asarray(np_grid_x)
        self.grid_y=cp.asarray(np_grid_y)
        self.grid_z=cp.asarray(np_grid_z)
        self.shape=cp.hstack((cp.zeros(self.grid_x.ravel()[:, cp.newaxis].shape),cp.zeros(self.grid_y.ravel()[:, cp.newaxis].shape),cp.zeros(self.grid_z.ravel()[:, cp.newaxis].shape))).reshape(self.grid_x.shape + (3,)).shape
        self.b_field=cp.zeros(self.shape)
        
        if(u_field==0):
            self.u_field=cp.full(self.shape,4*cp.pi * 1.0e-7)
        else:
            self.u_field=u_field
            
        for idx,vert in enumerate(vertex_list[:-1]):
            self.b_field+=self.calc_b_for_line((vert,vertex_list[idx+1]),cur_list[idx],dl_total)
    def calc_b_inc(self,pos_v,dl,i_val):
        r1_vect = cp.hstack((self.grid_x.ravel()[:, cp.newaxis],  self.grid_y.ravel()[:, cp.newaxis], self.grid_z.ravel()[:, cp.newaxis]))-pos_v
        r1 = cp.sqrt((self.grid_x - pos_v[0])**2 + (self.grid_y - pos_v[1])**2 +(self.grid_z - pos_v[2])**2)
        b1_vect = ((i_val/ 4*cp.pi) * cp.cross(dl,r1_vect)/(r1**3 ).ravel()[:, cp.newaxis]).reshape(self.grid_x.shape + (3,))*self.u_field
        return b1_vect  
    def calc_b_for_line(self,vert,i_val,dl_part):
        dl_vect=(cp.array(vert[1])-cp.array(vert[0]))/dl_part
        b_temp=cp.zeros(self.shape)
        for dl in range(dl_part):
            pos=cp.array(vert[0])+dl_vect*dl
            b_temp+=self.calc_b_inc(pos,dl_vect,i_val)
        return b_temp/dl_part
    def get_b(self):
        return self.b_field