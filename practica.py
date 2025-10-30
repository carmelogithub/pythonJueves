unidades=15
precio=7.5
subtotal=unidades*precio
iva=0.21
cuotaIva=subtotal*iva
total=subtotal+cuotaIva

print("El subtotal es "+str(subtotal))
print(f"La cuota de IVA es {cuotaIva}") #format moderno
print("El total de la factura es ",total)

mensaje="Esto es \"muy\" importante"
mensaje2='Esto es "muy" importante'
print(mensaje)
print(mensaje2)

ciudad="Madrid" #array de caracteres
print(ciudad[1])