class Complex:
    # __init__ method
    # Create 'Complex' object 'a+bi' by given
    # 'a' is real part of a complex number
    # 'b' is imaginary part a complex number
    def __init__(self,a,b):
        self.real = a
        self.imaginary = b
    
    # __str__ method
    # This method can convert Complex(2,3) to string "2+3i"
    def __str__(self):
        # Assign the value from object to variable
        a = self.real
        b = self.imaginary
        complex_str = ""

        # Case 1: Imaginary part is 0 (b = 0)
        # Example: Complex(0,0) = 0
        # Example: Complex(5,0) = 5
        if(b == 0):
            complex_str = str(a)
        
        # Case 2: Real part is 0 and real part isn't 0 (a = 0, b != 0)
        elif(a == 0 and b != 0):
            # Case 2.1: Imaginary part is 1 (a = 0, b = 1)
            # Example: Complex(0,1) = i
            if(a == 0 and b == 1):
                complex_str = "i"
            # Case 2.2: Imaginary part is -1 (a = 0, b = -1)
            # Example: Complex(0,1) = -i
            elif(a == 0 and b == -1):
                complex_str = "-i"
            # Case 2.3: Imaginary part is any number that is not 1, 0 or -1
            # Example: Complex(0,7) = 7i
            else:
                complex_str = str(b) + "i"
        
        # Case 3: Imaginary part is 1 and real part isn't 0 (a != 0, b = 1)
        # Example: Complex(5,1) = 5+i
        elif(a != 0 and b == 1):
            complex_str = str(a) + "+i"
        
        # Case 4: Imaginary part is -1 and real part isn't 0 (a != 0, b = 1)
        # Example: Complex(5,-1) = 5-i
        elif(a != 0 and b == -1):
            complex_str = str(a) + "-i"
        
        # Case 5: Imaginary part > 1 and real part isn't 0 (a != 0, b > 1)
        # Example: Complex(5,8) = 5+8i
        elif(a != 0 and b > 1):
            complex_str = str(a) + "+" + str(b) + "i"
        
        # Case 6: Imaginary part < 1 and real part isn't 0 (a != 0, b < 1)
        # Example: Complex(7,-9) = 7-9i
        elif(a != 0 and b < 1):
            complex_str = str(a) + str(b) + "i"
        
        # Retrun complex number as a string
        return complex_str
    
    # __add__ method
    # This method can find sum of 2 complex number
    # 'self' is a+bi and 'rhs' is c+di
    # So the sum will be (a+b) + (c+d)i
    # Example: a = Complex(5,6) and b = Complex(7,8)
    # a.add(b) returns "12+14i"
    def __add__(self, rhs):
        # Assign the value from object to variable
        a = self.real
        b = self.imaginary
        c = rhs.real
        d = rhs.imaginary
        
        # Find the sum
        SUM = Complex(a+c, b+d)
        
        # Return a value
        return SUM
    
    # __mul__ method
    # This method can find a product of 2 complex number
    # 'self' is a+bi and 'rhs' is c+di
    # So the product will be (ac-bd) + (ad+bc)i
    def __mul__(self, rhs):
        # Assign the value from object to variable
        a = self.real
        b = self.imaginary
        c = rhs.real
        d = rhs.imaginary

        # Find a product
        Real = (a*c) - (b*d)
        Imaginary = (a*d) + (b*c)
        PRODUCT = Complex(Real, Imaginary)

        # Return a value
        return PRODUCT
    
    # __truediv__ method
    # This method can find a quotient of 2 complex number
    # 'self' is a+bi and 'rhs' is c+di
    # So the quotient will be [(ac+bd)/(c^2 + d^2)] + [(-ad+bc)/(c^2 + d^2)]i
    def __truediv__(self, rhs):
        # Assign the value from object to variable
        a = self.real
        b = self.imaginary
        c = rhs.real
        d = rhs.imaginary

        # Find a quotient
        Real = (a*c + b*d)/(c**2 + d**2)
        Imaginary = (-1*a*d + b*c)/(c**2 + d**2)
        QUOTIENT = Complex(Real, Imaginary)

        # Return a value
        return QUOTIENT

# Input value
t,a,b,c,d = [int(x) for x in input().split()]

# Create object
c1 = Complex(a,b)
c2 = Complex(c,d)

# Output
if(t == 1):
    print(c1)
elif(t == 2): 
    print(c2)
elif(t == 3): 
    print(c1+c2)
elif(t == 4): 
    print(c1*c2) 
else: 
    print(c1/c2)