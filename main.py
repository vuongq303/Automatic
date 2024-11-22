from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController, Button

from time import sleep
import tkinter as tk
from tkinter import messagebox

facebookUrl = "https://facebook.com"
groupsFacebookUrl = [
    "386614282654291",
    "1224323587769514",
    "chungcu9999",
    "224257585866951",
    "1294145241531831",
    "4026316140810705",
    "1608065743039124",
    "chothuechungcuminihanoii",
    "330494224423543",
    "1466279290584312",
    "tglandmark.98",
    "903887330495903",
    "415565940789802",
    "252597635198019",
    "chungcuminihanoigiaree",
    "1215795799391969",
    "1539608956964434",
    "1437237960311125",
    "1313925196663431",
    "chothuephongtrochungcuhanoi",
    "193554109987236",
    "164150650736749",
    "batdongsan2022",
]

driverPath = "D:\Automatic\chromedriver.exe"
username = "0975460402"
password = "0338311009@#quanhq"
file_path = "D:\Automatic\images"

root = tk.Tk()
root.title("Automatic Facebook")
root.geometry("800x600")


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
    mouse = MouseController()
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
        post_content(keyboard, content, mouse, driver, group)

    driver.quit()


def logWithColor(text):
    print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")


def submit_form():
    content = text_box.get("1.0", "end-1c")

    if content:
        openFacebook(content)
        sleep(100)
    else:
        messagebox.showwarning("Error", "Form is empty!")


def post_content(keyboard, content, mouse, driver, group):
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
    openImage = driver.find_elements(
        By.XPATH,
        '//div[@class="x6s0dn4 x78zum5 xl56j7k x1n2onr6 x5yr21d xh8yej3"]',
    )
    openImage[1].click()
    sleep(0.5)
    openInputImage = driver.find_element(
        By.XPATH,
        '//div[span[text()="Thêm ảnh/video"]]',
    )
    openInputImage.click()
    logWithColor("Click to open file explorer")
    sleep(1)
    select_all_file(keyboard, mouse)
    logWithColor("Send image to feed")
    sleep(2)
    # post to feed

    # postToFeed = driver.find_element(By.XPATH, '//div[span[span[text()="Đăng"]]]')
    # postToFeed.click()
    # sleep(5)
    logWithColor("Complete " + group)


def select_all_file(keyboard, mouse):
    keyboard.type(file_path)
    sleep(0.5)
    logWithColor("Enter file path")

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    logWithColor("Click open")

    mouse.position = (120, 150)
    sleep(0.5)
    mouse.click(Button.left, 1)

    keyboard.press(Key.ctrl)
    keyboard.press("a")

    keyboard.release("a")
    keyboard.release(Key.ctrl)
    logWithColor("Select all image")

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


text_box = tk.Text(root, font=("Arial", 12), height=20, width=100, wrap="word")
text_box.grid(row=1, column=0, padx=10, pady=5)

submit_button = tk.Button(root, text="Gửi", font=("Arial", 12), command=submit_form)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
