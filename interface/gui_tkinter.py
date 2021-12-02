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
        self.root.title("Relatório generator")
        self.root.configure(background='#4F4F4F')
        self.root.geometry('788x588')
        self.root.resizable(True,True)
        self.root.maxsize(width=1000,height=1000)
        self.root.minsize(width=788,height=588)       
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=20, bg="#000000",
            background="#DCDCDC")
        self.frame_1.place(relx=0.05,rely=0.05,relwidth=0.9,
            relheight=0.9)   
    def widgets_da_tela(self):



        #* Confirmar
        self.bt_confirmar = Button(self.frame_1, 
            text="Confirmar", bd=3, font= ('verdana',12,'bold'))
        self.bt_confirmar.place(relx=0.35, rely=0.9,
            relheight=0.1,relwidth=0.2)

        #* Cancelar
        self.bt_cancelar = Button(self.frame_1, 
            text="Cancelar", bd=3, font= ('verdana',12,'bold'))
        self.bt_cancelar.place(relx=0.55, rely=0.9,
            relheight=0.1,relwidth=0.2)

        #* Usuário
        self.lb_usuario = Label(self.frame_1, 
            text="Usuário", font=('verdana',12,'bold'))
        self.lb_usuario.place(relx=0.45,rely=0,
            relwidth=0.1)
        self.usuario_entry = Entry(self.frame_1,
            font=('verdana',12))
        self.usuario_entry.place(relx=0,rely=0.05,
        relwidth=1, )

        #* Senha
        self.lb_senha = Label(self.frame_1, 
            text="Senha", font=('verdana',12,'bold'))
        self.lb_senha.place(relx=0.45,rely=0.1,
            relwidth=0.1)
        self.senha_entry = Entry(self.frame_1,
            font=('verdana',12))
        self.senha_entry.place(relx=0,rely=0.15,
        relwidth=1)
            
Application()


