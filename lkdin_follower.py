"""
Login to your facebook and send bd wishes to your friend!

@Author: Yuki Kakegawa 
@Github: StuffbyYuki
"""

import time
from selenium import webdriver
from config import EMAIL, PASS



def find_textbox_and_fill(driver, key, config):
    '''We need to make it so that it can adopt search by id and name as well'''
    try:
        textbox = driver.find_element_by_name(key)
        textbox.send_keys(config)
        time.sleep(3)
        return
    except Exception as e:
        print(f'\nError! {e}\n')
        driver.quit()
    

def click_to_flip_page(driver, key):
    '''We need to make it so that it can adopt search by id and name as well'''
    try:
        button = driver.find_element_by_class_name(key)
        button.click()
        time.sleep(3)
        return
    except Exception as e:
        print(f'\nError! {e}\n')
        driver.quit()













def main():
    #Set up driver
    driver = webdriver.Chrome('/Users/Yuki/Downloads/chromedriver')#webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
    driver.get('https://www.linkedin.com/');
    time.sleep(3) 

    #go to the login page
    click_to_flip_page(driver, 'nav__button-secondary') 

    #fill username(email) and password
    find_textbox_and_fill(driver, 'session_key', EMAIL)
    find_textbox_and_fill(driver, 'session_password', PASS)

    #Click on login button
    click_to_flip_page(driver, 'btn__primary--large.from__button--floating') 



    #Quit the session
    print('Start counting to quit!')
    # time.sleep(3) 
    # driver.quit()




if __name__ == "__main__":
    main()
