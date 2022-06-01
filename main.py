from backend.scrapper.scrapper import ScrapperResearch, ScrapperColect
from data.dataSave import dbBuildAnalysys

email = "oscarfreire@projete5d.com.br"
password = "@Timeprojete5d"
local_save = "data"

browser = ScrapperResearch(email,password,local_save)

browser.openResearch()
browser.addLogin()
browser.addSenha()
browser.addCompany()
browser.selectProject()
browser.goToIssues()
browser.openAll()
browser.htmlGenerator()

id = []
titulo = []
status = []
descricao = []
empreendimento = []
etiqueta = []
responsavel = []
fase = []
tipo = []
area = []
prazo = []
prioridade =[]
ultimaAlteracao = []
primeiraAlteracao = []

for i in browser.htmlList:
    coleta = ScrapperColect(i)
    
    dicionario = coleta.dictionaryGeneration()
    
dataframe = dbBuildAnalysys(dicionario)
    
    
    
