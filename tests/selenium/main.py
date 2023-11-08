from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
import os
import hashPictureFile # by GS

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)


LOGIN_URL = 'https://www.facebook.com/login.php'
# LOGIN_URL = 'https://www.facebook.com/FolkMusicIsrael/posts/pfbid02QqJZ1xCueK69pA5DxknnZdWRT1HqYmzcSBj14G9suQZjVr9uxnfa48F811Ucn1bYl'


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
        self.driver.get(LOGIN_URL)
        sleep(1)


    def login(self):
        email_element = self.driver.find_element('id', "email")
        email_element.send_keys(self.email)  # Give keyboard input

        password_element = self.driver.find_element('id', "pass")
        password_element.send_keys(self.password)  # Give keyboard input

        # self.driver.get_screenshot_as_file("screenshotLogin.png")
        login_button = self.driver.find_element('id', "loginbutton")
        sleep(1)
        login_button.click()  # Send mouse click
        sleep(2)


    def screenCapture(self, postURL,reportID):
        # postURL = 'https://www.facebook.com/FolkMusicIsrael/posts/pfbid02QqJZ1xCueK69pA5DxknnZdWRT1HqYmzcSBj14G9suQZjVr9uxnfa48F811Ucn1bYl'
        self.driver.get(postURL)
        self.driver.get_screenshot_as_file("screenshotPost_0_" + reportID + ".png")
        sleep(1)
        self.driver.get_screenshot_as_file("screenshotPost_1_" + reportID + ".png")
        sleep(2)
        self.driver.get(postURL)
        self.driver.get_screenshot_as_file("screenshotPost_2_" + reportID + ".png")
        sleep(1)
        self.driver.get_screenshot_as_file("screenshotPost_3_" + reportID + ".png")


    def getPictureFileNameAndPath(self, reportID):
        script_directory = os.path.dirname(os.path.realpath(__file__))
        # return (f"The directory of the current script is: {script_directory}")
        return (script_directory + '\screenshotPost_0_' + reportID + '.png')


    def dismissAlert(self):
        alert = Alert(self.driver)
        print(alert.text)
        alert.dismiss()


if __name__ == '__main__':
    postURL = 'https://www.facebook.com/rogerwaters/posts/pfbid02HRtXq4b5J1Jkx9Am3BvYprbhZESAMAsgafbD2SoDRCqNPCWoTYKBb98AxF5zV3yrl'
    reportID = '28154'
    try:
        # fb_login = FacebookLogin(email='henriettamaragoza', password='fgal5313k', browser='chrome')
        fb_login = FacebookLogin(email='galtmp@gmail.com', password='fgal5313k', browser='chrome')
        PictureFileNameAndPath = fb_login.getPictureFileNameAndPath(reportID)
        fb_login.login()
        fb_login.screenCapture(postURL,reportID)

        PictureFileNameAndPath = fb_login.getPictureFileNameAndPath(reportID)
        # image_filepath = 'tst.png'
        md5_hash = hashPictureFile.compute_hash(PictureFileNameAndPath, 'md5')
        sha256_hash = hashPictureFile.compute_hash(PictureFileNameAndPath, 'sha256')

        print(f"\nReport ID: {reportID}")
        print(f"Post URL: {postURL}")
        print(f"PictureFileNameAndPath: {PictureFileNameAndPath}")
        print(f"MD5 hash of the image: {md5_hash}")
        print(f"SHA-256 hash of the image: {sha256_hash}")

    except Exception as error:
        print("An exception occurred:", error, type(error).__name__)  # An exception occurred: ZeroDivisionError
        exit()



