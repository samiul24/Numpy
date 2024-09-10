
import numpy as np
from numpy import random
import matplotlib.pyplot as pl

class IntArray:
    def __init__(self, int_array) -> None:
        if not isinstance(int_array, np.ndarray) or int_array.dtype != int:
            raise ValueError('Input array should be integer value')
    
        self.int_array = int_array


    def display(self):
        print(self.int_array)

    
    def salary(self):
        array_shape = self.int_array.shape #return array shape
        #print(array_shape)
        #money_for_product = np.full(array_shape, random.randint(100)) #full is a function that is return the same elemet.
        money_for_product = random.randint(100, size=(array_shape)) #generate random values+size
        profite = self.int_array*money_for_product
        print(f"product price {self.int_array} and respective profite {profite}")


    def min_productivity(data_frame):
        pass

    
    def show_data(self):
        #x = np.arange(len(self.int_array))
        x = np.arange(1,len(self.int_array)+1) #arange function generates value as secquentially where as random generates discreate value based on range
        print(x)
        pl.plot(x, self.int_array, marker='*')
        pl.title('Product VS Price')
        pl.xlabel('Product Quantity')
        pl.ylabel('Perice Per Unit')
        pl.xticks(x) #x-axis values populated based on xticks(x)
        pl.grid()
        pl.show()