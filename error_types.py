## error types

# SyntaxError

#print '¡Hola comunidad!' descomentar para Error
print('¡Hola comunidad!')

# NameError
language = 'Spanish'  #comentar para error
print(language)


#IndexError
my_list = ['Python', 'Swift', 'Kotlin', 'Dart', 'JavaScript']
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5])  Descomentar para error


# ModuleNotFoundError

#import maths Descomentar para error
import math

# AttributeError

# print(math.PI) descomentar para error
print(math.pi)


# KeyError

my_dict = {'Nombre':'Carlos', 'Apellido':'Mendoza', 'Edad':30, 1:'Python'}
print(my_dict['Edad'])
# print(my_dict['Apelido']) descomentar para error
print(my_dict['Apellido'])




# TypeError
#print(my_list['0']) descomentar para error
print(my_list[0])



# ImportError
# from math import PI  descomentar para error
from math import pi


# ValueError
# my_int = int('10 años') descomentar para error
my_int = int('10')

print(my_int)


# ZeroDivisionError

print(4/2)
print(4/0)