from src.pages.Skillgunloginpage import Skillgunloginpage
from src.pages.StudentDashboardPage import StudentDashboardPage
from src.pages.Newplacementpage import Newplacementpage
from src.pages.Inteviewschedule import Interviewschedule
from src.pages.Applieddrives import Applieddrives
import time
from selenium import webdriver
driver= webdriver.Chrome()

def test_login():
    driver.get('http://skillgun.com')
    time.sleep(5)
    l=Skillgunloginpage(driver)
    l.enter_mobile(7019050006)
    time.sleep(5)
    l.enter_email('nithinl2001@gmail.com')
    l.enter_password('Nithinl@0810')
    l.agreement()
    time.sleep(10)
    l.login_button()
    time.sleep(5)
    assert 'Home' in driver.current_url

def test_newplacement():
    dashboard= StudentDashboardPage(driver)
    dashboard.click_newplacement()
    time.sleep(5)
    assert 'NewPlacement' in driver.current_url

def test_Newplacementpage():
    newplace= Newplacementpage(driver)
    newplace.click_gohome()
    time.sleep(3)
    assert 'Home' in driver.current_url

def test_interviewschedule():
    intesch=StudentDashboardPage(driver)
    intesch.cick_iterviewschedules()
    time.sleep(3)
    assert 'Interviews' in driver.current_url

def test_interviewscheduleback():
    intscdback=Interviewschedule(driver)
    intscdback.click_gohome_is()
    time.sleep(3)
    assert 'Home' in driver.current_url

def test_applieddeives():
    appdri=StudentDashboardPage(driver)
    appdri.click_applieddrives()
    time.sleep(3)
    assert "AppliedDrives" in driver.current_url

def test_applieddrivesback():
    appdriback=Applieddrives(driver)
    appdriback.click_gohome_ad()
    time.sleep(3)
    assert 'Home' in driver.current_url

def test_coursematerials():
    coursemate=StudentDashboardPage(driver)
    coursemate.click_coursematerials()
    time.sleep(3)
    assert 'CourseMaterial' in driver.current_url
    driver.back()
    time.sleep(2)
    assert 'Home' in driver.current_url