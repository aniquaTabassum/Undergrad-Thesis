from selenium import webdriver
import random
import time
import selenium.webdriver.firefox.options
import time
import numpy as np


def get_random_delay():
    return int(random.uniform(5, 15))


def run_popsurvey():
    options = selenium.webdriver.firefox.options.Options()
    options.headless = True

    with webdriver.Firefox(
            executable_path=r"C:\Users\USER\Documents\AUST CSE 4.1\Undergrad Thesis\Website\geckodriver.exe",
            options=options) as driver:
        driver.get("http://popsurvey.azurewebsites.net/")
        sleep_time = get_random_delay()
        print("Sleeping for {} seconds before clicking 'Choose' option on VITA webpage.".format(sleep_time))
        time.sleep(sleep_time)


def get_delay():
    return np.random.uniform(-600, 600)


default_delay = 900
while True:
    run_popsurvey()
    noise = get_delay()
    sleep_time = default_delay + noise
    time.sleep(sleep_time)
