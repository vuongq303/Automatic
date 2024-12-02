from sources.source import facebookUrl, driverPath, groupsFacebookUrl
from sources.util import logWithColor
from sources.functions.file import drag_and_drop_file
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Controller as KeyboardController
from tkinter import messagebox

username = "0975460402"
password = "0338311009@#quanhq"
file_path = "D:\Automatic\images\z6087732207028_27cef68c2ef88e439812bb7b9e319f06.jpg"


def openFacebook(content):
    option = Options()
    # chorme setting options
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-extensions")
    # chorme remove allow notification
    option.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.notifications": 2,
        },
    )
    # config selenium
    service = Service(driverPath)
    driver = webdriver.Chrome(service=service, options=option)
    keyboard = KeyboardController()
    driver.get(facebookUrl)

    username_box = driver.find_element(By.ID, "email")
    password_box = driver.find_element(By.ID, "pass")
    button_login = driver.find_element(By.NAME, "login")

    username_box.send_keys(username)
    password_box.send_keys(password)
    button_login.click()

    logWithColor("Click login")
    sleep(1)

    for group in groupsFacebookUrl:
        post_content(keyboard, content, driver, group)

    driver.quit()


def post_content(keyboard, content, driver, group):
    groupFacebookUrl = facebookUrl + "/groups/" + group
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.COMMAND + "t")
    # open group
    driver.get(groupFacebookUrl)
    logWithColor(f"Open {group}")
    sleep(2)
    # open feed
    findFeedInGroup = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe"]/span[text()="Bạn viết gì đi..."]',
            )
        )
    )
    findFeedInGroup.click()
    logWithColor("Feed apear")
    sleep(2)
    # write feed
    writeToFeedGroup = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="_1mf _1mj"]'))
    )
    writeToFeedGroup.send_keys(content)
    logWithColor("Write complete")
    sleep(1)
    # click open input image

    findInputImage = driver.find_elements(
        By.XPATH,
        '//div[@class="x6s0dn4 x78zum5 xl56j7k x1n2onr6 x5yr21d xh8yej3"]',
    )
    drag_and_drop_file(path=file_path, drop_target=findInputImage[1])
    logWithColor("Send image to feed")
    sleep(1)
    # post to feed
    # postToFeed = driver.find_element(By.XPATH, '//div[span[span[text()="Đăng"]]]')
    # postToFeed.click()
    sleep(5)
    logWithColor("Complete " + group)


def submit_form(text_box):
    content = text_box.get("1.0", "end-1c")

    if content:
        openFacebook(content)
        sleep(100)
    else:
        messagebox.showwarning("Error", "Form is empty!")
