from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests 
from backend.scrapper.errorScrapper.errorHandling import *

class ScrapperResearch():
    def __init__(self,login:str,senha:str,standardTime:int = 15):
        self.login = login
        self.password = senha
        self.standardTime = standardTime
        
        self.statusColeta = ""
    def __str__(self) -> str:
        return("html_resource")
    
    def __repr__(self) -> str:
        return(f"html({len(self.htmlList)})")
    
    def openResearch(self)->webdriver:
        """abrir navegador
        Returns:
            webdriver: site
        """
        conf = Options()
        conf.add_argument('--headless')
        self.navegador = webdriver.Chrome(options=conf)
        self.navegador.get("https://join.bimcollab.com/WebApp/Account/Login.aspx") 
    
    def addLogin(self)->None:
        """
        adicionar login
        """
        
        try:
            Navigator(self.navegador,self.standardTime,"email").exceptionsID()
            
        except:
            status = ResultStatus(0,'Falha na inserção do email')
            print(status.statusGenerate())
            self.navegador.refresh()
            
        else:
            self.navegador.find_element_by_id("email").send_keys(self.login)
            self.navegador.find_element_by_css_selector("#login").click() 
            status = ResultStatus(0,'Realizando Login, email adicionado')
            print(status.statusGenerate())
            
    def addSenha(self)->None:
        """
        adicionar senha 
        """
        
        try:
            Navigator(self.navegador,self.standardTime,"password").exceptionsID()
            
        except: 
            print(ResultStatus(1,'Falha na inserção da senha').statusGenerate())
            self.navegador.refresh()
        
        else:
            self.navegador.find_element_by_id("password").send_keys(self.password)
            self.navegador.find_element_by_css_selector("#loginWithPassword").click() 
            status = ResultStatus(1,'Realizando login, senha adicionada')
            print(status.statusGenerate())  
            
    def addCompany(self)->None:
        """
        adicionar companhia
        """
        try: 
            Navigator(self.navegador,self.standardTime,"saveCompanyInfo").exceptionsID()
        
        except:
            status = ResultStatus(2,'Falha na inserção da companhia')
            print(status.statusGenerate())
            self.navegador.refresh()
            
        else:
            self.navegador.find_element_by_id("saveCompanyInfo").click()
            print(ResultStatus(2,'Companhia adicionada').statusGenerate())
            
    def selectProject(self)->None:
        """
        selecionar o projeto ativo
        """
        try:
            standby = Navigator(self.navegador,self.standardTime,"#ProjectImage")
            standby.exceptionsCSSselector()
        
        except:
            status = ResultStatus(3,'Falha na seleção do projeto')
            print(status.statusGenerate())
            self.navegador.refresh()
            
        else:
            self.navegador.find_element_by_css_selector('#ProjectImage').click()
            print(ResultStatus(3,'Projeto selecionado').statusGenerate())
            
    def goToIssues(self)->None:
        """
        navegar para as incompatibilidades
        """
        try:
            standby = Navigator(self.navegador,self.standardTime,"#HyperLinkIssue")
            standby.exceptionsCSSselector()
        
        except:
            status = ResultStatus(4,'Falha na seleção da área das incompatibilidades')
            print(status.statusGenerate())
            self.navegador.refresh()
            
        else:
            self.navegador.find_element_by_css_selector('#HyperLinkIssue').click()
            print(ResultStatus(4,'Área das incompatibilidades').statusGenerate())

    def openAll(self)->None:
        """
        abrir todas as incompatibilidades
        """
        try:
            standby = Navigator(self.navegador,self.standardTime,"LinkButtonAll")
            standby.exceptionsID()
        
        except:
            status = ResultStatus(5,'Falha na abertura de todos os dados')
            print(status.statusGenerate())
            self.navegador.refresh()
            
        else:
            self.navegador.find_element_by_id("LinkButtonAll").click()
            print(ResultStatus(5,'Todos os dados abertos').statusGenerate())
            
    def htmlGenerator(self)->list:
        """
        Gera uma lista com todos os htmls das incompatibilidades

        Returns:
            list: html das incompatibilidades
        """
        self.htmlList = []
        issueList = self.navegador.find_elements_by_css_selector(".gridViewRow > .colTitle")
        
        for i in range(len(issueList)):
            try:
                standby = Navigator(self.navegador,self.standardTime,f"#LabelIndex_{i}")
                standby.exceptionsCSSselector()
                
            except:
                status = ResultStatus(6,f'Falha na coleta da incompatibilidade {i}')
                print(status.statusGenerate())
                self.navegador.refresh()
                self.statusColeta = f"INCOMPATIBILIDADE {i+1} DE {len(issueList)} --> ERRO!"
                continue
            
            else:
                status = ResultStatus(6,f'Coletando incompatibilidade {i} de {len(issueList)}')
                print(status.statusGenerate())
                
                self.navegador.find_element_by_css_selector(f"#LabelIndex_{i}").click()
                html = bs(self.navegador.page_source, 'html.parser')
                self.htmlList.append(html)
                self.navegador.back()
                self.statusColeta = f"INCOMPATIBILIDADE {i+1} DE {len(issueList)} --> OK"
            

