print("Ejercicios Operadores ")
'''
**Nota:** Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

1. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos 
(es suficiente con mostrar True o False):
   - Si los dos números son iguales
   - Si los dos números son diferentes
   - Si el primero es mayor que el segundo
   - Si el segundo es mayor o igual que el primero

**Ejemplo de ejecución:**
```
Introduce un número entero: 2
Introduce otro número entero: 2
Son los dos números iguales: True
Son los dos números diferentes: False
El primero es mayor que el segundo: False
El segundo es mayor o igual que el primero: True
'''
'''
numero_primero = input("Introduce un numero cualquiera: ")

numero_segundo = input("Introduce un segundo numero cualquiera: ")

print("Los dos numeros son iguales : ", numero_primero == numero_segundo)
print("Los dos numeros son diferentes : " , numero_segundo != numero_primero)
print("El primer numero es mayor que el segundo : ", numero_primero > numero_segundo )
print("El segundo numero es mayor o igual que el primero : " , numero_segundo >= numero_primero)
'''

'''
2. Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario 
tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiente con mostrar True o False).

'''
'''

resultado = ""

cadena = str(input("Introduce una cadena de texto :  "))

if len(cadena ) >= 3 and len(cadena) > 10 :
    resultado= True
else:
    resultado = False

print(resultado)
'''
'''
Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)

Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que es un número)

Multiplica el numero_usuario por 9 en sí mismo

Multiplica el numero_magico por el numero_usuario en sí mismo

Finalmente muestra el valor final del numero_magico por pantalla
'''
'''
numero_magico = 12345679

correcto = False
while not correcto:
    numero_usuario = int(input("Introduce un numero del 1 al 9 : "))
    if numero_usuario in range (1, 9):
        correcto = True
    else: 
        print("Introduce un numero correcto pofavor")
    
numero_usuario = numero_usuario*9

numero_magico = numero_magico*numero_usuario

print("Este es el numero_magico: ", numero_magico)
'''

print("Ejercicios Flujos de Datos ")
'''
Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números.

Mostrar una resta de los dos números (el primero menos el segundo).

Mostrar una multiplicación de los dos números.

En caso de no introducir una opción válida, el programa informará de que no es correcta.
'''
'''
Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
'''
'''
Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
'''
'''
Sugerencia: Puedes utilizar las funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.
'''
'''
Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.
'''