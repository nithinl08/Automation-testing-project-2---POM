from seleniumpagefactory.Pagefactory import PageFactory

class Skillgunloginpage(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    locators={
        'mobile':('id','ContentPlaceHolder1_tbPhoneNumber'),
         'email':('id','ContentPlaceHolder1_tbEmail'),
        'password':('id','ContentPlaceHolder1_tbPassword'),
    'agree':('id','lblPolicyAgreement'),
    'logbutton':('xpath', '//*[@id="ContentPlaceHolder1_btnLogin"]')}
    def enter_mobile(self,mobileno):
        self.mobile.send_keys(mobileno)
    def enter_email(self,emailid):
        self.email.send_keys(emailid)
    def enter_password(self,passw):
        self.password.send_keys(passw)
    def agreement(self):
        self.agree.click()
    def login_button(self):
        self.logbutton.click()