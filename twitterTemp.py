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


    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path='/Users/barryyim/Documents/python/chromeDriver/chromedriver', chrome_options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.get('https://twitter.com/login')
    driver.find_element_by_name('session[username_or_email]').send_keys(username)
    time.sleep(8)
    driver.find_element_by_name('session[password]').send_keys(password)
    time.sleep(8)
    driver.find_element_by_class_name('submit EdgeButton EdgeButton--primary EdgeButtom--medium').click()
    time.sleep(8)

    driver.quit()

if __name__ == '__main__':
	twitterTemp()
