import ctypes

class ArrayList:
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.arraylist = self.make_array(self.capacity)

    def GetItem(self,index):
        if index < 0:
            index = self.length - index

        if 0 <= index < self.length:
            return self.arraylist[index]
        else:
            return IndexError('key is out of bounds')

    def append(self,value):
        if self.length >= self.capacity:
            temp = self.make_array(2*self.capacity)
            for i in range(0,self.length):
                temp[i] = self.arraylist[i]

            self.arraylist = temp
            self.capacity *= 2

        self.arraylist[self.length] = value
        self.length += 1

    def len(self):
        return self.length

    def make_array(self,size):
        return(ctypes.py_object*size)()