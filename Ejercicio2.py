'''
1.1 Dado el siguiente diccionario, cambia el valor de la clave "edad" por 25.
     persona={"nombre":'Juan',"edad":10}
1.2 Declara una variable "precio" y asignale el valor 25. Luego crea una variable "impuesto" y asígnale el valor precio multiplicado por 0.21.
    Muestra ambos valores por consola de esta forma:
         El precio es 25 y el impuesto es 5.25

1.3 Dado el siguiente diccionario, imprime con un print el valor de la clave "apellido".
   persona ={"nombre":'Juan',apellido:'Pérez' } 
   
1.4 Crea un diccionario llamdo "producto" que tenga las claves "nombre", "precio" y "cantidad". Asigna valores a estas claves y luego muestra el diccionario completo por consola'''

persona = {"nombre":'Juan', "edad":10}
persona["edad"] = 25
#print(persona["edad"])

precio=25 
impuesto = precio * 0.21
#print(impuesto)
#print(f"El precio es {precio} y el impuesto es {impuesto}")

persona ={"nombre":"Juan", "apellido":"Pérez"}
#print(persona["apellido"])

producto = {"nombre":'Ordenador', "precio":800 , "cantidad": 1301}
print(producto)
