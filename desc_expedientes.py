from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def clamp(n, min):
    if n < min:
        return min
    elif n >= 1:
        return n
    else:
        return n
    

#funcion para revisar la carpta que contiene el listado de archivos    
def revisar_carpeta(driver, carpeta_container):
    sleep(0.5)
    en_revision_btn = carpeta_container.find_element(By.CLASS_NAME, 'collapsible-header')
    en_revision_btn.send_keys(Keys.RETURN) 

    #Busca entre los archivos cual se acomoda al criterio de busqueda
    criterio_busqueda = 'Reporte de Circulo de Crédito Cliente.'

    #seleccionar todos los elementos dentro de el menu desplegable
    documentos = carpeta_container.find_elements(By.CSS_SELECTOR, '.collapsible-document-item-table')
    if len(documentos) == 0:
        return False
    for documento in documentos:

        #Obtener el nombre de cada documento
        name = documento.find_element(By.CSS_SELECTOR, '.collapsible-title-document').text 

        #Revisar si alguno de los archivos tiene un nombre que coincida con el criterio de busqueda
        if criterio_busqueda in name:
            documento.click()

            #Abre el archivo
            sleep(1)
            try:
                boton_archivo = driver.find_element(By.CSS_SELECTOR, '.file-name-list')
            except:
                return
            boton_archivo.click()
            sleep(1)
            #obtain parent window handle
            p = driver.window_handles[0]
            #obtain browser tab window
            c = driver.window_handles[1]
            #switch to tab browser
            driver.switch_to.window(c)

            # print("Page title :")
            print(driver.title)
            sleep(0.5)
            #waves-effect light-blue darken-1 btn

            boton_archivo = driver.find_element(By.CSS_SELECTOR, 'a.dropdown-trigger.btn')
            boton_archivo.click()
            boton_descarga = driver.find_element(By.XPATH, '//*[@id="dropdown-download"]/li[2]/a')
            boton_descarga.click()
            #close browser tab window
            driver.close()
            #switch to parent window
            driver.switch_to.window(p)
            # print("Current page title:")
            # print(driver.title)
            return True

#carpeta para descargar archivos encontrados
def descargar_archivos(driver):

    #Scroll dentro de la carpeta del expediente
    for _ in range(15):
        webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

    #Acceder a la zona de archivos en revision
    en_revision_container = driver.find_element(By.CSS_SELECTOR, '#carpet-reviewing')
    carpet_state = en_revision_container.get_attribute('class')
    if carpet_state == 'disabled-item':
        print('no hay archivos listos para revision')
    else:
        if revisar_carpeta(driver, en_revision_container):
            print('Descarga exitosa')
            return
        print('checando en archivos validados')
        validos_container = driver.find_element(By.CSS_SELECTOR, '#carpet-valid')
        carpet_state = en_revision_container.get_attribute('class')
        if carpet_state == 'disabled-item':
            print('no hay archivos validados')
            return
        if revisar_carpeta(driver, validos_container):
            print('Descarga exitosa')
    



EMAIL = 'mailz@mail.com'
PASSWORD = 'mipass'

indice_actual = 0

url = 'https://sistema.expedienteazul.com/expedienteazul/login?language=es'

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver=webdriver.Chrome(options=options)
driver.get(url)

#Login en la pagina----
email_field = driver.find_element(By.CSS_SELECTOR, '#email')
password_field = driver.find_element(By.CSS_SELECTOR, '#password')
submit_btn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')

email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
submit_btn.click()


#rutina para buscar cada folio en el sistema

f = open("folios.txt", "r")
for folio in f:
    url2 = "https://sistema.expedienteazul.com/expedienteazul/folder/"+ folio +"/edit"
    driver.get(url2)
    print(folio)
    descargar_archivos(driver)
