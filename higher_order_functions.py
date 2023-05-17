## higher oreder functions

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(3, 3, sum_one))

print(sum_two_values_and_add_value(3, 3, sum_five))

### Closures 
from functools import reduce

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))

print(sum_ten(5)(1))

## built-in higher oreder functions

numbers = [2, 5, 10, 21, 3, 30]
# Map
def multiply_two(number):
    return number * 2 
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
def filter_greater_that_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))



'''lista = []

acumulador = 0
dato = int(input('Ingrese el número de veces que va a iterar: '))
ask_data = 0
var = 1
while dato > acumulador:
    if dato == 0:
      print('Ingrese un número mayor que cero')
    elif dato > 0:
      ask_data = int(input('Ingrese un número: '))
      lista.append(int(ask_data))
    acumulador += 1

def sum_values(ask_data):
    print(ask_data)
    return ask_data - ask_data

#print(reduce(sum_two_values, lista))

def multiply_values(lista):
    global var
    var = 1
    for i in lista:
        var = var * i
    return var



#print(multiply_values(lista))

def division_values(lista): 
    for divisor in range(len(lista)):
        lista[divisor] /= divisor
    return divisor

print(division_values(lista))'''
