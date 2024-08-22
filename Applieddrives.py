from seleniumpagefactory.Pagefactory import PageFactory

class Applieddrives(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators={
        'applieddrives':('xpath','//*[@id="content"]/div[1]/div[1]/div/div/div/div[1]/fieldset/div[2]/a')
    }
    def click_gohome_ad(self):
        self.applieddrives.click()