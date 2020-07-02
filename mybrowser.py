'''
The class with basic methods for crawling web pages defined here.

@Author: Yuki Kakegawa 
@Github: StuffbyYuki
'''

import time
from selenium import webdriver

class MyBrowser():
    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)
    
    def find_textbox_and_fill(self, key, config, find_element_by):
        '''Locate a specified textbox and fill out text you pass in'''
        try:
            if find_element_by == 'id':
                textbox = self.driver.find_element_by_id(key)
                textbox.send_keys(config)
            elif find_element_by == 'name':
                textbox = self.driver.find_element_by_name(key)
                textbox.send_keys(config)
            elif find_element_by == 'class_name':
                textbox = self.driver.find_element_by_class_name(key)
                textbox.send_keys(config)
            time.sleep(3)
            return
        except Exception as e:
            print(f'\nError!\n\n {e}\n')
            self.driver.quit()
    
    def click_button(self, key, find_element_by):
        '''Locate an element you specified by id, name, class_name, or text. And then click the button'''
        try:
            if find_element_by == 'id':
                button = self.driver.find_element_by_id(key)
                button.click()
            elif find_element_by == 'name':
                button = self.driver.find_element_by_name(key)
                button.click()
            elif find_element_by == 'class_name':
                button = self.driver.find_element_by_class_name(key)
                button.click()
            elif find_element_by == 'text':
                button = self.driver.find_element_by_link_text(key)
                button.click()
            time.sleep(3)
        except Exception as e:
            print(f'\nError!\n\n {e}\n')
            self.driver.quit()
