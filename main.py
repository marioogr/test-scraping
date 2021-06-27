from selenium import webdriver
from querys import querys
from config import set_up_driver
from re import sub
import json
from datetime import datetime

def get_element_text_xpath(driver: webdriver.Chrome ,xpath):
    """Return text of element"""

    return driver.find_element_by_xpath(xpath).text


driver = set_up_driver()

driver.get("https://coinmarketcap.com/currencies/bitcoin/")

driver.refresh()

"""cokies acept"""
driver.find_element_by_xpath(
    querys['buttons']['xpatch']['cookie_button']).click()

"""show more button click"""
show_more_button = driver.find_element_by_xpath(
    querys['buttons']['xpatch']['show_more_button'])
show_more_button.click()


regexp = "[^0-9\.]"

statistics_querys = querys['statistics']['xpatch']

date = datetime.now().strftime("%Y-%m-%d")

data = {
    "asset": "BTC",
    "values": []
}

temp = {}
for query in statistics_querys:
    temp[query] = float(sub(regexp,"",get_element_text_xpath(
                        driver ,statistics_querys[query])))

data['values'].append({date: temp})

print (json.dumps(data))

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

driver.close()