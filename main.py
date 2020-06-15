import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from tqdm import tqdm

if __name__ == "__main__":
    driver = webdriver.Chrome()
    username = "test@gmail.com"
    insta_url = "https://www.instagram.com/?hl=en"

    # waits in sec
    soft_wait = 2
    long_wait = 4

    # INITIALIZE driver
    driver.get(insta_url)

    file_name = 'Database.csv'
    # reading file in pandas DataFrame
    user_id = pd.read_csv(file_name, encoding="ISO-8859-1", usecols=range(0, 1))

    driver.find_element_by_id('foo').send_keys(Keys.CONTROL + "a");
    driver.find_element_by_id('foo').send_keys(Keys.DELETE);

    for a in tqdm(range(len(user_id))):
        time.sleep(long_wait)
        driver.find_element_by_xpath("""//*[@name="username"]""").send_keys(Keys.CONTROL + "a")
        driver.find_element_by_xpath("""//*[@name="username"]""").send_keys(Keys.DELETE)
        driver.find_element_by_xpath("""//*[@name="username"]""").send_keys(username)
        driver.find_element_by_xpath("""//*[@name="password"]""").send_keys(Keys.CONTROL + "a")
        driver.find_element_by_xpath("""//*[@name="password"]""").send_keys(Keys.DELETE)
        driver.find_element_by_xpath("""//*[@name="password"]""").send_keys(user_id['password'][a])
        driver.find_element_by_xpath("""//*[@class="sqdOP  L3NKy   y3zKF     "]""").click()
        time.sleep(long_wait)
        msg = driver.find_element_by_xpath("""//*[@id="slfErrorAlert"]""").text
        print(msg)
