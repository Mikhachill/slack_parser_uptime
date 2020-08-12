from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():
    def __init__(self,browser,url, timeout=5):
        self.browser=browser
        self.url=url
        self.browser.implicitly_wait(timeout)

 
    def open(self):
        self.browser.get(self.url)
  
    def is_disappeared(self, how, what, timeout=5):
        #WebDriver ждёт 4 секунды и делает запросы каждую секунду
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
            #если убрать _not тогда все будет проходить
            #потому что будет проверка на присутствие элемента  
        except TimeoutException:
            return False
        return True
    
#упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый. 
    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
                return True
        return False
 
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


        

    
    
