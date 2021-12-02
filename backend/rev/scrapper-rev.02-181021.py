"""
! Código destinado para webscrapping no Bim Collab 
"""

#* Importações
from bs4 import BeautifulSoup as bs 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
from openpyxl import load_workbook
import requests

#* Informações
longinurl = ('https://join.bimcollab.com/WebApp/Account/Login.aspx')
login='maxtrindade@projete5d.com.br'
password= '@timeprojete5d'

#*Navegador
conf = Options()
conf.add_argument('--headless')
navegador = webdriver.Chrome(options=conf)
navegador.get(longinurl)

#* Movimentação no sistema
navegador.find_element_by_id('UserName').send_keys(login)
navegador.find_element_by_id('Password').send_keys(password)
navegador.find_element_by_css_selector('#LoginButton').click()
sleep(2)
selecionar_projeto = navegador.find_element_by_css_selector('#ProjectImage').click()
selecionar_issue = navegador.find_element_by_css_selector('#HyperLinkIssue').click()

c=0
descricao = []
titulos = []
prioridades = []
imagens = []
d = ''

a = navegador.find_elements_by_css_selector('.gridViewRow > .colTitle')
navegador.find_element_by_css_selector('.gridViewRow > .colTitle').click()
for i in range(len(a)-1):

    site = bs(navegador.page_source, 'html.parser')

    u = site.find_all('div',attrs={'class':'onerow commentContent innerPaddingComment'})
    for i in range(len(u)):
        desc = site.find_all('div',attrs={'class':'onerow commentContent innerPaddingComment'})[i]
        d = desc.p.text +'\n'+ d  
        
    descricao.append(d)    
    d = ''

    titulo = site.find('span',attrs={'id':'LabelDescription'})
    prioridade = site.find('span', attrs={'id':'LabelPriority'})

    titulos.append(titulo.text)
    prioridades.append(prioridade.text)
    sleep(2)

    imagem = site.find('div',attrs={'class':'thumbnailImageFrame backgroundWhite'})
    a =imagem['style'] 
    imagens.append('https://join.bimcollab.com/' + a[21:-5])

    nome = 'dados/'+ str(i) +'.jpg'
    f = open(nome,'wb')
    response = requests.get('https://join.bimcollab.com/' + a[21:-5])
    f.write(response.content)
    f.close

    navegador.find_element_by_css_selector('#HyperLinkNext').click()

    c += 1
    if c == 2:
        break

dados = {'Título':titulos,'Prioridade':prioridades,'Descrição':descricao,'Imagens':imagens}
dados_pandas = pd.DataFrame(dados)
dados_pandas.to_excel('dados/max_trindade.xlsx',index=False)
navegador.close() 

print('\n\n\n Finalizado!')

