import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 3


def gh_login(browser):
    url = 'https://github.com/login'
    browser.get((url))
    username = browser.find_element_by_id('login_field')
    username.send_keys(os.environ.get('GH_USER'))
    pw = browser.find_element_by_id('password')
    pw.send_keys(os.environ.get('GH_PW'))
    pw.submit()


def transfer(browser, module, source_issue_no):
    source_base = f'https://github.com/dune-community/{module}'
    target_base = 'https://github.com/dune-community/dune-xt'
    source_issue_url = f'{source_base}/issues/{source_issue_no}'
    browser.get((source_issue_url))

    transfer = '''//*[@id="partial-discussion-sidebar"]/form'''
    transfer = browser.find_element_by_xpath(transfer)
    transfer.click()

    dropdown = '''//*[@id="partial-discussion-sidebar"]/form/div/details/details-dialog/div[2]/details/summary'''
    dropdown = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, dropdown))
    )
    dropdown.click()

    item = '''//*[@id="transfer-possible-repositories-menu"]/label[2]'''
    item = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, item))
    )
    item.click()

    button = '''//*[@id="partial-discussion-sidebar"]/form/div/details/details-dialog/div[3]/button'''
    button = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, button))
    )
    button.click()


browser = webdriver.Chrome()
gh_login(browser)
transfer(browser, 1)