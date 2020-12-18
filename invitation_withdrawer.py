# -*- coding: UTF-8 -*-
"""
- Things to note -
• The code is working as of 10/27/2020.
• Your Message box on linkedin should be minimized when executing this code. When it's expanded, the code may or may not fail.
• You need your config file that contains your username, password, and path to your driver or any other way that works best for you.
• Please adjust time.sleep() value depending on your computer/browser condition/power.
• When the structure of the website changes, this script might not be able to do the job (I'll try to check and update the code occasionally).

- Summary of what this code does -
• This code will login to your account and go to invitation "Sent" page. 
• And then go through the list of people with your specified length (period) of how long you're waiting on an invitation (ex.'1 week', 'month', 'year'). 
• You can add an argument when you run the script in command line -> python my_script.py "2 weeks".
• Or you can change the value inside the script (default is set to "3 months").
• The code will tell you the number of invitations you withdrew on each page.

- Future development -
• Refer "TODO"s.

@Author: Yuki Kakegawa 
@Github: StuffbyYuki
"""

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import EMAIL, PASS, PATH_TO_CHROMEDRIVER
import mybrowser

class MyWithdrawer(mybrowser.MyBrowser):
    def __init__(self, driver, url, period='month'):
        super().__init__(driver, url)
        self.period = self.clean_astring(period)

    def withdraw_invitation(self, withdraw_class_name, withdraw2_class_name):
        """Wtihdraw if I sent the invite to the person with your specified period (any period that contains "month" for an instance)."""
        inv_list = self.driver.find_element_by_class_name('artdeco-list.mn-invitation-list')
        withdrawn_count = 0
        for alist in inv_list.find_elements_by_tag_name('li'):
            lower_text_value = self.clean_astring(alist.text)
            if self.period in lower_text_value:
                # first layer
                withdraw_button = alist.find_element_by_class_name(
                    withdraw_class_name)  # Need to add onto alist variable instead of using "click_button()" function
                withdraw_button.click()
                print(f'\n{withdrawn_count + 1}. Withdraw button clicked!\n')
                time.sleep(3)
                # second layer
                self.click_button(withdraw2_class_name, find_element_by='class_name')
                print('\nWithdrew an invitation!\n')
                withdrawn_count += 1
                time.sleep(3)
        print('\nFinished going through invitation list on current page!\n')
        print(f'\nYou withdrew {withdrawn_count} invitations on this page!\n')
    
    def clean_astring(self, string):
        """return a lower-cased string without any space"""
        return string.strip().replace(' ', '').lower()


def main():
    # Set up your driver
    url = 'https://www.linkedin.com/login'#'https://www.linkedin.com/mynetwork/invitation-manager/sent/'
    # chrome_options = Options()
    # chrome_options.set_headless()
    driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)  # Specify your chosen driver here. (i.g. firefox, safari, and chrome)
    if len(sys.argv) == 2:
        myWithdrawer = MyWithdrawer(driver, url, sys.argv[1])  # By default, the code will withdraw invitations with more than a month wait.
    else:
        myWithdrawer = MyWithdrawer(driver, url)
    time.sleep(5)
    print(f'\nYour specified length of wait: {myWithdrawer.period}\n')

    # TODO: Handle when "This page isn't working"

    # Go to the login page
    # myWithdrawer.click_button('nav__button-secondary', find_element_by='class_name')
    # print('\nGo to the login page!\n')

    # Enter username(email) and password
    myWithdrawer.find_textbox_and_fill('session_key', EMAIL, find_element_by='name')
    print('\nEntered email!\n')
    myWithdrawer.find_textbox_and_fill('session_password', PASS, find_element_by='name')
    print('\nEntered password!\n')

    # Click on login button
    time.sleep(3)
    myWithdrawer.click_button('btn__primary--large.from__button--floating', find_element_by='class_name')
    print('\nClicked login button!\n')

    # Go to the network page
    time.sleep(3)
    # myWithdrawer.click_button('My Network', find_element_by='text')
    sent_page = driver.find_element_by_xpath('/html/body/div[7]/header/div[2]/nav/ul/li[2]/a/span')
    sent_page.click()
    print('\nGo to the networks page!\n')

    # Go to the invitation manage page
    time.sleep(3)
    myWithdrawer.click_button(
        'mn-invitations-preview__manage-all.artdeco-button.artdeco-button--tertiary.artdeco-button--muted.artdeco-button--2.ember-view',
        find_element_by='class_name')
    print('\nGo to the invitation manage page!\n')

    # Go to the "Sent" section
    time.sleep(3)
    sent_button_class_name = driver.find_element_by_xpath('//button[text()="Sent"]')
    sent_button_class_name.click()
    print('\nGo to "Sent" section!\n')

    # Go to the last page first
    time.sleep(5)
    next_button_class_name = "artdeco-pagination__button.artdeco-pagination__button--next.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--1.artdeco-button--tertiary.ember-view"
    try:  # Check if next button. When there is no next button available, that means all invites are in one page.
        next_button = driver.find_element_by_class_name(next_button_class_name)
        while next_button.is_enabled():
            print('\nGo to the next page!\n')
            myWithdrawer.click_button(next_button_class_name, find_element_by='class_name')
    except:
        # Next button is NOT available
        pass


    # And then go through the list of invitations as we come back to the first page.
    while True:
        print('\nLoop for withdrawing started!\n')
        # Call and keep variables for the withdrawfunction here.
        withdraw_class_name = 'invitation-card__action-btn.artdeco-button.artdeco-button--muted.artdeco-button--3.artdeco-button--tertiary.ember-view'
        withdraw2_class_name = 'artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view'
        myWithdrawer.withdraw_invitation(withdraw_class_name, withdraw2_class_name)
        time.sleep(3)
        prev_button_class_name = 'artdeco-pagination__button.artdeco-pagination__button--previous.artdeco-button.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view'
        try:  # Check if there is prev button
            prev_button = driver.find_element_by_class_name(prev_button_class_name)
            if not prev_button.is_enabled():
                break
            print("\nGo to the prev page!\n")
            myWithdrawer.click_button(prev_button_class_name, find_element_by='class_name')
        except:
            # Prev button is NOT available
            break
    print("\nLoop ended!\n")

    # TODO: Might want to implement a func that sends an email telling the script finished executing. (useful when executing on a long list)

    # Quit the session
    print('\nQuitting the session!\n')
    time.sleep(3)
    driver.quit()


if __name__ == "__main__":
    main()
