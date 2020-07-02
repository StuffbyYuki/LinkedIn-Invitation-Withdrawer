"""
Your Message box should be minimized when executing this code. 
When it's expanded, the code may or may not fail.
The code is working as of 7/1/2020.

You need your config file that contains your username, password, and path to your driver or you directly put them in the code.

@Author: Yuki Kakegawa 
@Github: StuffbyYuki
"""

import time
from selenium import webdriver
from config import EMAIL, PASS, PATH_TO_CHROMEDRIVER

linkedin = 'https://www.linkedin.com/'

class MyWithdrawer():
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(linkedin)
    
    def find_textbox_and_fill(self, key, config, find_element_by):
        '''locate a specified textbox and fill out text you put in'''
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
            print('\nFound and filled the textbox!\n')
            time.sleep(3)
            return
        except Exception as e:
            print(f'\nError!\n\n {e}\n')
            self.driver.quit()
    
    def click_button(self, key, find_element_by):
        '''Locate an element you specified by id, name or class_name, and press the button'''
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
            print('\nClicked button!\n')
            time.sleep(3)
        except Exception as e:
            print(f'\nError!\n\n {e}\n')
            self.driver.quit()
    
    def withdraw_invitation(self):
        '''Wtihdraw if I sent the invite to the person more than a month ago.'''
        inv_list = self.driver.find_element_by_xpath("//ul[@class='mn-invitation-list']") #get the ul element
        for alist in inv_list.find_elements_by_tag_name('li'):                       #get the li element
            lower_text_value = alist.text.lower()
            if 'year' in lower_text_value:
                print('\n\n', lower_text_value)
                self.click_button(self.driver, 'Withdraw', find_element_by='text')
                print('withdrew an invitation!')
                time.sleep(1)
        print('\nFinished going through invitation list on the page!\n')
    
def main():
    #Set up driver
    driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)#webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
    myWithdrawer = MyWithdrawer(driver)
    time.sleep(3) 

    #go to the login page
    myWithdrawer.click_button('nav__button-secondary', find_element_by='class_name') 

    #fill username(email) and password
    myWithdrawer.find_textbox_and_fill('session_key', EMAIL, find_element_by='name')
    myWithdrawer.find_textbox_and_fill('session_password', PASS, find_element_by='name')

    #Click on login button
    myWithdrawer.click_button('btn__primary--large.from__button--floating', find_element_by='class_name') 

    #Go to the network page
    myWithdrawer.click_button('mynetwork-nav-item', find_element_by='id') 

    #Go to the invitation manage page
    myWithdrawer.click_button('mn-invitations-preview__manage-all.artdeco-button.artdeco-button--tertiary.artdeco-button--muted.artdeco-button--2.ember-view', find_element_by='class_name') 

    #Go to the "Sent" section
    myWithdrawer.click_button('Sent', find_element_by='text') 
    
    #Flip page until "next button" is disabled
    next_button_class_name = "artdeco-pagination__button.artdeco-pagination__button--next.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--1.artdeco-button--tertiary.ember-view"
    next_button = driver.find_element_by_class_name(next_button_class_name)

    while True:
        myWithdrawer.withdraw_invitation()
        time.sleep(2)
        print("\nNext page!\n")
        myWithdrawer.click_button(next_button_class_name, find_element_by='class_name')
        if not next_button.is_enabled():
            break
    print("\nWhile loop ended!\n")
    
    #We need to be able to go through the list of people one by one and see if we wanna delete from the list
    #If I sent the invitation a long time ago, I will click the withdraw bottun. 
    #As you go through the list of people in opposite order, check the time (i.e. 1 week ago), and say if they are too new, we don't withdraw 
    #And that means we reached the point where we don't have anyone too old who I sent the invitation to.

    #Hopefully implement a func that sends an email that says the number of people I withdrew my invite or error occured.


    #Quit the session
    print('Start counting to quit!')
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    main()
