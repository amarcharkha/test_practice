import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep


@pytest.mark.lambdatest1_1
def test_lambdatest1_1():
    chrome_driver = webdriver.Chrome("C:\\Users\\HOD\Downloads\\driver path\\chromedriver.exe")

    chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
    chrome_driver.maximize_window()

    chrome_driver.find_element_by_name("li1").click()
    chrome_driver.find_element_by_name("li2").click()

    title = "Sample page - lambdatest.com"
    assert title == chrome_driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = chrome_driver.find_element_by_id("sampletodotext")
    email_text_field.send_keys(sample_text)
    time.sleep(5)

    chrome_driver.find_element_by_id("addbutton").click()
    time.sleep(5)

    output_str = chrome_driver.find_element_by_name("li6").text
    sys.stderr.write(output_str)

    time.sleep(2)
    chrome_driver.close()


@pytest.mark.lambdatest1_2
def test_lambdatest1_2():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('https://www.google.com/')
    chrome_driver.maximize_window()

    title = "Google"
    assert title == chrome_driver.title

    search_text = "LambdaTest"
    search_box = chrome_driver.find_element_by_xpath("//input[@name='q']")
    search_box.send_keys(search_text)

    time.sleep(5)

    # Option 1 - To Submit the search
    # search_box.submit()

    # Option 2 - To Submit the search
    search_box.send_keys(Keys.ARROW_DOWN)
    search_box.send_keys(Keys.ARROW_UP)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    # Click on the LambdaTest HomePage Link
    title = "Cross Browser Testing Tools | Free Automated Website Testing | LambdaTest"
    lt_link = chrome_driver.find_element_by_xpath(
        "//h3[.='LambdaTest: Cross Browser Testing Tools | Free Automated ...']")
    lt_link.click()

    time.sleep(10)
    assert title == chrome_driver.title

    chrome_driver.close()