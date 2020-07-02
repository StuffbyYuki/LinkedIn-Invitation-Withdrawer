"""
• The code is working as of 7/1/2020.
• Your Message box on linkedin should be minimized when executing this code. When it's expanded, the code may or may not fail.
• You need your config file that contains your username, password, and path to your driver or you directly enter them in the code.
• Please adjust time.sleep() value depending on your computer condition/power.

• This code will login to your account and go to invitation "Sent" page. 
• And then go through list of people with your specified length of wait (ex.'1 week', 'month', 'year'). 
• The code will tell you the number of invitations you withdrew on each page.
• Might want to implement a func that sends an email telling the script finished executing (useful when executing on a long list).

@Author: Yuki Kakegawa 
@Github: StuffbyYuki
"""

import time
from selenium import webdriver
from config import EMAIL, PASS, PATH_TO_CHROMEDRIVER

linkedin = 'https://www.linkedin.com/'

class MyWithdrawer():
    def __init__(self, driver, period='month'):
        self.driver = driver
        self.driver.get(linkedin)
        self.period = period           #speficy your period here (ex. 'month', 'year', '4 weeks', etc. Default is 'month')
    
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
    
    def withdraw_invitation(self, withdraw_class_name, withdraw2_class_name):
        '''Wtihdraw if I sent the invite to the person with your specified period (any period that contains "month" by default).'''
        inv_list = self.driver.find_element_by_xpath("//ul[@class='mn-invitation-list']") #get the ul element
        withdrawn_count = 0
        for alist in inv_list.find_elements_by_tag_name('li'):                            #get the li element
            lower_text_value = alist.text.lower()
            if self.period in lower_text_value:
                #first layer
                withdraw_button = alist.find_element_by_class_name(withdraw_class_name) #Need to add onto alist variable instead of using "click_button()"
                withdraw_button.click()
                print('\nWithdraw button clicked!\n')
                time.sleep(3)
                #second layer
                self.click_button(withdraw2_class_name, find_element_by='class_name')
                print('\nWithdrew an invitation!\n')
                withdrawn_count += 1
                time.sleep(3)
        print('\nFinished going through invitation list on current page!\n')
        print(f'\nYou withdrew {withdrawn_count} invitations on this page!\n')
    
def main():
    #Set up your driver
    driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER) #Specify your chosen driver here. (i.g. firefox, safari, and chrome)
    myWithdrawer = MyWithdrawer(driver, 'month')    #By default, the code will withdraw invitations with more than a month wait.
    time.sleep(3) 

    #Go to the login page
    myWithdrawer.click_button('nav__button-secondary', find_element_by='class_name') 
    print('\nGo to the login page!\n')

    #Enter username(email) and password
    myWithdrawer.find_textbox_and_fill('session_key', EMAIL, find_element_by='name')
    print('\nEntered email!\n')
    myWithdrawer.find_textbox_and_fill('session_password', PASS, find_element_by='name')
    print('\nEntered password!\n')

    #Click on login button
    myWithdrawer.click_button('btn__primary--large.from__button--floating', find_element_by='class_name') 
    print('\nClicked login button!\n')

    #Go to the network page
    myWithdrawer.click_button('mynetwork-nav-item', find_element_by='id') 
    print('\nGo to the networks page!\n')

    #Go to the invitation manage page
    myWithdrawer.click_button('mn-invitations-preview__manage-all.artdeco-button.artdeco-button--tertiary.artdeco-button--muted.artdeco-button--2.ember-view', find_element_by='class_name') 
    print('\nGo to the invitation manage page!\n')

    #Go to the "Sent" section
    myWithdrawer.click_button('Sent', find_element_by='text') 
    print('\nGo to "Sent" section!\n')
    
    #I should go to the last page first. 
    #And then go back to previous so that I won't need to worry about new people coming in to the page which is problematic.
    #Withdraw invitations
    #Flip page until "next button" is disabled
    prev_button_class_name = 'artdeco-pagination__button.artdeco-pagination__button--previous.artdeco-button.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view'
    prev_button = driver.find_element_by_class_name(prev_button_class_name)
    next_button_class_name = "artdeco-pagination__button.artdeco-pagination__button--next.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--1.artdeco-button--tertiary.ember-view"
    next_button = driver.find_element_by_class_name(next_button_class_name)

    #Go to the last page and then go through the list of invitations as we come back to the first page.
    while next_button.is_enabled():
        print('\nGo to the next page!\n')
        myWithdrawer.click_button(next_button_class_name, find_element_by='class_name')
    while True:
        print('\nLoop for withdrawing started!\n')
        #Call and keep variables for the withdrawfunction here.
        withdraw_class_name = 'invitation-card__action-btn.artdeco-button.artdeco-button--muted.artdeco-button--3.artdeco-button--tertiary.ember-view'
        withdraw2_class_name = 'artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view'
        myWithdrawer.withdraw_invitation(withdraw_class_name, withdraw2_class_name) #Call withdraw function
        time.sleep(3)
        if not prev_button.is_enabled(): #If the prev button is not enabled, then break the loop
            break
        print("\nGo to the prev page!\n")
        myWithdrawer.click_button(prev_button_class_name, find_element_by='class_name') #Click the next button
    print("\nLoop ended!\n")
    
    #Might want to implement a func that sends an email telling the script finished executing. (useful when executing on a long list)

    #Quit the session
    print('\nQuitting the session!\n')
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    main()
