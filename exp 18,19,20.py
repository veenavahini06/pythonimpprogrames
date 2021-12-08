
#write a python program to convert an integer into roman numeral
import sys

ROMAN_NUMERAL_TABLE = [ ("M", 1000), ("CM", 900), ("D", 500),
("CD", 400), ("C", 100), ("XC", 90),
("L", 50),	("XL", 40), ("X", 10),
("IX", 9),	("V", 5),	("IV", 4),
("I", 1)
]
class Roman(object):

   def convert_to_roman(self, number):
        roman_numerals = []
        for numeral, value in ROMAN_NUMERAL_TABLE:
            while value <= number:
                number -= value
                roman_numerals.append(numeral)
                return ''.join(roman_numerals)


n=int(input("Enter a number: "))
r = Roman()
print("The roman value of ",n,"is = ", r.convert_to_roman(n))

#write a python program to implement pow(x,n)
class py_solution: 
   def pow(self, x, n):
      if x==0 or x==1 or n==1:
         return x
      if x==-1:
         if n%2 ==0:
            return 1
         else:
            return -1
      if n==0:
         return 1
      if n<0:
         return 1/self.pow(x,-n)
      val = self.pow(x,n//2)
      if n%2 ==0:
          return val*val
      return val*val*x

while True:
    print("Enter q or Q to quit ")
    x=input("Enter x value: ")
    if (x=='q' or x=='Q'):
        break
    else:
      n=input("Enter n value: ")
      n=int(n)
      x=int(x)
      p=py_solution()
      q=p.pow(x,n)
    print(x," to the power ",n," is = ",q)
    print()
    continue

#write a python class to reverse a string word by word    
class py_solution:
    def reverse_words(self, s):
        lst = s.split(" ")
        lst = lst[::-1]
        st=""
        for w in lst:
            st = st + " " + w
        return st

s=input("Enter a string: ")
rs=py_solution()
r = rs.reverse_words(s) 
print("The reversed sentence: ",r)

