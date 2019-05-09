import numpy as np
#activation function
def activation(x):
  return np.heaviside(x,1)
Class Neuron :
  def __init__(self,weigths,bias):
    self.weigths=weigths
    self.bias=bias
  def forward():
    sum=np.dot(self.weights,inputs)+self.bias
    return activation(sum)
input(    
    
