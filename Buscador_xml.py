import re
import tkinter.filedialog

#Buscar y abrir el archivo 
file_name = tkinter.filedialog.askopenfilename()
file = open(file_name, 'r')
text = file.read()
cont = 's'

while (cont=='s'):
    #Que voy a buscar
    print("Que buscas? (Solo XML)")
    print("1. Nombre emisor\n"
          "2. Nombre facturado\n"
          "3. Descripcion\n"
          "4. Fecha\n"
          "5. Cantidad de pago\n"
          "6. Metodo de pago")
    buscar = int(input("Selecciona una opcion a buscar: \n"))

    if buscar == 1:
        field_search = text.find('Nombre')
        start_q = text.find("\"", field_search)
        end_q = text.find("\"", start_q+1)
        quote = text[start_q:end_q+1]

        print("Emisor = {}".format(quote))
    
    if buscar == 2:
        field_search = text.rfind('Nombre')
        start_q = text.find("\"", field_search)
        end_q = text.find("\"", start_q+1)
        quote = text[start_q:end_q+1]

        print("Facturado = {}".format(quote))
    
    if buscar == 3:
        print("Descripcion")
        result = re.finditer("Descripcion:", text)
        for match in result:
            start_q = text.find("\"", match.start())
            end_q = text.find("\"", start_q + 1)
            quote = text[start_q:end_q+1]

            print(quote)
    
    if buscar == 4:
        field_search = text.find('Fecha')
        start_q = text.find("\"", field_search)
        end_q = text.find("\"", start_q+1)
        quote = text[start_q:end_q+1]

        print("Fecha = {}".format(quote))

    if buscar == 5:
        field_search = text.find(' Total')
        start_q = text.find("\"", field_search)
        end_q = text.find("\"", start_q+1)
        quote = text[start_q:end_q+1]

        print("Total = {}".format(quote))

    if buscar == 6:
        print("Metodo de pago: ")
        field_search = text.find(' MetodoPago')
        start_q = text.find("\"", field_search)
        end_q = text.find("\"", start_q+1)
        quote = text[start_q:end_q+1]
    
        if quote == ('"PPD"'):
            print("Pago en parcialidades o diferido")
        elif quote == ('"PUE"'):
            print("Pago en una sola exhibicion")
    
    cont = input("Deseas continuar? (s)i o (n)o \n")
file.close()
    

