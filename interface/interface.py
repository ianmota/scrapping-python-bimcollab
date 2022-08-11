from tkinter import *
from tkinter import filedialog
from threading import *
from backend.scrapper.scrapper import ScrapperColect, ScrapperResearch
import base64
from data.dataSave import *
from os.path import abspath

class Application(ScrapperResearch,ScrapperColect):
    
    def __init__(self):
        self.root = Tk()
        self.Imagens()
        self.Root01()
        self.Root01Labels()
        self.Root01Button()
        self.Root01Entry()
        self.root.mainloop()
        
    def Root01(self):
        self.root.title("Tabela de incompatibilidades")
        self.root.configure(background='#71A67a')
        self.root.geometry('400x300')
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW", self._close)
 
        self.logoP5D = PhotoImage(data=base64.b64decode(self.logo))
        self.root.iconphoto(False,self.logoP5D)
            
    def Root01Labels(self):
        lb_width = 0.4
        self.lb_usuario = Label(self.root, text="Usuário", font=('verdana',11,'bold'),justify='center')
        self.lb_usuario.place(relx=0.01,rely=0.5,relwidth=lb_width)
        
        self.lb_senha = Label(self.root, text="Senha", font=('verdana',11,'bold'))
        self.lb_senha.place(relx=0.01,rely=0.6,relwidth=lb_width)
        
        self.lb_local = Label(self.root, text="Local", font=('verdana',11,'bold'))
        self.lb_local.place(relx=0.01,rely=0.7,relwidth=lb_width)
        
        textoImpacto = 'Se você não tem dúvida \n é porque está mal informado'
        self.lb_fraseImpacto = Label(self.root, text=textoImpacto, font=('verdana',11,'bold'), bg='#71A67a')
        self.lb_fraseImpacto.place(relx=0.38, rely=0.2)
        
        self.fr_logoP5D = Label(self.root, image= self.logoP5D)
        self.fr_logoP5D.place(relx=0.02,rely=0.02,relheight=0.45,relwidth=0.35)

    def Root01Entry(self):
        en_width = 0.55
        self.en_usuario = Entry(self.root,font=('verdana',10))
        self.en_usuario.place(relx=0.43,rely=0.5,relwidth=en_width, )

        self.en_senha = Entry(self.root,font=('verdana',10),show='*')
        self.en_senha.place(relx=0.43,rely=0.6,relwidth=en_width)
        
    def Root01Button(self):    
        self.bt_confirmar = Button(self.root, text="Confirmar", font= ('verdana',11,'bold'),command=self._th_get_html)
        self.bt_confirmar.place(relx=0.4, rely=0.85)
        
        self.bt_localSave = Button(self.root, font= ('verdana',11,'bold'), justify='center',command=self._get_folder,text="Local")
        self.bt_localSave.place(relx=0.43, rely=0.7, relwidth=0.55, height=26)

    def _th_get_html(self):
        self.t1 = Thread(target=self._get_html)
        self.t1.start()
        
    def _close(self):
        try:
            self.t1.join()
        except AttributeError:
            pass
            
        self.root.destroy()
        
    def _get_html(self):
        
        email = str(self.en_usuario.get())
        password = str(self.en_senha.get())

        
        self.lb_fraseImpacto["text"] = 'Abrindo servidor'
        self.lb_fraseImpacto["font"] = ('verdana',9)
        self.lb_fraseImpacto["fg"] = '#008000'
        
        self.browser = ScrapperResearch(email,password)
        try:
            self.browser.openResearch()
            self.browser.addLogin()
            self.browser.addSenha()
            self.browser.addCompany()
            self.browser.selectProject()
            self.browser.goToIssues()
            self.browser.openAll()
        except:   
            self.lb_fraseImpacto["text"] = 'Falha na abertura'
            self.lb_fraseImpacto["font"] = ('verdana',9)
        else:
            self.lb_fraseImpacto["text"] = 'Coletando dados, aguarde. Esta \
                \n  operação costuma demorar \n 10 minutos'
            self.lb_fraseImpacto["font"] = ('verdana',9)
            self.lb_fraseImpacto["fg"] = '#008000'
        
        try:
            self.browser.htmlGenerator()
            
        except:
            self.lb_fraseImpacto["text"] = 'Não foi possível coletar\
                \n os dados. ERRO!'
            self.lb_fraseImpacto["font"] = ('verdana',9)
            
        else:
            self.lb_fraseImpacto["text"] = 'Dados coletados, construindo\
                \n o banco de dados bruto'
            self.lb_fraseImpacto["font"] = ('verdana',9)
            self.lb_fraseImpacto["fg"] = '#008000'
        
        

        self._create_dictionary()
        
    def _get_folder(self):
        self.en_localSalve = filedialog.askdirectory()
    
    def _create_dictionary(self):
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

            
        self.dicionario = {}
        for i in self.browser.htmlList:
            coleta = ScrapperColect(i)
            dicBase = coleta.dictionaryGeneration()
            
            id.append(dicBase.get("ID"))
            titulo.append(dicBase.get("Título"))    
            status.append(dicBase.get("Status")) 
            descricao.append(dicBase.get("Descrição")) 
            empreendimento.append(dicBase.get("Empreendimento"))
            etiqueta.append(dicBase.get("Etiqueta"))
            responsavel.append(dicBase.get("Responsável"))
            fase.append(dicBase.get("Fase"))
            tipo.append(dicBase.get("Tipo"))
            area.append(dicBase.get("Local"))
            prazo.append(dicBase.get("Prazo"))
            prioridade.append(dicBase.get("Prioridade"))
            ultimaAlteracao.append(dicBase.get("Última modificação"))
            primeiraAlteracao.append(dicBase.get("Primeira alteração"))
            
            
        self.dicionario["ID"] = id
        self.dicionario["Título"] = titulo
        self.dicionario["Status"] = status
        self.dicionario["Descrição"] = descricao
        self.dicionario["Empreendimento"] = empreendimento
        self.dicionario["Etiqueta"] = etiqueta
        self.dicionario["Responsável"] = responsavel
        self.dicionario["Fase"] = fase
        self.dicionario["Tipo"] = tipo
        self.dicionario["Local"] = area
        self.dicionario["Prazo"] = prazo
        self.dicionario["Prioridade"] = prioridade
        self.dicionario["Última alteração"] = ultimaAlteracao
        self.dicionario["Primeira alteração"] = primeiraAlteracao
        
        self._save()
        
    def _save(self):
        nomeEmail = self.en_usuario.get()
        nomeArquivo = nomeEmail.split('@')
        
        dbBuildCSV(self.dicionario,f'{self.en_localSalve}/{nomeArquivo[0]}.csv')

    def Imagens(self):
        self.logo = "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"