import re
import tkinter.filedialog

#Buscar y abrir el archivo 
file_name = tkinter.filedialog.askopenfilename()


def get_quote(text: str, field_search: int):
    start_q = text.find("\"", field_search)
    end_q = text.find("\"", start_q+1)
    quote = text[start_q:end_q+1]
    return quote

def xml_finder():
    with open(file_name) as file:
        text = file.read()
    cont = "s"

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
            quote = get_quote(text, field_search)

            print("Emisor = {}".format(quote))
        
        if buscar == 2:
            field_search = text.rfind('Nombre')
            quote = get_quote(text, field_search)

            print("Facturado = {}".format(quote))
        
        if buscar == 3:
            print("Descripcion")
            result = re.finditer("Descripcion:", text)
            for match in result:
                quote = get_quote(text, match.start())
                print(quote)
        
        if buscar == 4:
            field_search = text.find('Fecha')
            quote = get_quote(text, field_search)

            print("Fecha = {}".format(quote))

        if buscar == 5:
            field_search = text.find(' Total')
            quote = get_quote(text, field_search)

            print("Total = {}".format(quote))

        if buscar == 6:
            print("Metodo de pago: ")
            field_search = text.find(' MetodoPago')
            quote = get_quote(text, field_search)
        
            if quote == ('"PPD"'):
                print("Pago en parcialidades o diferido")
            elif quote == ('"PUE"'):
                print("Pago en una sola exhibicion")
        
        cont = input("Deseas continuar? (s)i o (n)o \n")



if __name__ == "__main__":
    xml_finder()
    

