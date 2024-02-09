import math

# input
r = input("Ingrese el radio:")
r = int(r)

# processing
a = math.pi* r**2
p = 2* math.pi*r

# output
print("El àrea es:"+ str(a))
print("El perìmetro es:" + str(p))