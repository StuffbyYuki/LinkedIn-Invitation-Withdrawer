"""
- Things to note -
• The code is working as of 7/2/2020.
• Your Message box on linkedin should be minimized when executing this code. When it's expanded, the code may or may not fail.
• You need your config file that contains your username, password, and path to your driver or you directly enter them in the code.
• Please adjust time.sleep() value depending on your computer condition/power.
• Might want to implement a func that sends an email telling the script finished executing (useful when executing on a long list).

- Summary of what this code does -
1. This code will login to your account and go to invitation "Sent" page. 
2. And then go through list of people with your specified length of wait (ex.'1 week', 'month', 'year'). 
3. The code will tell you the number of invitations you withdrew on each page.

@Author: Yuki Kakegawa 
@Github: StuffbyYuki
"""

import time
from selenium import webdriver
from config import EMAIL, PASS, PATH_TO_CHROMEDRIVER
import mybrowser

class MyWithdrawer(mybrowser.MyBrowser):
    def __init__(self, driver, url, period):
        super().__init__(driver, url)
        self.period = period
    
    def withdraw_invitation(self, withdraw_class_name, withdraw2_class_name):
        '''Wtihdraw if I sent the invite to the person with your specified period (any period that contains "month" by default).'''
        inv_list = self.driver.find_element_by_xpath("//ul[@class='mn-invitation-list']") 
        withdrawn_count = 0
        for alist in inv_list.find_elements_by_tag_name('li'):                            
            lower_text_value = alist.text.lower()
            if self.period in lower_text_value:
                #first layer
                withdraw_button = alist.find_element_by_class_name(withdraw_class_name) #Need to add onto alist variable instead of using "click_button()" function
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
    url = 'https://www.linkedin.com/'
    driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)      #Specify your chosen driver here. (i.g. firefox, safari, and chrome)
    myWithdrawer = MyWithdrawer(driver, url, 'month')    #By default, the code will withdraw invitations with more than a month wait.
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
    
    #Create variables used for the upcoming while loops
    prev_button_class_name = 'artdeco-pagination__button.artdeco-pagination__button--previous.artdeco-button.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view'
    prev_button = driver.find_element_by_class_name(prev_button_class_name)
    next_button_class_name = "artdeco-pagination__button.artdeco-pagination__button--next.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--1.artdeco-button--tertiary.ember-view"
    next_button = driver.find_element_by_class_name(next_button_class_name)

    #Go to the last page first
    while next_button.is_enabled():
        print('\nGo to the next page!\n')
        myWithdrawer.click_button(next_button_class_name, find_element_by='class_name')
    
    #And then go through the list of invitations as we come back to the first page.
    while True:
        print('\nLoop for withdrawing started!\n')
        #Call and keep variables for the withdrawfunction here.
        withdraw_class_name = 'invitation-card__action-btn.artdeco-button.artdeco-button--muted.artdeco-button--3.artdeco-button--tertiary.ember-view'
        withdraw2_class_name = 'artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view'
        myWithdrawer.withdraw_invitation(withdraw_class_name, withdraw2_class_name) 
        time.sleep(3)
        if not prev_button.is_enabled():
            break
        print("\nGo to the prev page!\n")
        myWithdrawer.click_button(prev_button_class_name, find_element_by='class_name') 
    print("\nLoop ended!\n")
    
    #Might want to implement a func that sends an email telling the script finished executing. (useful when executing on a long list)

    #Quit the session
    print('\nQuitting the session!\n')
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    main()
