from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

folios_exp = [""]

username = "tu correo de latin cupid"
password = "contraseña"


#SET WEBDRIVER
options = Options()
options.binary_location = "AppData\Local\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox("executable_path=\geckodriver.exe", options=options)


# Abrimos la página con get del driver
webdriver.get("https://sistema.expedienteazul.com/expedienteazul/login")
    

email ="myemail@email.com"
password= "mypassword1@23"
email_textfield = driver.find_element_by_name("email")
password_textfield = driver.find_element_by_name("password")
login_button = driver.find_element_by_name("btn btn-primary")


print (email_textfield)
print (password_textfield) 
