from tkinter import *

root = Tk()
class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_da_tela()
        root.mainloop()
    def tela(self):
        self.root.title("Gerador de relatório")
        self.root.configure(background='#DAA520')
        self.root.geometry('500x500')
        self.root.resizable(False,False)
        #self.root.maxsize(width=1000,height=1000)
        #self.root.minsize(width=300,height=500)       
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=20, bg="#000000",
            background="#778899")
        self.frame_1.place(relx=0.1,rely=0.1,relwidth=0.8,
            relheight=0.4)   
    def widgets_da_tela(self):
        #* Confirmar
        self.bt_confirmar = Button(self.frame_1, 
            text="Confirmar", bd=3, font= ('verdana',11,'bold'))
        self.bt_confirmar.place(relx=0.4, rely=0.9,relwidth=0.3)

        #* Usuário
        self.lb_usuario = Label(self.frame_1, 
            text="Usuário", font=('verdana',11,'bold'))
        self.lb_usuario.place(relx=0,rely=0.05,
            relwidth=0.2)
        self.usuario_entry = Entry(self.frame_1,
            font=('verdana',11))
        self.usuario_entry.place(relx=0.21,rely=0.05,
        relwidth=0.8 )

        #* Senha
        self.lb_senha = Label(self.frame_1, 
            text="Senha", font=('verdana',11,'bold'))
        self.lb_senha.place(relx=0,rely=0.22,
            relwidth=0.2)
        self.senha_entry = Entry(self.frame_1,
            font=('verdana',11))
        self.senha_entry.place(relx=0.21,rely=0.22,
        relwidth=0.8)
            
        #* Issues
        self.lb_issues = Label(self.frame_1, 
            text="Issues", font=('verdana',11,'bold'))
        self.lb_issues.place(relx=0,rely=0.38,
            relwidth=0.2)
        self.issues_entry = Entry(self.frame_1,
            font=('verdana',11))
        self.issues_entry.place(relx=0.21,rely=0.38,
        relwidth=0.8)

Application()


