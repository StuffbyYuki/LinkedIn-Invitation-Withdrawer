"""
Login to your facebook and send bd wishes to your friend!

@Author: Yuki Kakegawa 
@Github: StuffbyYuki
"""

import time
from selenium import webdriver
from config import EMAIL, PASS



def find_textbox_and_fill(driver, key, config, find_element_by):
    '''locate a specified textbox and fill out text you put in'''
    try:
        if find_element_by == 'id':
            textbox = driver.find_element_by_id(key)
            textbox.send_keys(config)
        elif find_element_by == 'name':
            textbox = driver.find_element_by_name(key)
            textbox.send_keys(config)
        elif find_element_by == 'class_name':
            textbox = driver.find_element_by_class_name(key)
            textbox.send_keys(config)
        time.sleep(3)
        return
    except Exception as e:
        print(f'\nError! {e}\n')
        driver.quit()
    

def click_to_flip_page(driver, key, find_element_by):
    '''Locate an element you specified by id, name or class_name, and press the button'''
    try:
        if find_element_by == 'id':
            button = driver.find_element_by_id(key)
            button.click()
        elif find_element_by == 'name':
            button = driver.find_element_by_name(key)
            button.click()
        elif find_element_by == 'class_name':
            button = driver.find_element_by_class_name(key)
            button.click()
        elif find_element_by == 'text':
            button = driver.find_element_by_link_text(key)
            button.click()
        time.sleep(3)
    except Exception as e:
        print(f'\nError! {e}\n')
        driver.quit()

def main():
    #Set up driver
    driver = webdriver.Chrome('/Users/Yuki/Downloads/chromedriver')#webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
    driver.get('https://www.linkedin.com/');
    time.sleep(3) 

    #go to the login page
    click_to_flip_page(driver, 'nav__button-secondary', find_element_by='class_name') 

    #fill username(email) and password
    find_textbox_and_fill(driver, 'session_key', EMAIL, find_element_by='name')
    find_textbox_and_fill(driver, 'session_password', PASS, find_element_by='name')

    #Click on login button
    click_to_flip_page(driver, 'btn__primary--large.from__button--floating', find_element_by='class_name') 

    #Go to the network page
    click_to_flip_page(driver, 'mynetwork-nav-item', find_element_by='id') 

    #Go to the invitation manage page
    click_to_flip_page(driver, 'mn-invitations-preview__manage-all.artdeco-button.artdeco-button--tertiary.artdeco-button--muted.artdeco-button--2.ember-view', find_element_by='class_name') 

    #Go to the "Sent" section
    click_to_flip_page(driver, 'Sent', find_element_by='text') 
    
    #Maye scroll pages to the last page

    #If I sent the invitation a long time ago, I will click the withdraw bottun. 
    #As you go through the list of people in opposite order, check the time (i.e. 1 week ago), and say if they are too new, we don't withdraw 
    #And that means we reached the point where we don't have anyone too old who I sent the invitation to.

    #Hopefully implement a func that sends an email that says the number of people I withdrew my invite or error occured.


    #Quit the session
    print('Start counting to quit!')
    # time.sleep(3) 
    # driver.quit()




if __name__ == "__main__":
    main()
