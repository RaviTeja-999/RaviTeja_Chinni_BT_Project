import logging
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Sample1:
    def __init__(self):
        service = Service("C:\\Users\\178360\\PycharmProjects\\Drivers\\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()
    def go_to_url(self, url):
        self.driver.get(url)

    def switch_to_frames(self, id, element1):
        if self.driver.find_element(By.TAG_NAME, "iframe").is_displayed():
            self.driver.switch_to.frame(id)
            time.sleep(10)
            self.verify_alert_popup(element1)
        else:
            logging.info("Accept cookies Alert is not present")


    def verify_alert_popup(self, element1):
        time.sleep(10)
        if self.driver.find_element(By.XPATH, element1).is_displayed():
            self.driver.find_element(By.XPATH, element1).click()
        else:
            logging.info("No alert popup displayed")

    def mouse_hover(self, element2, element3):
        try:
            self.driver.switch_to.default_content()
            time.sleep(5)
            self.action1 = ActionChains(self.driver)
            self.webele = self.driver.find_element(By.XPATH, element2)

            self.webele2 = self.driver.find_element(By.XPATH, element3)
            self.action1.move_to_element(self.webele).perform()
            time.sleep(5)
            self.action1.move_to_element(self.webele2).click().perform()
            time.sleep(10)
        except Exception as e:
            logging.info("Could not hover on the given element", e)

    def find_banners(self, element):
        self.banner = self.driver.find_elements(By.XPATH, element)
        if len(self.banner) >= 3:
            assert True, "There are 3 or more than 3 banners present"
        else:
            assert False, "There are less than 3 banners"

    def scroll_bar(self, ele):
        try:
            self.simonly = self.driver.find_element(By.XPATH, ele)
            self.simonly.location_once_scrolled_into_view
        except Exception as e:
            logging.info("Couldn't scroll to the element", e)

    def click_verify_title(self, element, Title):
        self.simonly.click()
        time.sleep(10)
        if self.driver.title == Title:
            assert True, "Title found as expected"
        else:
            assert False, "Incorrect title name"

    def validate_xpath(self, xpath):
        if self.driver.find_element(By.XPATH, xpath).is_displayed():
            assert True, "found the expected element"
        else:
            assert False, "Couldn't find the expected element"

    def close_browser(self):
        self.driver.quit()


ob = Sample1()
ob.go_to_url("https://www.bt.com/")
ob.switch_to_frames(0, "//a[text()='Accept all cookies']")
ob.mouse_hover("//div[@class='bt-navbar-top-menu bt-navbar-left-menu']//span[text()='Mobile']", "//a[@data-di-id='di-id-1672f262-8d36f8c2']")
ob.find_banners("//a[@class='bt-btn bt-btn-primary mt-2 mb-12' and text()='See handset deals']/../div[@class='flexpay_flexpaycard_container__GnRx9']/div")
ob.scroll_bar("//a[@class='bt-btn bt-btn-primary' and text()='View SIM only deals']")
ob.click_verify_title("//a[@class='bt-btn bt-btn-primary' and text()='View SIM only deals']", "SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile")
ob.validate_xpath("(//div[normalize-space(text()) = '18']/sub[normalize-space(text()) = '.'])[last()]/ancestor::div[@class='simo-card-ee_plan_details_wrapper__2oiEq relative px-4 mb-5']/ancestor::div[@class='simo-card-ee_text_container__30ltg']/preceding-sibling::div")
ob.close_browser()