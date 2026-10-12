# ---- Polymorphism----
# <Q1> What is polymorphism ?
# -->it is a one of the important pilllors of OOP.
# the same name entity behaves differently at diffrent times and is called as polymorphism.

# * poly means ------> "many"
# * morph     -------> "form"
# =====================================================================================================
# There are two types of polymorphism.
# <1> Overloading:
                # 1> Operator Overloading
                # 2> Method/constructor Overloading

# <2> Overriding:
                # 1> Method Overriding
                # 2> Variable Overriding   (not required in python) 
# ==========================================================================================================



# class book:
#     def __init__(self, n, p):
#         self.name = n
#         self.price = p         
    
# b1 = book("core python", 200)
# b2 = book("advance python", 600)
# print(b1+ b2)     #TypeError: unsupported operand type(s) for +: 'book' and 'book'



# operatior overloading
class book:
    def __init__(self,t,p):
        self.tital = t
        self.price = p
    def __add__(self, other):
        return self.price + other.price   
        
b1 = book("core python",200)
b2 = book("advance python",600)
print(b1 + b2)

# ========================================================================================================
# task 1> all operator use in operator overloading
class Book:
    def __init__(self, t, p):
        self.title = t
        self.price = p

    # ---- Arithmetic ----
    def __add__(self, other):         # +
        return self.price + other.price

    def __sub__(self, other):         # -
        return self.price - other.price

    def __mul__(self, n):             # *
        return self.price * n

    def __truediv__(self, n):         # /
        return self.price / n

    def __floordiv__(self, n):        # //
        return self.price // n

    def __mod__(self, n):             # %
        return self.price % n

    def __pow__(self, n):             # **
        return self.price ** n

    # ---- Comparison ----
    def __eq__(self, other):          # ==
        return self.price == other.price

    def __ne__(self, other):          # !=
        return self.price != other.price

    def __lt__(self, other):          # <
        return self.price < other.price

    def __le__(self, other):          # <=
        return self.price <= other.price

    def __gt__(self, other):          # >
        return self.price > other.price

    def __ge__(self, other):          # >=
        return self.price >= other.price

    # ---- Unary ----
    def __neg__(self):                # -obj
        return -self.price

    def __abs__(self):                # abs(obj)
        return abs(self.price)

    # ---- Augmented assignment ----
    def __iadd__(self, amount):       # +=
        self.price += amount
        return self                   # self return karna zaroori hai

    def __isub__(self, amount):       # -=
        self.price -= amount
        return self

    # ---- Special ----
    def __str__(self):                # print(obj)
        return f"{self.title} - Rs.{self.price}"

    def __len__(self):                # len(obj)
        return len(self.title)


b1 = Book("core python", 200)
b2 = Book("advance python", 600)

# ---- Arithmetic ----
print(b1 + b2)     # 800
print(b2 - b1)     # 400
print(b1 * 2)      # 400
print(b2 / 4)      # 150.0
print(b2 // 7)     # 85
print(b2 % 7)      # 5
print(b1 ** 2)     # 40000

# ---- Comparison ----
print(b1 == b2)    # False
print(b1 != b2)    # True
print(b1 < b2)     # True
print(b1 <= b2)    # True
print(b1 > b2)     # False
print(b1 >= b2)    # False

# ---- Unary ----
print(-b1)         # -200
print(abs(b1))     # 200

# ---- Augmented ----
b1 += 50
print(b1.price)    # 250
b1 -= 100
print(b1.price)    # 150

# ---- Special ----
print(b1)          # core python - Rs.150
print(len(b1))     # 11

