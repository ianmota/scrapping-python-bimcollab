from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class ResultStatus():
    def __init__(self,id:int,mensagem:str):
        self.id = id
        self.msg = mensagem
    def statusGenerate(self):
        return({'status':[self.id,self.msg]})

class Navigator():
    def __init__(self, webdriver, time:int, idElement:str):
        self.webdriver = webdriver
        self.time = time
        self.id = idElement
    
    def exceptionsID(self):
        return WebDriverWait(self.webdriver,self.time).until(ec.presence_of_element_located((By.ID,self.id)))
    
    def exceptionsCSSselector(self):
        return WebDriverWait(self.webdriver,self.time).until(ec.presence_of_element_located((By.CSS_SELECTOR,self.id)))