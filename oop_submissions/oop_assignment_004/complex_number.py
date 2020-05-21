import math
class ComplexNumber:
    def __init__(self, real_part = 0, imaginary_part = 0):
        if type(real_part) == str and type(imaginary_part) == str:
            raise ValueError("Invalid value for real and imaginary part")
            
        if type(real_part) == str:
            raise ValueError("Invalid value for real part")
        
        self.real_part = real_part
            
        if type(imaginary_part) == str:
            raise ValueError("Invalid value for imaginary part")
        
        self.imaginary_part = imaginary_part
   
   
    def __str__(self):
        return f'{self.real_part}{self.imaginary_part:+}i'
        
    def conjugate(self):
        return ComplexNumber(self.real_part, -self.imaginary_part)
        
    def __add__(self, other):
        self.add_real = self.real_part + other.real_part
        self.add_img = self.imaginary_part + other.imaginary_part
        return ComplexNumber(self.add_real, self.add_img)
    
    def __sub__(self, other):
        return ComplexNumber(self.real_part - other.real_part, self.imaginary_part - other.imaginary_part)
    
    def __mul__(self, other):
        mul_real = (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part)
        mul_imaginary = (self.real_part * other.imaginary_part) + (other.real_part * self.imaginary_part)
        return ComplexNumber(mul_real, mul_imaginary)
        

    def __truediv__(self, other):
        k = math.sqrt((other.real_part ** 2) + (other.imaginary_part ** 2))
        div_real = round(((self.real_part/k) * (other.real_part/k)) + ((self.imaginary_part/k) * (other.imaginary_part/k)), 2)
        div_img = round(((self.real_part/k) * (- other.imaginary_part/k) + (self.imaginary_part/k) * (other.real_part/k)),2)
        return ComplexNumber(div_real, div_img)
       
       
    def __abs__(self):
        return (round(math.sqrt(self.real_part ** 2 + self.imaginary_part ** 2),3))
        
    def __eq__(self, other):
        return (self.real_part == other.real_part and self.imaginary_part == other.imaginary_part)
        