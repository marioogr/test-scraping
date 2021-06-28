from selenium import webdriver
from querys import assets_querys
from config import set_up_driver
from re import sub
from json import dumps, dump
from datetime import datetime
from constants import regexp

implicitly_wait = 10

def get_element_text_xpath(
        driver: webdriver.Chrome ,xpath: str):
    """Return text of element"""
    
    return driver.find_element_by_xpath(xpath).text

driver = set_up_driver(implicitly_wait)

driver.get("https://coinmarketcap.com/")

for asset in assets_querys:
    driver.find_element_by_xpath(
        asset['entry_point']['xpath']).click()
    driver.refresh()

    #cookie acept 
    driver.find_element_by_xpath(
        asset['buttons']['xpath']['cookie_button']).click()

    #show more button click
    driver.find_element_by_xpath(
        asset['buttons']['xpath']['show_more_button']).click()

    statistics_querys = asset['statistics']['xpath']
    date = datetime.now().strftime("%Y-%m-%d")

    data = {
        "asset": asset['asset'],
        "values": []
    }

    temp = {}
    for query in statistics_querys:
        temp[query] = float(sub(regexp,"",get_element_text_xpath(
                            driver ,statistics_querys[query])))

    data['values'].append({date: temp})


print (dumps(data, indent=4))
driver.close()

#data to json file
with open('data.json', 'w') as file:
    dump(data, file, indent=4)

