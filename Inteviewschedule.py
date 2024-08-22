from seleniumpagefactory.Pagefactory import PageFactory

class Interviewschedule(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators={
        "interviewsch":('xpath','//*[@id="content"]/div[1]/div[1]/div/div/div/div/div[2]/fieldset/div[4]/a')
    }
    def click_gohome_is(self):
        self.interviewsch.click()