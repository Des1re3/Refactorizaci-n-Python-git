def introducir_puntaje():
    while True:
        print( 'Por favor, introduzca una puntuación en una escala de 1 a 5' )
        point = input()
        if point.isdecimal():
            point = int(point)
            if  point <= 0 or point > 5:
                print( 'Indíquelo en una escala de 1 a 5!!' )
            else:
                print( 'Introduzca sus comentarios.' )
                comment = input()
                ingresar_datos(point, comment)
                break
        else: 
            print( 'Introduzca los puntos de valoración como números' )

def imprimir_resultados():
    print( 'Resultados hasta la fecha.' )
    read_file = open("data.txt", "r")
    print( read_file.read() )
    read_file.close()
    
def ingresar_datos(punto, comentario):
    post = f'Punto: {punto} \t Comentario: {comentario}'
    file_pc = open("data.txt", 'a')
    file_pc.write( f'{ post } \n' )
    file_pc.close()


#---------------

while True:
    print( 'Seleccione el proceso que desea aplicar' )
    print( '1: Introduzca los puntos de valoración y los comentarios.' )
    print( '2: Comprueba los resultados obtenidos hasta ahora.' )
    print( '3: Terminación.' )
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            introducir_puntaje()
        elif num == 2:
            imprimir_resultados()
        elif num == 3:
          print( 'Terminación.' )
          break
        else:
            print( 'Por favor, introduzca del 1 a 3' )
    else:
        print( 'Por favor, introduzca del 1 a 3' )