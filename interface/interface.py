from tkinter import *
from tkinter import filedialog
from threading import *
from backend.scrapper.scrapper import ScrapperColect, ScrapperResearch
import base64
from data.dataSave import *
from os.path import realpath

class Application(ScrapperResearch,ScrapperColect):
    
    def __init__(self):
        self.root = Tk()
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
 
        with open(realpath("icons\Projete5D140x140png.png"), "rb") as image_file:
            image64 = base64.b64encode(image_file.read())
        self.logoP5D = PhotoImage(data=image64)
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
