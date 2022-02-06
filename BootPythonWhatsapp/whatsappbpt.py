#importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
time.sleep(20)
#Defionir contatos ou grupos e mensagem a ser enviada
contatos = [#'NomeDoContato']
mensagem = #"MensagemQueDesejaEnviar"
#Buscar o destinario
def buscarContato(contato):
   campoPesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
   time.sleep(3)
   campoPesquisa.click()
   campoPesquisa.send_keys(contato)
   campoPesquisa.send_keys(Keys.ENTER)

def enviarMensagem(mensagem):
   campoMensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
   campoMensagem[1].click()
   time.sleep(3)
   campoMensagem[1].send_keys(mensagem)
   campoMensagem[1].send_keys(Keys.ENTER)




for contato in contatos:
    buscarContato(contato)
    enviarMensagem(mensagem)
#Campo de pesquisa "copyable-text selectable-text"
#Campo de mensagem "copyable-text selectable-text"
#Enviar mensagens