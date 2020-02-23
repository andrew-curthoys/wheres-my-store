from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from collections import namedtuple
from db_functions import pg_insert, pg_select
from zip_codes import get_zip_codes
import csv
import time


def duke_cannon():
    zip_code_list = get_zip_codes()
    for zip_code in zip_code_list:
        
        # wait 10 seconds between calls to not overload them with requests
        time.sleep(10)

        # create connection to Firefox browser to Duke Cannon store locator
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("https://dukecannon.com/pages/store-locator")

        # input zip code
        print(f'Gettings results for zip code: {zip_code}')
        zip_code_input = driver.find_element_by_id('storemapper-zip')
        zip_code_input.send_keys(zip_code)

        # submit zip code - use try/except method in case there is a pop-up window
        submit_button = driver.find_element_by_id('storemapper-go')
        try:
            submit_button.click()
        except:
            popup = driver.find_element_by_id('popup')
            popup_close = popup.find_element_by_class_name('close-modal')
            popup_close.click()
        submit_button.click()

        # get the container with the list of store information
        # then create a list of all stores
        store_list_container = driver.find_element_by_id('storemapper-list')
        store_list = store_list_container.find_elements_by_tag_name('li')

        # create namedtuple to hold the store information
        store_info = namedtuple('StoreInfo', 'store_id store_name address phone')

        # loop through each store and store the store name, address, & phone number
        # in a namedtuple called store_info
        store_data = []
        for store in store_list:
            store_id = store.get_attribute('data-idx')
            store_name = store.find_element_by_class_name('storemapper-title').text
            try:
                address = store.find_element_by_class_name('storemapper-address').text
            except:
                address = "No address found"
            try:
                phone = store.find_element_by_class_name('storemapper-phone').text
            except:
                phone = "No phone number found"
            store = store_info(store_id, store_name, address, phone)
            store_data.append(store)
        
        # insert data into Postgres DB
        pg_insert('duke_cannon', store_data)
    
        driver.quit()


def olivina_men():
    # create connection to Firefox browser to Olivina Men store locator
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://olivinamen.com/pages/store-locator")

    # get the container with the list of store information
    # then create a list of all stores
    store_list_container = driver.find_element_by_id('storemapper-list')
    store_list = store_list_container.find_elements_by_tag_name('li')

    # create namedtuple to hold the store information
    store_info = namedtuple('StoreInfo', 'store_id store_name address phone')

    # loop through each store and store the store name, address, & phone number
    # in a namedtuple called store_info
    store_data = []
    for store in store_list:
        store_id = store.get_attribute('data-idx')
        store_name = store.find_element_by_class_name('storemapper-title').text
        try:
            address = store.find_element_by_class_name('storemapper-address').text
        except:
            address = "No address found"
        try:
            phone = store.find_element_by_class_name('storemapper-phone').text
        except:
            phone = "No phone number found"
        store = store_info(store_id, store_name, address, phone)
        store_data.append(store)

    # insert data into Postgres DB
    pg_insert('olivina_men', store_data)

    driver.quit()


def fulton_and_roark():
    # create connection to Firefox browser to Fulton and Roark store locator
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://fultonandroark.com/pages/stockists")

    # get the container with the list of store information
    # then create a list of all stores
    store_list_container = driver.find_element_by_id('storemapper-list')
    store_list = store_list_container.find_elements_by_tag_name('li')

    # create namedtuple to hold the store information
    store_info = namedtuple('StoreInfo', 'store_id store_name address phone')

    # loop through each store and store the store name, address, & phone number
    # in a namedtuple called store_info
    store_data = []
    for store in store_list:
        store_id = store.get_attribute('data-idx')
        store_name = store.find_element_by_class_name('storemapper-title').text
        try:
            address = store.find_element_by_class_name('storemapper-address').text
        except:
            address = "No address found"
        try:
            phone = store.find_element_by_class_name('storemapper-phone').text
        except:
            phone = "No phone number found"
        store = store_info(store_id, store_name, address, phone)
        store_data.append(store)

    # insert data into Postgres DB
    pg_insert('fulton_and_roark', store_data)

    driver.quit()


def cbd_for_life():
    # create connection to Firefox browser to CBD for Life store locator
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://cbdforlife.us/store-locator/")

    # get the container with the list of store information
    # then create a list of all stores
    store_list_container = driver.find_element_by_id('storemapper-list')
    store_list = store_list_container.find_elements_by_tag_name('li')

    # create namedtuple to hold the store information
    store_info = namedtuple('StoreInfo', 'store_id store_name address phone')

    # loop through each store and store the store name, address, & phone number
    # in a namedtuple called store_info
    store_data = []
    for store in store_list:
        store_id = store.get_attribute('data-idx')
        store_name = store.find_element_by_class_name('storemapper-title').text
        try:
            address = store.find_element_by_class_name('storemapper-address').text
        except:
            address = "No address found"
        try:
            phone = store.find_element_by_class_name('storemapper-phone').text
        except:
            phone = "No phone number found"
        store = store_info(store_id, store_name, address, phone)
        store_data.append(store)

    # insert data into Postgres DB
    pg_insert('cbd_for_life', store_data)

    driver.quit()


if __name__ == "__main__":
    #olivina_men()
    #fulton_and_roark()
    #cbd_for_life()
    duke_cannon()
