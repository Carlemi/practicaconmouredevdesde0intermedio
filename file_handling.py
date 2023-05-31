# File Handling

# .txt file
import os

txt_file = open('../python_intermedio/my_file.txt', 'w+') # Leer y escribir
txt_file.write('Mi nombre es Carlos\nMi apellido es Mendoza\n30 años\ny mi lenguaje favorito es Python\nAunque también me gusta Php')
print(txt_file.read())
#print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write('\nAunque también me gusta Php')
txt_file.close()

with open('../python_intermedio/my_file.txt', 'a') as my_other_file:
    my_other_file.write('\nY JavaScript')

#os.remove('../python_intermedio/my_file.txt')