from selenium import webdriver #подключение библиотеки

import time
# driver = webdriver.Chrome()

driver = webdriver.Chrome(executable_path="chromedriver.exe")

# driver.get('https://google.com')

from selenium.webdriver.common.by import By




def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    selenium.get('https://google.com')

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    search_input = selenium.find_element(By.NAME, "q")


    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = selenium.find_element(By.NAME,'btnK')
    search_button.submit()

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')