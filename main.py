from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
from time import sleep

# Enter your Email & password
username = "U18103997@sharjah.ac.ae"
password = "10637939"
#


class BlackBoard:
    def __init__(self, course_xpath, bb_ultra_xpath):
        self.driver = webdriver.Firefox()
        self.driver.get("https://elearning.sharjah.ac.ae/")
        self.web = WebDriverWait(self.driver, 50)
        self.username = username
        self.password = password
        self.course_xpath = course_xpath
        self.bb_ultra_xpath = bb_ultra_xpath

    def waitMin(self, minutes):
        sleep(minutes * 60)

    def login(self):
        # agree button at the start
        self.driver.find_element_by_xpath('.//*[@id="agree_button"]').click()
        self.driver.find_element_by_css_selector(
            'input.button:nth-child(5)').click()
        self.web.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="userNameInput"]')))  # log in in the outlook
        self.driver.find_element_by_xpath(
            '//*[@id="userNameInput"]').send_keys(self.username)
        self.driver.find_element_by_xpath(
            '//*[@id="passwordInput"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="submitButton"]').click()

    def openCourses(self):
        self.web.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[10]/div/li/a')))
        self.web.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[4]/div/li/a'))).click()  # open the courses

    def disableMic(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        self.web.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[5]/div/button"))).click()
        self.web.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div/div/button"))).click()

    def enterCourse(self):
        self.web.until(EC.frame_to_be_available_and_switch_to_it(
            (By.ID, 'collabUltraLtiFrame')))  # switch to Blackboard Collaborate Ultra
        try:
            self.web.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/main/div[2]/div[3]/ul/li/div/div[2]/ul/li/button'))).click()
            self.web.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/main/div[2]/div[3]/ul/li/ul/li[1]/div/button'))).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/bb-loading-button/button').click()  # needs editing
        except:
            self.web.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div/main/div[1]/div/div/button'))).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/bb-loading-button/button').click()

    def courseDirs(self):
        self.web.until(EC.frame_to_be_available_and_switch_to_it(
            (By.CLASS_NAME, 'classic-learn-iframe')))

    def enterClass(self):
        self.login()
        self.openCourses()
        # selects Automata class
        self.web.until(EC.element_to_be_clickable(
            (By.XPATH, self.course_xpath))).click()
        # open  Blackboard Collaborate Ultra
        self.courseDirs()
        # open class
        self.web.until(EC.element_to_be_clickable(
            (By.XPATH, self.bb_ultra_xpath))).click()

        self.enterCourse()
        self.disableMic()
        self.waitMin(75)
        self.driver.quit()
