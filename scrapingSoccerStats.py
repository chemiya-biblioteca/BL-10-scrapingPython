from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

from selenium.common.exceptions import NoSuchElementException

#-boton de las cookies por xpath y click en el
#-encuentro tabla por xpath y busco en ella elementos por clase



#conectar con el web driver-----------------
driver_path = "C:\\Users\\chema\\Desktop\\formacionPracticar\\AAcorreccionesGIT\\scraping\\chromedriver_win32\\chromedriver.exe"


urls = [

    "https://www.soccerstats.com/results.asp?league=germany2&pmtype=bydate",
    "https://www.soccerstats.com/results.asp?league=belgium&pmtype=bydate",

]

nombres = [
    "alemania2.txt", "belgica.txt"

]


posicionNombre = 0
for url in urls:
    #busco la pagina----------------------
    driver = webdriver.Chrome(driver_path)
    driver.get(url)


    #boton de las cookies por xpath y click-------------------
    cookies = driver.find_element(
        "xpath", "/html/body/div[1]/div/div/div/div[2]/div/button[3]")
    cookies.click()



    #encuentro tabla por xpath------------------------
    tabla = driver.find_element(
        "xpath", "/html/body/div[3]/div[2]/div[7]/table[1]")  # cuidado el div 7 o 6


    #busco elementos por clase--------------------------
    partidos = tabla.find_elements(By.CLASS_NAME, "odd")
    idUnico = 1
    resultados = []
    for partidoLeer in partidos:
        partido = partidoLeer.text
        posicionTercerEspacio = partido.index(" ", 7, 10)
        separado = partido.split("  ")

        if "pp." in partido:
            print("salta")
        elif ":" in partido:
            localNombre = separado[0]
            localNombre = localNombre[posicionTercerEspacio+1:]

            posicionH2h = separado[2].index("h2h")

            visitanteNombre = separado[2]
            visitanteNombre = visitanteNombre[:posicionH2h-1]

            fecha = separado[0]
            fecha = fecha[3:posicionTercerEspacio]
            separoFecha = fecha.split(" ")
            dia = separoFecha[0]
            mes = separoFecha[1]

            mesNumero = 0
            if "Jan" in mes:
                mesNumero = 1
            elif "Feb" in mes:
                mesNumero = 2
            elif "Mar" in mes:
                mesNumero = 3
            elif "Apr" in mes:
                mesNumero = 4
            elif "May" in mes:
                mesNumero = 5
            elif "Jun" in mes:
                mesNumero = 6
            elif "Jul" in mes:
                mesNumero = 7
            elif "Aug" in mes:
                mesNumero = 8
            elif "Sep" in mes:
                mesNumero = 9
            elif "Oct" in mes:
                mesNumero = 10
            elif "Nov" in mes:
                mesNumero = 11
            elif "Dec" in mes:
                mesNumero = 12

            salidaCorrecta = dia+"\t" + \
                str(mesNumero)+"\t"+localNombre+"\t"+visitanteNombre
            resultados.append(salidaCorrecta)

        else:
            localNombre = separado[0]
            localNombre = localNombre[posicionTercerEspacio+1:]

            try:
                posicionStats = separado[2].index("stats")
            except:
                posicionStats = len(separado[2])-5
            visitanteNombre = separado[2]
            visitanteNombre = visitanteNombre[:posicionStats-1]

            resultadoLocal = separado[1]
            resultadoLocal = resultadoLocal[0]
            resultadoVisitante = separado[1]
            resultadoVisitante = resultadoVisitante[4]

            salidaCorrecta = str(idUnico)+"\t"+localNombre+"\t" + \
                resultadoLocal+"\t"+resultadoVisitante+"\t"+visitanteNombre
            idUnico += 1
            resultados.append(salidaCorrecta)

    f = open("C:\\Users\\chema\\Desktop\\CARPETARAIZ\\apuestasNuevoInicio\\nuevosprogramas\\NUEVOSPROGRAMAS\\programaBasicoPorcentajes\\excel\\resultadosExcel\\" +
             nombres[posicionNombre], "w")
    for resultado in resultados:
        f.write(resultado+"\n")
        print(resultado)

    print(nombres[posicionNombre] +
          " finalizado con exito--------------------------------------------")
    posicionNombre += 1

    driver.quit()

