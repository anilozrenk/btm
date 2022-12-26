import numpy as np

class Bobin():
    
     def __init__(self, _turn, _current, _radius, _lenght, _position, _step):
          self.turn=_turn
          self.current=_current
          self.radius=_radius
          self.lenght=_lenght
          self.position=_position
          self.step=_step
         
         
     def generate_vertices(self):
          dl=np.linspace(0,self.turn,self.step)
          self.vertices=np.c_[np.cos(2*np.pi*dl)*0.2,np.sin(2*np.pi*dl)*0.2,((dl-self.turn/2)/self.magic)]
