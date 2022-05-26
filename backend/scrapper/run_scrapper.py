from scrapper import ScrapperResearch

email = "oscarfreire@projete5d.com.br"
password = "@Timeprojete5d"
local_save = "data"

browser = ScrapperResearch(email,password,local_save)

browser.openResearch()
browser.addLogin()
browser.addSenha()
browser.addCompany()
browser.selectProject()
browser.goToIssues()
browser.openAll()
browser.htmlGenerator()

print(len(browser.htmlList))
