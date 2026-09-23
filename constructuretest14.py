#temperature convertor

class temperature:
    def __init__(self,celsius):
        self.celsius=celsius

    def convert(self):
        fahrenheit=(self.celsius*9/5)+32
        print("fahrenheit:",fahrenheit)

t1=temperature(25)
t1.convert()
