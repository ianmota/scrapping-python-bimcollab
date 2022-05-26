from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests 
from errorScrapper.errorHandling import *

class ScrapperResearch():
    def __init__(self,login:str,senha:str,local_save:str,standardTime:int = 15):
        self.login = login
        self.password = senha
        self.localSave = local_save  
        self.standardTime = standardTime
    
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
                continue
            
            else:
                status = ResultStatus(6,f'Coletando incompatibilidade {i} de {len(issueList)}')
                print(status.statusGenerate())
                
                self.navegador.find_element_by_css_selector(f"#LabelIndex_{i}").click()
                html = bs(self.navegador.page_source, 'html.parser')
                self.htmlList.append(html)
                self.navegador.back()
                
            finally:
                self.navegador.quit()

class ScrapperColect():
    def __init__(self,htmlPage:ScrapperResearch):
        """Busca a nível baixo de informações em html

        Args:
            htmlPage (html): a busca acontece em uma página por vez
        """
        
        self.htmlList = htmlPage
    
    def __str__(self) -> str:
        return("database")
    
    def __repr__(self) -> str:
        return("DataBase")
    
    def coletar_numero(self)->list:
        numero=[]
        if(self.htmlList.find('div',attrs={'id':'LabelId'})):
            d = self.site.find('div',attrs={'id':'LabelId'}).text
            numero.append(d)
        return(numero)
        
    def coletar_descricao(self)->list:
        descricao = []

        if(self.site.find('span', attrs={"id":"LabelDescription"})):
            if(self.site.find('span',attrs={"id":"LabelDescription"}).text == '-'):
                self.navegador.back() 
            else:
                d = self.site.find("span",attrs={"id":"LabelDescription"}).text
                descricao.append(d)
        return(descricao)
                
    def coletar_titulo(self)->list:
        titulo = []

        if(self.site.find('span',attrs={'id':'LabelTopic'})):
            d = self.site.find('span',attrs={'id':'LabelTopic'}).text
            titulo.append(d)
        return(titulo)
    
    def coletar_prioridade(self)->list:
        prioridade = []

        if(self.site.find('span', attrs={'id':'LabelPriority'})):
            d = self.site.find('span', attrs={'id':'LabelPriority'})
            prioridade.append(d)
        return(prioridade)
    
    def coletar_responsavel(self)->list:
        responsavel = []

        if(self.site.find('span', attrs={'id':'LabelAssignTo'})):
            d = self.site.find('span', attrs={'id':'LabelAssignTo'}).text
            responsavel.append(d)
        return(responsavel)
    
    def coletar_tipo(self)->list:
        tipo = []

        if(self.site.find('span', attrs={'id':'LabelType'})):
            d = self.site.find('span', attrs={'id':'LabelType'}).text
            tipo.append(d)
        return(tipo)
    
    def coletar_area(self)->list:
        area = []

        if(self.site.find('span', attrs={'id':'LabelArea'})):
            d = self.site.find('span', attrs={'id':'LabelArea'}).text
            area.append(d)
        return(area)
    
    def coletar_data(self)->list:
        data = []

        if(self.site.find('span', attrs={'id':'LabelDeadline'})):
            d = self.site.find('span', attrs={'id':'LabelDeadline'}).text
            data.append(d)
        return(data)
            
    def coletar_etiqueta(self)->list:
        etiqueta = []

        if(self.site.find('span', attrs={'id':'LabelLabel'})):
            d = self.site.find('span', attrs={'id':'LabelLabel'}).text
            etiqueta.append(d)
        return(etiqueta)
    
    def coletar_milestone(self)->list:
        milestone = []

        if(self.site.find('span', attrs={'id':'LabelMilestone'})):
            d = self.site.find('span', attrs={'id':'LabelMilestone'}).text
            milestone.append(d)
        return(milestone)
    
    def coletar_status(self)->list:
        status = []

        if(self.site.find('span', attrs={'id':'LabelStatus'})):
            d = self.site.find('span', attrs={'id':'LabelStatus'}).text
            status.append(d)
        return(status)
    
    def coletar_empreendimento(self)->list:
        empreendimento = []

        if(self.site.find('span', attrs={'id':'LabelCurrentProject'})):
            d = self.site.find('span', attrs={'id':'LabelCurrentProject'}).text
            empreendimento.append(d)
        return(empreendimento)
    
    def coletar_comentarios_imagens(self)->list:
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
        


