from scrapper import Scrapper_collect
login = "oscarfreire@projete5d.com.br"
senha = "@Timeprojete5d"
filtro = 1
ordem = 0
incompatibilidades = "35-38"
local_save = "data"

navegador = Scrapper_collect(login,senha,filtro,ordem,incompatibilidades,local_save)
navegador.abrir_navegador()


navegador.add_login()
    
navegador.add_senha()
navegador.add_company()
navegador.select_project()
navegador.go_to_issues()
navegador.filtro()
#navegador.ordem() colocar na hora de salvar
navegador.coletar_dados()
print(navegador.coletar_dados( ))

"""
self.VerificadorEmail = True
self.VerificadorSenha = False
self.VerificadorCompany = False
self.VerificadorProjeto = False
self.VerificadorIssues = False
self.VerificadorFiltro = False   
self.VerificadorOrdem = False
VerificadorColeta = False
self.abrir_navegador()

time.sleep(1)
while True:
    if(self.VerificadorEmail):
        self.VerificadorEmail = False
        self.add_login()
        self.VerificadorSenha = True
    if(self.VerificadorSenha):
        self.VerificadorSenha = False
        self.add_senha()
        self.VerificadorCompany = True
        self.VerificadorProjeto = True
    if(self.VerificadorCompany):
        self.VerificadorCompany = False   
        self.add_company()
        self.VerificadorProjeto = True                 
    if(self.VerificadorProjeto):
        self.VerificadorProjeto = False
        self.select_project()
        self.VerificadorIssues = True
    if(self.VerificadorIssues):
        self.VerificadorIssues = False
        self.go_to_issues()
        self.VerificadorFiltro = True
    if(self.VerificadorFiltro):
        self.VerificadorFiltro = False
        self.filtro()
        self.VerificadorOrdem = True
    if(self.VerificadorOrdem):
        self.VerificadorOrdem = False
        self.selecao_incompatibilidades()
        self.ordem()
        VerificadorColeta = True
    if(VerificadorColeta):
        self.coletar_dados()
        VerificadorColeta = False
"""