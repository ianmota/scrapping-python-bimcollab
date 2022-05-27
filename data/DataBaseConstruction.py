import pandas as pd
from backend.scrapper.scrapper import *

class Database():
    def __init__(self,id:list,title:list,status:list="None", 
                 build:list="None",                 description:list="None", 
                 label:list="None", assingTo:list="None", 
                 milestone:list="None", dataType:list="None",
                 area:list="None",deadline:list="None", priority:list="None",              lastModification:list="None") -> pd.DataFrame():
        """
        Constrói o banco de dados no pandas

        Args:
            database (ScrapperColect): banco de dados 
        """
        self.id = id 
        self.title = title
        self.status = status
        self.build = build
        self.description = description
        self.label = label
        self.assingTo = assingTo
        self.milestone = milestone
        self.dataType = dataType
        self.area = area
        self.deadline = deadline
        self.priority = priority
        self.lastModification = lastModification        
    
    def __str__(self) -> str:
        return("DataBase")
    
    def __repr__(self) -> str:
        return("DataBase")
    
    def dictionaryGeneration(self):
        dataDictionary = {
            "ID":self.id,
            "Título": self.title,
            "Status": self.status,
            "Empreendimento": self.build,
            "Descrição":self.description,
            "Etiqueta": self.label,
            "Responsável": self.assingTo,
            "Fase": self.milestone,
            "Tipo":self.dataType,
            "Local": self.area,
            "Prazo": self.deadline,
            "Prioridade": self.priority,
            "Última modificação": self.lastModification
            
        }
        return(dataDictionary)
    
    def dbBuild(self):
        dicionario = self.dictionaryGeneration()
        index = dicionario.pop("ID")
        
        database = pd.DataFrame(self.dictionaryGeneration(),index=index)
    
        return(database)