def obtener_puntuacion_y_comentario():
    while True:
        puntuacion = input("Por favor, introduzca una puntuación (1-5): ")
        if puntuacion.isdigit():
            puntuacion = int(puntuacion)
            if 1 <= puntuacion <= 5:
                comentario = input("Por favor, introduzca un comentario: ")
                return puntuacion, comentario
            else:
                print("Indíquelo en una escala de 1 a 5")
        else:
            print("Por favor, introduzca un número")

def guardar_datos(puntuacion, comentario):
    with open("data.txt", "a") as file:
        file.write(f"Puntuación: {puntuacion}, Comentario: {comentario}\n")

def mostrar_resultados():
    with open("data.txt", "r") as file:
        print(file.read())

while True:
    print("Seleccione el proceso que desea aplicar:")
    print("1: Ingresar puntuación y comentario")
    print("2: Comprueba los resultados obtenidos hasta ahora.")
    print("3: Finalizar")

    opcion = input()
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 1:
            puntuacion, comentario = obtener_puntuacion_y_comentario()
            guardar_datos(puntuacion, comentario)
        elif opcion == 2:
            mostrar_resultados()
        elif opcion == 3:
            print("Finalizando")
            break
        else:
            print("Introduzca un número del 1 al 3")
    else:
        print("Introduzca un número del 1 al 3")