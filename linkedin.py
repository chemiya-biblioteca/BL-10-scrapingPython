from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

#
#-entrada de texto por xpath y buscar
#-buscar muchos elementos por class y extraer de cada uno el titulo por class 
#
#
#

#conectar con el webdriver----------------------------
driver_path="C:\\Users\\chema\\Desktop\\formacionPracticar\\AAcorreccionesGIT\\scraping\\chromedriver_win32\\chromedriver.exe"

driver=webdriver.Chrome(driver_path)



#buscar la pagina------------------------------
driver.get("https://es.linkedin.com/learning/?trk=learning-course_nav-header-logo&upsellOrderOrigin=default_guest_learning")



#buscar entrada de texto con xpath e introducir texto y buscar-----------------------------------
search=driver.find_element("xpath","/html/body/header/nav/section/section[3]/form/section/input")
search.send_keys("java")
search.send_keys(Keys.RETURN)




#buscar muchos elementos por nombre de clase-----------------------------------
principal=driver.find_elements(By.CLASS_NAME,"results-list__item")



#en cada elemento extraer titulo---------------------------------------
for i in principal:
    titulo=i.find_element(By.CLASS_NAME,"base-search-card__title")
    print(titulo.text)



driver.quit()