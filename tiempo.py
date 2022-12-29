
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys


#-acepto boton de las cookies
#-entrada de texto introduzco valor
#-por xpath doy a buscar
#-selecciono pestaña de horas
#-cojo valor del viento



#conecto con el webdriver----------------------------
driver_path="C:\\Users\\chema\\Desktop\\formacionPracticar\\python\\scraping\\chromedriver_win32\\chromedriver.exe"

driver=webdriver.Chrome(driver_path)# las opciones no son necesarias

driver.get("https://www.eltiempo.es/")




#acepto el boton de las cookies---------------------------------
#inspeccionar, boton derecho sonbre el html, copy full xpath
cookies = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div/div/div[3]/button[2]")
cookies.click()




#entrada de texto introduzco valor--------------------------
entrada = driver.find_element(By.ID, "term")
entrada.send_keys("madrid")

time.sleep(3)


#por xpath doy click para buscar-----------------------------------------
madrid = driver.find_element("xpath", "/html/body/div[5]/header/div[3]/section/div[2]/div/div[1]/div/ul/li[1]/a")
madrid.click()


time.sleep(7)



#por selector selecciono pestaña de horas---------------------------------
horas = driver.find_element(By.CSS_SELECTOR, "#cityTable > div > article > section > ul:nth-child(1) > li:nth-child(2) > h2 > a")
horas.click()



#cojo valores del viento por clase-----------------------------------
viento = driver.find_elements(By.CLASS_NAME, "m_table_weather_hour_wind")

for i in viento:
    print(i.text)

driver.quit()



									