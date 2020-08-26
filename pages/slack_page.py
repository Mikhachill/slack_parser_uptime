from .base_page import BasePage
from .locators import SlackPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import requests
import pandas as pd

import itertools

id_massive = [1.0, 2.0]


class SlackPage(BasePage):

    def registration(self, work_zone, mail, pas):
        input_work_zone = self.browser.find_element(*SlackPageLocators.WORK_ZONE_INSERT)
        input_work_zone.send_keys(work_zone)
        time.sleep(3)
        countinue_button = self.browser.find_element(*SlackPageLocators.CONTINUE_BUTTON)
        countinue_button.click()
        time.sleep(3)
        google_button = self.browser.find_element(*SlackPageLocators.SIGN_WITH_GOOGLE_BUTTON)
        google_button.click()
        time.sleep(3)
        insert_mail = self.browser.find_element(*SlackPageLocators.INSERT_MAIL)
        insert_mail.send_keys(mail)
        time.sleep(3)
        dalee = self.browser.find_element(*SlackPageLocators.DALEE)
        dalee.click()
        time.sleep(3)
        insert_password = self.browser.find_element(*SlackPageLocators.INSERT_PASSWORD)
        insert_password.send_keys(pas)
        time.sleep(10)

        dalee2 = self.browser.find_element(*SlackPageLocators.DALEE2)
        dalee2.click()
        time.sleep(40)

        scroll_bar = self.browser.find_element(*SlackPageLocators.SCROLL_BAR)
        actions = ActionChains(self.browser)
        actions.move_to_element(scroll_bar)
        actions.drag_and_drop_by_offset(scroll_bar, 0, 300)
        actions.perform()

        time.sleep(3)

        infra_notification = self.browser.find_element(*SlackPageLocators.INFRA_GROUP)
        infra_notification.click()
        time.sleep(3)

        to_day_button = self.browser.find_element(*SlackPageLocators.TO_DAY)
        to_day_button.click()
        time.sleep(3)

        specific_date = self.browser.find_element(*SlackPageLocators.SPECIFIC_DATE)
        specific_date.click()
        time.sleep(3)

        button_2020 = self.browser.find_element(*SlackPageLocators.BUTTON_2020)
        button_2020.click()
        time.sleep(3)

        january_button = self.browser.find_element(*SlackPageLocators.JANUARY)
        january_button.click()

        first_january = self.browser.find_element(*SlackPageLocators.FIRST)
        first_january.click()

        time.sleep(10)

    def data_for_pars(self):
        global id_massive
        z = 0
        xpath = "//div[@class='c-virtual_list c-virtual_list--scrollbar c-message_list c-scrollbar c-scrollbar--fade']/div/div/div[@data-qa='slack_kit_list']"
        for i in itertools.count():
            z += 1
            with open('debug.txt', 'a') as u:
                u.write('дошел до 95 ')

            try:
                data = self.browser.find_element(By.XPATH, xpath + f"/div[{z}]")
                with open('debug.txt', 'a') as u:
                    u.write('дошел до 99 ')

                if data.get_attribute('innerHTML') == 'Loading history...':
                    try:
                        self.browser.find_element(By.XPATH, xpath + f"/div[{z - 1}]")
                        with open('debug.txt', 'a') as u:
                            u.write('дошел до 104')

                        z = 0
                    except(NoSuchElementException):
                        iterator = 0
                        with open('debug.txt', 'a') as u:
                            u.write('дошел до 110')

                        for i in range(150):
                            try:
                                count_element = self.browser.find_element(By.XPATH, xpath + f"/div[{2 + i}]")
                                id_for_check = count_element.get_attribute('id')
                                if id_for_check == id_massive[-1]:
                                    iterator = i
                                    break
                            except(NoSuchElementException):
                                iterator = 0
                                break

                        with open('debug.txt', 'a') as u:
                            u.write(f'дошел до 117 break,итератор {iterator}')

                        for i in itertools.count():

                            lst = self.browser.find_element(By.XPATH, xpath + f"/div[{2 + iterator}]")
                            df = lst.get_attribute('innerHTML')
                            iterator += 1
                            with open('debug.txt', 'a') as u:
                                u.write('дошел до 126')

                            if df == 'Loading history...':
                                for_last_id = self.browser.find_element(By.XPATH, xpath + f"/div[{2 + iterator - 2}]")
                                last_id = for_last_id.get_attribute('id')
                                id_massive.append(last_id)
                                with open('id.txt', 'a') as u:
                                    u.write(last_id + ' ')
                                scroll = self.browser.find_element(*SlackPageLocators.MAIN_SCROLL_BAR)
                                actions = ActionChains(self.browser)
                                actions.move_to_element(scroll)
                                actions.drag_and_drop_by_offset(scroll, 0, 45)
                                actions.perform()
                                z = 0
                                with open('debug.txt', 'a') as u:
                                    u.write('дошел до 140 break')
                                break



                            else:
                                with open('slack.html', 'a') as output_file:
                                    output_file.write(df)

                            # with open('slack.html', 'a') as output_file:
                            #    if df[-100:-3] not in output_file[-600:-1]:
                            #       output_file.write(df)


            except(NoSuchElementException):
                z = 0
                with open('debug.txt', 'a') as u:
                    u.write('дошел до 150 основной except')

                #  else:
        #     time.sleep(1)
        #    scroll = self.browser.find_element(*SlackPageLocators.MAIN_SCROLL_BAR)
        #    actions = ActionChains(self.browser)
        #    actions.move_to_element(scroll)
        #    actions.drag_and_drop_by_offset(scroll,0,5)
        #    actions.perform()

        # до 90 сообщений за один показ
