from backend.scrapper.scrapper import ScrapperResearch, ScrapperColect
from data.DataBaseConstruction import Database

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

for i in browser.htmlList:
    coleta = ScrapperColect(i)
    
    id.append(coleta.numberColect())
    titulo.append(coleta.titleColect())
    status.append(coleta.statusColect())
    descricao.append(coleta.descriptionColect())
    empreendimento.append(coleta.buildColect())
    etiqueta.append(coleta.labelColect())
    responsavel.append(coleta.assingToColect())
    fase.append(coleta.milestoneColect())
    tipo.append(coleta.typeColect())
    area.append(coleta.areaColect())
    prazo.append(coleta.deadlineColect())
    prioridade.append(coleta.priorityColect())
    ultimaAlteracao.append(coleta.lastModificationColect())
    
banco = Database(id=id, title=titulo,status=status, build=empreendimento, description=descricao, label=etiqueta,assingTo=responsavel,milestone=fase,dataType=tipo,area=area,deadline=prazo,priority=prioridade,lastModification=ultimaAlteracao)

dicionario = banco.dictionaryGeneration()
print(dicionario)
    
dataframe = banco.dbBuild()
print(dataframe)
    
    
    