class ScrapperColect():
    def __init__(self,htmlPage:bs):
        """Busca a nível baixo de informações em html

        Args:
            htmlPage (html): a busca acontece em uma página por vez
        """
        
        self.htmlList = htmlPage
    
    def __str__(self) -> str:
        return("Colect data")
    
    def __repr__(self) -> str:
        return("Colect()")
    
    def numberColect(self)->int:
        """coleta o número de todas as incompatibilidades

        Returns:
            int: 3
        """
        number = self.htmlList.find('span',attrs={'id':'LabelId'}).text
        status = ResultStatus(11,f'Número {number} coletado').statusGenerate()
        print(status)
        return(number)   
        
    def statusColect(self)->str:
        """Coletar o status do dado

        Returns:
            str: fechado/aberto
        """

        try:
            self.htmlList.find('span', attrs={'id':'LabelStatus'}).text

        except:
            resultSatus = ResultStatus(12,'Não foi possível coletar o status')
            print(resultSatus.statusGenerate())
            pass
        
        else:
            status = self.htmlList.find('span', attrs={'id':'LabelStatus'}).text
            resultSatus = ResultStatus(12,'Status coletado')
            print(resultSatus.statusGenerate())
            
            return(status)
    
    def titleColect(self)->str:
        """Coleta o titulo do dado

        Returns:
            str: 0000-nome
        """
        try:
            self.htmlList.find('span',attrs={'id':'LabelTopic'}).text
            
        except:
            statusResult = ResultStatus(13,'Não foi possível coletar o título')
            print(statusResult.statusGenerate())
        
        else:
            title = self.htmlList.find('span',attrs={'id':'LabelTopic'}).text
            statusResult = ResultStatus(13,'Título coletado')
            print(statusResult.statusGenerate())
            
            return(title)
    
    def buildColect(self)->str:
        """
        Coleta o empreendimento

        Returns:
            str: Max trindade
        """
        try:
            self.htmlList.find('span', attrs={'id':'LabelCurrentProject'}).text
        
        except:
            statusResult = ResultStatus(14, 'Não foi possível coletar o empreendimento')
            print(statusResult.statusGenerate())
            pass
        
        else:
            build = self.htmlList.find('span', attrs={'id':'LabelCurrentProject'}).text
            statusResult = ResultStatus(14, 'Empreendimento coletado')
            print(statusResult.statusGenerate())
            
            return(build)
    
    def descriptionColect(self)->str:
        """
        Coleta a descrição do empreendimento

        Returns:
            str: 0000-Tubulação
        """
        try:
            self.htmlList.find("span",attrs={"id":"LabelDescription"}).text
        
        except:
            statusResult = ResultStatus(15, 'Não foi possível coletar a descrição')
            print(statusResult.statusGenerate())
            pass
        
        else:
            description = self.htmlList.find("span",attrs={"id":"LabelDescription"}).text
            statusResult = ResultStatus(15, 'Descrição coletada')
            print(statusResult.statusGenerate())
            
            return(description)
    
    def labelColect(self)->str:
        """
        Coleta as disciplinas do problema

        Returns:
            str: Arquitetura, Estrutura
        """
        
        try:
            self.htmlList.find('span', attrs={'id':'LabelLabel'}).text
        
        except:
            statusResult = ResultStatus(16, 'Não foi possível coletar a etiqueta')
            print(statusResult.statusGenerate())
            pass
        
        else:
            label = self.htmlList.find('span', attrs={'id':'LabelLabel'}).text
            statusResult = ResultStatus(16, 'Etiqueta coletada')
            print(statusResult.statusGenerate())
            
            return(label)

    def assingToColect(self)->str:
        """
        Coletar o responsável pela incompatibilidade

        Returns:
            str: João
        """
        try:
            self.htmlList.find('span', attrs={'id':'LabelAssignTo'}).text
        
        except:
            statusResult = ResultStatus(17, 'Não foi possível coletar o responsável')
            print(statusResult.statusGenerate())
            pass
        
        else:
            assingTo = self.htmlList.find('span', attrs={'id':'LabelAssignTo'}).text
            statusResult = ResultStatus(17, 'Responsável coletado')
            print(statusResult.statusGenerate())
            
            return(assingTo)
        
    def milestoneColect(self)->str:
        """
        Coleta a fase

        Returns:
            str: Construção virtual 02
        """
        try:
            self.htmlList.find('span', attrs={'id':'LabelMilestone'}).text
        
        except:
            statusResult = ResultStatus(18, 'Não foi possível coletar a fase')
            print(statusResult.statusGenerate())
            pass
        
        else:
            milestone = self.htmlList.find('span', attrs={'id':'LabelMilestone'}).text
            statusResult = ResultStatus(18, 'Fase coletada')
            print(statusResult.statusGenerate()) 

            return(milestone)
    
    def typeColect(self)->str:
        """
        Coleta o tipo da incompatibilidade

        Returns:
            str: Otimização
        """
        try:
            self.htmlList.find('span', attrs={'id':'LabelType'}).text
        
        except:
            statusResult = ResultStatus(19, 'Não foi possível coletar o tipo')
            print(statusResult.statusGenerate())
            pass
        
        else:
            dataType = self.htmlList.find('span', attrs={'id':'LabelType'}).text
            statusResult = ResultStatus(19, 'Tipo coletado')
            print(statusResult.statusGenerate()) 

            return(dataType)
    
    def areaColect(self)->str:
        """
        Coleta a área do problema

        Returns:
            str: Pavimento coberta
        """
        try:
            self.htmlList.find('span', attrs={'id':'LabelArea'}).text
        
        except:
            statusResult = ResultStatus(20, 'Não foi possível coletar a localização')
            print(statusResult.statusGenerate())
            pass
        
        else:
            area = self.htmlList.find('span', attrs={'id':'LabelArea'}).text
            statusResult = ResultStatus(20, 'Localização coletada')
            print(statusResult.statusGenerate()) 

            return(area)

    def deadlineColect(self)->str:
        """
        Coleta o prazo de resposta do projetista

        Returns:
            str: 26-04-2000
        """
        try:
            self.htmlList.find('span', attrs={'id':'LabelDeadline'}).text
        
        except:
            statusResult = ResultStatus(21, 'Não foi possível coletar o prazo')
            print(statusResult.statusGenerate())
            pass
        
        else:
            deadline = self.htmlList.find('span', attrs={'id':'LabelDeadline'}).text
            statusResult = ResultStatus(21, 'Prazo coletado')
            print(statusResult.statusGenerate()) 

            return(deadline)

    def priorityColect(self)->str:
        """
        Coleta a prioridade de cada problema

        Returns:
            str: Crítico
        """
        
        try:
            self.htmlList.find('span', attrs={'id':'LabelPriority'}).text
        
        except:
            statusResult = ResultStatus(22, 'Não foi possível coletar a prioridade')
            print(statusResult.statusGenerate())
            pass
        
        else:
            priority = self.htmlList.find('span', attrs={'id':'LabelPriority'}).text
            statusResult = ResultStatus(22, 'Prioridade coletada')
            print(statusResult.statusGenerate()) 

            return(priority)
    
    def lastModificationColect(self)->str:
        """
        Coleta a última data e hora de modificação

        Returns:
            str: 26-04-200 19:00
        """
        try:
            self.htmlList.find('div', attrs={'id':'PanelCommentList'})
        
        except:
            statusResult = ResultStatus(23, 'Não foi possível coletar a última modificação')
            print(statusResult.statusGenerate())
            pass
        
        else:
            lastModification = self.htmlList.find('div', attrs={'id':'PanelCommentList'})
            lastModification = lastModification.find('div', attrs={'class':"onerow commentTitle innerPaddingComment"})
            statusResult = ResultStatus(23, 'Última modificação coletada')
            print(statusResult.statusGenerate()) 

            return(lastModification.find('p').text)
    
    def firstModificationColect(self)->str:
        """Coleta a primeira data e hora de modificação

        Returns:
            str: 26-04-200 19:00
        """
        try:    
            self.htmlList.find('div', attrs={'id':'PanelCommentList'})
        
        except:
            statusResult = ResultStatus(23, 'Não foi possível coletar a primeira modificação')
            print(statusResult.statusGenerate())
            pass
        
        else:
            firstModification = self.htmlList.find('div', attrs={'id':'PanelCommentList'})
            firstModification = firstModification.find_all('div', attrs={'class':"onerow commentTitle innerPaddingComment"})
            statusResult = ResultStatus(23, 'Última modificação coletada')
            print(statusResult.statusGenerate()) 
            return(firstModification[-1].find('p').text)
    
    def dictionaryGeneration(self)->dict:
        """Gera um dicionário com todas as informações coletadas

        Returns:
            dict: informações coletadas
        """
        dataDictionary = {
            "ID":self.numberColect(),
            "Título": self.titleColect(),
            "Status": self.statusColect(),
            "Empreendimento": self.buildColect(),
            "Descrição":self.descriptionColect(),
            "Etiqueta": self.labelColect(),
            "Responsável": self.assingToColect(),
            "Fase": self.milestoneColect(),
            "Tipo":self.typeColect(),
            "Local": self.areaColect(),
            "Prazo": self.deadlineColect(),
            "Prioridade": self.priorityColect(),
            "Última modificação": self.lastModificationColect(),
            "Primeira alteração": self.firstModificationColect()
            
        }
        return(dataDictionary)
    
    def coletar_comentarios_imagens(self)->list:
        """
        Não usar, ainda está sendo desenvolvida

        Returns:
            list: ERRO!
        """
        comentario = []
        imagem = []
        elementos = self.site.find_all("div",attrs={"class":"onerow commentContent innerPaddingComment"})
        for i in range(len(elementos)):
            d = self.site.find_all("div",attrs={"class":"onerow commentContent innerPaddingComment"})[i]
            comentario.append(d)

            issueimg = self.site.find_all('a',attrs={"class":"viewpointIssueImgLink previewLeft"})
            for i in issueimg:

                issuelink = i["href"]
                imagem.append(issuelink[-12:])
                f = open(f"{self.local_save}/{issuelink[-12:]}.png","wb")
                f.write(requests.get(f"https://join.bimcollab.com{issuelink}").content)
                f.close() 
            return([comentario,imagem])
        


