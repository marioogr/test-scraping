from selenium import webdriver


def set_up_driver():
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.implicitly_wait(20)

    return driver
