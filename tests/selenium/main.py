from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
# driver = webdriver.Firefox()

LOGIN_URL = 'https://www.facebook.com/login.php'

class FacebookLogin():
    def __init__(self, email, password, browser='chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'chrome':
            # Use chrome
            # self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            # self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == 'firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        sleep(1) # Wait for some time to load


    def login(self):
        # email_element = self.driver.find_element_by_id('email')
        # email_element = self.driver.find_element("email", "q")
        # email_element = self.driver.find_element(self.driver.find_element.By.ID, "email")
        email_element = self.driver.find_element('id', "email")
        email_element.send_keys(self.email)  # Give keyboard input

        # password_element = self.driver.find_element_by_id('pass')
        # password_element.send_keys(self.password)  # Give password as input too
        password_element = self.driver.find_element('id', "pass")
        password_element.send_keys(self.password)  # Give keyboard input

        # login_button = self.driver.find_element_by_id('loginbutton')
        login_button = self.driver.find_element('id', "loginbutton")
        print('login_button',login_button)
        login_button.click()  # Send mouse click

        sleep(2)  # Wait for 2 seconds for the page to show up


    def screenCapture(self,url):
        print('starting screen capture')
        # driver.get('https://reva5.co.il')
        driver.get(url)
        # driver.get('https://www.instagram.com/reel/CzV9RnRKEVO/?utm_source=ig_web_copy_link')
        sleep(2)
        driver.get_screenshot_as_file("screenshot.png")
        driver.quit()
        print("end screen capture")


if __name__ == '__main__':
    url = 'https://www.facebook.com/FolkMusicIsrael/posts/pfbid02QqJZ1xCueK69pA5DxknnZdWRT1HqYmzcSBj14G9suQZjVr9uxnfa48F811Ucn1bYl'
    print('trying to log in')
    # Enter your login credentials here
    try:
        fb_login = FacebookLogin(email='henriettamaragoza', password='fgal5313k', browser='chrome')
        fb_login.login()
        fb_login.screenCapture(url)
    except Exception as error:
        print("An exception occurred:", error, type(error).__name__)  # An exception occurred: ZeroDivisionError
        exit()
    print('logged in')


#
# print('starting screen capture')
# # driver.get('https://reva5.co.il')
# driver.get('https://www.facebook.com/FolkMusicIsrael/posts/pfbid02QqJZ1xCueK69pA5DxknnZdWRT1HqYmzcSBj14G9suQZjVr9uxnfa48F811Ucn1bYl')
# # driver.get('https://www.instagram.com/reel/CzV9RnRKEVO/?utm_source=ig_web_copy_link')
# sleep(2)
# driver.get_screenshot_as_file("screenshot.png")
# driver.quit()
# print("end screen capture")