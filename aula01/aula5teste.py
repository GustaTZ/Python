# Teste1
"""
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 3
"""

#Teste2
"""
for contador in range (1,11,3):
    print(contador)
"""

#Teste3
"""
i = 1
while(i <= 7):
    print(i)
    i = i + 1
    if(i == 5):
        break
"""
#Teste4
"""
for i in range(1,8):
    if(i == 5):
        continue
    print(i)
"""


#Formatação de floats
#Teste5
"""
print("R$ {}".format(1.59))
R$ 1.59
"""

#Teste6
"""
print("R$ {:f}".format(1.59))
R$ 1.590000
"""

#Teste7
"""
print("R$ {:.2f}".format(1.59))
R$ 1.59
"""

#Teste8
"""
print("R$ {:.2f}".format(1.5))
R$ 1.50
print("R$ {:.2f}".format(1234.50))
R$ 1234.50
"""

#Teste9
"""
print("R$ {:7.2f}".format(1234.50))
R$ 1234.50
print("R$ {:7.2f}".format(1.5))
R$    1.50
"""


#Formatação de inteiros
#Teste10
"""
print("R$ {:07d}".format(4))
R$ 0000004
"""

#Teste11
"""
print("Data {:02d}/{:02d}".format(9, 4))
Data 09/04
print("Data {:02d}/{:02d}".format(19, 11))
Data 19/11
"""

#Teste12
"""
print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))
"""
#Teste13
"""
"R$ {:7.1f}".format(1000.12)
"R$ {:07.2f}".format(4.11)
"""