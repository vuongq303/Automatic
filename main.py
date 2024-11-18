from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
from pynput.keyboard import Controller, Key

from time import sleep
import tkinter as tk
from tkinter import messagebox
import os

facebookUrl = "https://facebook.com"
groupFacebookUrl = facebookUrl + "/groups/sharekhoahoccap3"
driverPath = "/Users/tv/Documents/Automatic/macos/chromedriver"
# listGroupFacebook = ["sharekhoahoccap3", "753195100086574", "2165358637179256"]

root = tk.Tk()
root.title("Automatic Facebook")
root.geometry("800x600")


def openFacebook(content):
    username = "aduc04915@gmail.com"
    password = "0338311009@#quanhq"
    service = Service(driverPath)
    driver = webdriver.Chrome(service=service)
    driver.get(facebookUrl)

    username_box = driver.find_element(By.ID, "email")
    password_box = driver.find_element(By.ID, "pass")
    button_login = driver.find_element(By.NAME, "login")

    username_box.send_keys(username)
    password_box.send_keys(password)
    button_login.click()

    logWithColor("Click login wait 1 second")
    sleep(1)

    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.COMMAND + "t")
    driver.get(groupFacebookUrl)

    logWithColor("Open new tab wait 1 second")
    sleep(1)
    driver.find_element(By.TAG_NAME, "body").click()

    findWriteFeedInGroup = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[span[text()="Bạn viết gì đi..."]]')
        )
    )

    logWithColor("Feed apear")
    sleep(1)
    findWriteFeedInGroup.click()

    writeToFeedGroup = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="_1mf _1mj"]'))
    )
    writeToFeedGroup.send_keys(content)
    logWithColor("Write complete")

    upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "images", "1.jpg")
    )
 
    addImage = driver.find_elements(
        By.XPATH,
        '//div[@class="x6s0dn4 x78zum5 xl56j7k x1n2onr6 x5yr21d xh8yej3"]',
    )
    addImage[1].click()
    
    keyboard = Controller()
    keyboard.type(upload_file)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    logWithColor("Send image to feed")
    # postToFeed = driver.find_element(By.XPATH, '//div[span[span[text()="Đăng"]]]')
    # postToFeed.click()

    sleep(2)
    logWithColor("Post to feed, wait 2 second")

    logWithColor("Wait 5 second")
    sleep(5)
    logWithColor("Exit")

    driver.quit()


def logWithColor(text):
    print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")


def submit_form():
    content = text_box.get("1.0", "end-1c")

    if content:
        openFacebook(content)
    else:
        messagebox.showwarning("Error", "Form is empty!")


tk.Label(root, text="Content:", font=("Arial", 12)).grid(
    row=1, column=0, padx=10, pady=5, sticky="w"
)
text_box = tk.Text(root, font=("Arial", 12), height=20, width=100, wrap="word")
text_box.grid(row=1, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Gửi", font=("Arial", 12), command=submit_form)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
