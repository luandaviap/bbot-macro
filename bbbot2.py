from selenium import webdriver
from time import sleep

login_globo  = 'email@email.com'
senha_globo  = 'senha12345'
id_login     = 'login'
id_password  = 'password'

votos_cont = 0

chrome_path = r"C:\Users\R3br34K\Desktop\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.implicitly_wait(10)

def login_gshow():

    driver.get("https://login.globo.com/login/4728?tam=widget&url=https%3A%2F%2Fintervencao.globo.com%2Fintervencoes%2Fshow.do%3Fpopin%3Dtrue%26servicoId%3D4728%26urlIntervencao%3Dhttps%3A%2F%2Fs.glbimg.com%2Fgl%2Fba%2Fbarra-globocom.callback.html%2523https%253A%252F%252Fgshow.globo.com%252F")
    input_login = driver.find_element_by_id(id_login)
    input_password = driver.find_element_by_id(id_password)
    input_login.send_keys(login_globo)
    input_password.send_keys(senha_globo)
    sleep(2)
    driver.find_element_by_xpath("""/html/body/div[1]/main/div[2]/div/div/div/div[2]/div[1]/form/div[6]/button""").click()
login_gshow()

def votar_na_manu():

    driver.get("https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml")
    driver.find_element_by_xpath("""/html/body/div[2]/div[4]/div/div[1]/div[4]/div[2]/div""").click() #Clica no Participante
    sleep(2)
    driver.find_element_by_xpath("""/html/body/div[2]/div[4]/div/div[1]/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/img""").click() #Clica no Captcha pela 1Âº vez
    sleep(4.5) #Altere o tempo em segundos de acordo com a demora de processar o voto!
    driver.find_element_by_xpath("""/html/body/div[2]/div[4]/div/div[1]/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/img""").click() #Clica no Captcha pela 2Âº vez
    sleep(5) #Altere o tempo em segundos de acordo com a demora de processar o voto!

while(True):
    votar_na_manu()
    votos_cont = votos_cont + 1
    print("{} votos foram testados".format(votos_cont))
