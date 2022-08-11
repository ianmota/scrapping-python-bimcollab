class Analysys():
    def __init__(self,dicionario) -> None:
        self.dic = dicionario
        self.GlobalVariables()
    
    def GlobalVariables(self):
        self.id1 = list()
        self.id2 = list()
        self.id3 = list()
        self.id4 = list()
        self.id5 = list()
        self.elemento1 = list()
        self.elemento2 = list()
        self.elemento3 = list()
        self.elemento4 = list()
        self.elemento5 = list()
        
        self.elementos = [self.id1,self.elemento1,self.id2,self.elemento2,self.id3,self.elemento3,self.id4,self.elemento4,self.id5,self.elemento5]
        
        self.disciplina1 = list()
        self.disciplina2 = list()
        self.disciplina3 = list() 
        self.disciplina4 = list() 
        self.disciplina5 = list() 
        self.disciplina6 = list() 
        self.disciplina7= list() 

        self.disciplinas = [self.disciplina1, self.disciplina2, self.disciplina3, self.disciplina4, self.disciplina5, self.disciplina6, self.disciplina7 ]
        
        self.updatedStatus = list()
        
        self.incompatibilidades = list()
        self.sugestoes = list()
        self.duvidas = list()
        
        self.primeirasAlteracoes = list()
        self.ultimasAlteracoes = list()
        
    def SeparadorInc(self):
        
        teste = list()
        for values in self.dic["Título"]:
            
            if "&" in values:
                splitValue = values.split("&")
            else:
                splitValue = values
            
            if type(splitValue) == list:
                countSplit = len(splitValue)
            else:
                countSplit = 1

            teste.append(splitValue)
        
        return teste
    
    def SeparadorID(self):
        
        teste2 = list()
        for i in range(len(self.SeparadorInc())):

            if type(self.SeparadorInc()[i]) == str:
                splitVar = self.SeparadorInc()[i].split("-")
                teste2.append(splitVar)
                
            if type(self.SeparadorInc()[i]) == list:
                variavel = []
                for j in range(len(self.SeparadorInc()[i])):
                    variavel = variavel + self.SeparadorInc()[i][j].split("-")
                teste2.append(variavel)
        return teste2
    
    def VerInc(self):
        for i in range(len(self.SeparadorID())):
            if len(self.SeparadorID()[i]) % 2 != 0:
                for j in range(len(self.elementos)):
                    self.elementos[j].append(None)
            
            else:
                for j in range(len(self.elementos)):
                    try:
                        self.elementos[j].append(self.SeparadorID()[i][j])
                    except IndexError:
                        self.elementos[j].append(None)
                        
    def VerID(self):
        
        for j in range(len(self.elementos)):
            for i in range(len(self.elementos[j])):

                if not self.elementos[j][i]:
                    continue

                else:
                    
                    if j%2 == 0:
                        try:
                            self.elementos[j][i] = int(self.elementos[j][i])
                        except ValueError:
                            self.elementos[j][i] = None
    def ErrorID(self):                            
        for i in range(len(self.elementos[0])):
            if not self.elementos[0][i]:
                for j in range(1,len(self.elementos)):
                    self.elementos[j][i] = "VERIFICAR"
        
        for i in range(len(self.elementos[0])):
            if not self.elementos[0][i]:
                for j in range(0,len(self.disciplinas)):
                    self.disciplinas[j][i] = "VERIFICAR"
        
        for i in range(len(self.elementos[0])):
            if not self.elementos[0][i]:
                self.updatedStatus[i] = "VERIFICAR"
        
        for i in range(len(self.elementos[0])):
            if not self.elementos[0][i]:
                self.incompatibilidades[i] = "VERIFICAR"
                self.sugestoes[i] = "VERIFICAR"
                self.duvidas[i] = "VERIFICAR"
   

    def GetDisciplinas(self):
        for titulos in self.dic["Etiqueta"]:
            etiquetas = titulos.split(",")
            
            if len(etiquetas)<=7:
                for i in range(len(self.disciplinas)):
                    try:
                        self.disciplinas[i].append(etiquetas[i]) 
                    except IndexError:
                        self.disciplinas[i].append(None) 
        return etiquetas
    
    def GetStatus(self):
        for status in dicionario["Status"]:
            if status.replace(" ","").upper() == "Active".upper():
                self.updatedStatus.append("Aberta")
            elif status.replace(" ","").upper() == "Resolved".upper():
                self.updatedStatus.append("Resolvida")
            
            elif status.replace(" ","").upper() == "Closed".upper():
                self.updatedStatus.append("Resolvida")
                
    def GetMarcadores(self):
        for j in range(len(dicionario["Descrição"])):
            splitDs01 = dicionario["Descrição"][j].split("-")
            
            for i in range(len(splitDs01)):
                if not splitDs01[i]:
                    splitDs01[i] = None
                elif len(splitDs01[i]) > 1:
                    splitDs01[i] = None

                if splitDs01[i] == "I":
                    incompatibilidade = splitDs01[i]
                elif splitDs01[i] == "S":
                    sugestao = splitDs01[i]
                elif splitDs01[i] == "D":
                    duvida = splitDs01[i]
                else:
                    incompatibilidade = None
                    sugestao = None
                    duvida = None
                
            self.incompatibilidades.append(incompatibilidade)
            self.sugestoes.append(sugestao)
            self.duvidas.append(duvida) 
    
    def GetFirstAlteration(self):
        for p_alteracao in dicionario["Primeira alteração"]:
            split01 = p_alteracao.split(" ")[-2]
            self.primeirasAlteracoes.append(split01.replace("-","/"))
    
    def GetLastAlteration(self):
        for u_alteracao in dicionario["Última alteração"]:
            split01 = u_alteracao.split(" ")[-2]
            self.ultimasAlteracoes.append(split01.replace("-","/")) 
    
    def DicFiltered(self):
        _dicionario = self.dic
        dicionarioFiltrado = dict()

        dicionarioFiltrado["ID"] = _dicionario["ID"]
        dicionarioFiltrado["ID-ELEMENTO 01"] = self.elementos[0]
        dicionarioFiltrado["ELEMENTO 01"] = self.elementos[1]
        dicionarioFiltrado["ID-ELEMENTO 02"] = self.elementos[2]
        dicionarioFiltrado["ELEMENTO 02"] = self.elementos[3]
        dicionarioFiltrado["ID-ELEMENTO 03"] = self.elementos[4]
        dicionarioFiltrado["ELEMENTO 03"] = self.elementos[5]
        dicionarioFiltrado["ID-ELEMENTO 04"] = self.elementos[6]
        dicionarioFiltrado["ELEMENTO 04"] = self.elementos[7]
        dicionarioFiltrado["ID-ELEMENTO 05"] = self.elementos[8]
        dicionarioFiltrado["ELEMENTO 05"] = self.elementos[9]
        dicionarioFiltrado["DISCIPLINA 01"] = self.disciplinas[0]
        dicionarioFiltrado["DISCIPLINA 02"] = self.disciplinas[1]
        dicionarioFiltrado["DISCIPLINA 03"] = self.disciplinas[2]
        dicionarioFiltrado["DISCIPLINA 04"] = self.disciplinas[3]
        dicionarioFiltrado["DISCIPLINA 05"] = self.disciplinas[4]
        dicionarioFiltrado["DISCIPLINA 06"] = self.disciplinas[5]
        dicionarioFiltrado["DISCIPLINA 07"] = self.disciplinas[6]
        dicionarioFiltrado["STATUS"] = self.updatedStatus
        dicionarioFiltrado["EMPREENDIMENTO"] = _dicionario["Empreendimento"]
        dicionarioFiltrado["RESPONSÁVEL"] = _dicionario["Responsável"]
        dicionarioFiltrado["FASE"] = _dicionario["Fase"]
        dicionarioFiltrado["TIPO"] = _dicionario["Tipo"]
        dicionarioFiltrado["LOCAL"] = _dicionario["Local"]
        dicionarioFiltrado["PRAZO"] = _dicionario["Prazo"]
        dicionarioFiltrado["PRIORIDADE"] = _dicionario["Prioridade"]
        dicionarioFiltrado["PRIMEIRA ALTERAÇÃO"] = self.primeirasAlteracoes
        dicionarioFiltrado["ÚLTIMA ALTERAÇÃO"] = self.ultimasAlteracoes
        dicionarioFiltrado["MARCADOR 01"] = self.incompatibilidades
        dicionarioFiltrado["MARCADOR 02"] = self.sugestoes
        dicionarioFiltrado["MARCADOR 03"] = self.duvidas
        
        return dicionarioFiltrado
    


