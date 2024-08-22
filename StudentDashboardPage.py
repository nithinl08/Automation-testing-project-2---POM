from seleniumpagefactory import PageFactory

class StudentDashboardPage(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators={
        'newplacement':('xpath','//*[@id="ContentPlaceHolder1_ahrefnewdrive"]'),
        'interviewshedule':('xpath','//*[@id="ContentPlaceHolder1_ahrefInterview"]'),
        'applieddrives':('id','ContentPlaceHolder1_ahrefapplieddrive'),
        'coursematerials':('xpath','//*[@id="a1"]')
    }
    def click_newplacement(self):
        self.newplacement.click()
    def cick_iterviewschedules(self):
        self.interviewshedule.click()
    def click_applieddrives(self):
        self.applieddrives.click()
    def click_coursematerials(self):
        self.coursematerials.click()

  
        
    