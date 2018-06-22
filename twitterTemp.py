#!/usr/bin/python

import time
from selenium import webdriver
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sys import argv
import click

@click.command()
@click.option('--temp', type=int, prompt='Temp', help='Your temperature to set')
@click.option('--username', prompt='Your Twitter username', help='Your Twitter account username')
@click.option('--password', prompt='Your Twitter password', help='Your Twitter account password')
def twitterTemp(temp, username, password):
    """Simple python program that takes the temp of the day and sends tweet."""
    print("Logging in as: " + username)
    print("Entered password: " + password)
    temp = str(temp)
    print("Entered temp: " + temp)

    DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0'
     driver = webdriver.PhantomJS(executable_path='/Users/devin.mancuso/node_modules/phantomjs/bin/phantomjs')
    driver.get('https://www.youtube.com/')
    driver.find_element_by_id('search').send_keys(username)
    time.sleep(8)
    #driver.find_element_by_class_name('session[password]').send_keys(password)
    #time.sleep(8)
    #driver.find_element_by_class_name('submit EdgeButton EdgeButton--primary EdgeButtom--medium').click()
    #time.sleep(8)

    driver.quit()

if __name__ == '__main__':
	twitterTemp()
