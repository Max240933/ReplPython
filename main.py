
print("Hola, te pedire a continuacion los siguientes datos")
import re



while True:
  Nombre = input ("Dame el nombre del producto: ")
  if len(Nombre) >=10 and len(Nombre) <=30:
    break

while True:
  Precio = input ("Dime el precio del producto: ")
  if Precio.isdigit:
    break

while True:   
  codigo = input ("Dame el codigo: ") 
  coincide = re.search("^[A-Z]{2}-[0-9]{4}$")
  if coincide:
    break

