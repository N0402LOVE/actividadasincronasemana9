#Inicio del programa

print("\t♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
print("\t♦Bienvenidos a nuestro programa♦")
print("\t♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦ \n")

#Indicacion para el usuario

print("\nIngrese los datos que se solicitan para ver a que etapa pertenece")

Nombre = input("\nIngrese su nombre -> ")
Apellido = input("\nIngrese su apellido -> ")
Edad = int(input("\nIngrese su edad -> "))
Sexo = input("Ingrese su sexo -> ").lower()

#Condicion mientras el usuario ingrese femenino

if Sexo == 'femenino' or Sexo == 'f' or Sexo == 'mujer':
    if Edad >= 0 and Edad <= 18:
        print(f"{Nombre} {Apellido} Usted es una niña.")
        
        if Edad >= 0 and Edad <= 2:
            print("Usted esta en la etapa de bebé")
            
        elif Edad >= 3 and Edad <= 5:
            print("Usted en la etapa de la infancia")
            
        elif Edad >= 6 and Edad <= 11:
            print("Usted esta en la etapa de niñes")
            
        elif Edad >= 12 and Edad <= 18:
            print("Usted esta en la etapa de la adolescencia")
    
    elif Edad >= 19 and Edad <= 26:
        print(f"{Nombre} {Apellido} Usted es una señorita")
        
        if Edad >= 19 and Edad <= 26:
            print("Usted esta en la etapa de la juventud")
            
    elif Edad >= 27 and Edad <= 55:
        print(f"{Nombre} {Apellido} Usted es una señora")
        
        if Edad >= 27 and Edad <= 40:
            print("Usted esta en la etapa de la adultez joven")
        
        elif Edad >= 41 and Edad <= 55:
            print("Usted esta en la etapa de la adultez")
            
    elif Edad >= 56 and Edad <= 100:
        print(f"{Nombre} {Apellido} Usted es una abuela")
        
        if Edad >= 56 and Edad <= 65:
            print("Usted esta en la etapa de la persona mayor")
            
        elif Edad >= 66 and Edad <= 100:
            print("Usted esta en la etapa de la tercera edad")
            
    else:
        print(f"{Nombre} {Apellido} La edad que usted ingresó es inexistente")
        
# Condicion mientras el usuario ingrese masculino

elif Sexo == 'masculino' or Sexo == 'm' or Sexo == 'niño':
    if Edad >= 0 and Edad <= 18:
        print(f"{Nombre} {Apellido} Usted es un niño")

        if Edad >= 0 and Edad <= 2:
            print("Usted esta en la etapa de bebé")

        elif Edad >= 3 and Edad <= 5:
            print("Usted en la etapa de la infancia")

        elif Edad >= 6 and Edad <= 11:
            print("Usted esta en la etapa de niñes")

        elif Edad >= 12 and Edad <= 18:
            print("Usted esta en la etapa de la adolescencia")

    elif Edad >= 19 and Edad <= 26:
        print(f"{Nombre} {Apellido} Usted es un caballero")

        if Edad >= 19 and Edad <= 26:
            print("Usted esta en la etapa de la juventud")

    elif Edad >= 27 and Edad <= 55:
        print(f"{Nombre} {Apellido} Usted es un señor")

        if Edad >= 27 and Edad <= 40:
            print("Usted esta en la etapa de la adultez joven")

        elif Edad >= 41 and Edad <= 55:
            print("Usted esta en la etapa de la adultez")

    elif Edad >= 56 and Edad <= 100:
        print(f"{Nombre} {Apellido} Usted es una abuelo")

        if Edad >= 56 and Edad <= 65:
            print("Usted esta en la etapa de la persona mayor")

        elif Edad >= 66 and Edad <= 100:
            print("Usted esta en la etapa de la tercera edad")

    else:
        print(f"{Nombre} {Apellido} La edad que usted ingresó es inexistente")
        
else:
    print("Su sexo no se encuentra en el registro")
    
Par = Edad % 2

if Par == 0:
    print("\nSu edad es par")
else:
    print("\nSu edad es impar")
  
print("Fin del programa ")  