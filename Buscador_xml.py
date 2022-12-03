#!/usr/bin/env python3
import re
import tkinter.filedialog
import os

print("Buscador XML".center(80, "="))

def get_quote(text: str, field_search: int):        #obtener la palabra clave en el archivo xml
    start_q = text.find("\"", field_search)         #encontrar en donde comienza la palabra buscada
    end_q = text.find("\"", start_q + 1)            #donde termina la palabra buscada
    quote = text[start_q : end_q + 1]               #obtiene el resultado dentro de donde empieza y termina la palabra
    return quote

def xml_finder():

    file_name = tkinter.filedialog.askopenfilename()
    file = open(file_name, encoding="utf-8")
    text = file.read()
    os.system('cls')

    while True:
    #Que voy a buscar
        print("".ljust(80, "-"))
        print("Que buscas? (Solo XML)")
        print("1. Nombre emisor\n"
              "2. Nombre facturado\n"
              "3. Descripcion\n"
              "4. Fecha\n"
              "5. Cantidad de pago\n"
              "6. Metodo de pago")
        buscar = int(input("Selecciona una opcion a buscar: \n"))   #selecciona opcion dentro las opciones

        if buscar == 1:
            field_search = text.find('Nombre')                      #encuentra el primer nombre, que es el emisor
            quote = get_quote(text, field_search)

            print("Facturado = {}".format(quote))

        if buscar == 2:
            field_search = text.rfind('Nombre')                     #encuentra segundo nombre, que es el facturado
            quote = get_quote(text, field_search)

            print("Facturado = {}".format(quote))

        if buscar == 3:
            print("Descripcion")                                    #encuentra descripcion
            result = re.finditer("Descripcion", text)
            for match in result:                                    #encuentra todos los elementos de la descripcion
                quote = get_quote(text, match.start())

                print(quote)

        if buscar == 4:
            field_search = text.find('Fecha')                       #encuentra la fecha
            quote = get_quote(text, field_search)

            print("Fecha = {}".format(quote))

        if buscar == 5:
            field_search = text.find(' Total')                      #Encuentra el total
            quote = get_quote(text, field_search)

            print("Total = {}".format(quote))

        if buscar == 6:
            print("Metodo de pago: ")                               #Encuentra el metodo de pago PPD o PUE
            field_search = text.find(' MetodoPago')
            quote = get_quote(text, field_search)

            if quote == ('"PPD"'):
                print("Pago en parcialidades o diferido")
            elif quote == ('"PUE"'):
                print("Pago en una sola exhibicion")

        print("".ljust(80, "-"))
        cont = input("Deseas continuar? (s/n)")                     #terminar o continuar con el programa
        if cont =='s':
            os.system('cls')
            continue

        else:
            os.system('cls')
            break


while True:                                       
    print("Selecciona una opcion")                                  #Inicio del programa, selecciona un archivo
    print("1. Seleccionar archivo\n"
          "2. Salir")
    con = int(input())

    if (con==1):
        xml_finder()

    else:
        print("Gracias")
        break
