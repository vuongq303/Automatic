from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
from time import sleep
import tkinter as tk
from tkinter import messagebox

facebookUrl = "https://facebook.com"
groupFacebookUrl = facebookUrl + "/groups/sharekhoahoccap3"
driverPath = "D:\Python\msedgedriver.exe"
# listGroupFacebook = ["sharekhoahoccap3", "753195100086574", "2165358637179256"]

root = tk.Tk()
root.title("Automatic Facebook")
root.geometry("800x600")


def openFacebook(username, password, content):
    service = Service(driverPath)
    driver = webdriver.Edge(service=service)
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
    findWriteFeedInGroup.click()

    writeToFeedGroup = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "._1mf._1mj"))
    )

    text_no_newlines = content.replace('\n', ' ').replace('\r', ' ')
    writeToFeedGroup.send_keys(text_no_newlines)

    logWithColor("Write to feed")
    postToFeed = driver.find_element(By.XPATH, '//div[span[span[text()="Đăng"]]]')
    postToFeed.click()

    sleep(2)
    logWithColor("Post to feed, wait 2 second")

    logWithColor("Wait 5 second")
    sleep(5)
    logWithColor("Exit")

    driver.quit()


def logWithColor(text):
    print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")


def submit_form():
    username = username_input.get()
    password = password_input.get()
    content = text_box.get("1.0", "end-1c")

    if username and password and content:
        openFacebook(username, password, content)
    else:
        messagebox.showwarning("Error", "Form is empty!")


tk.Label(root, text="Username:", font=("Arial", 12)).grid(
    row=0, column=0, padx=10, pady=5, sticky="w"
)
username_input = tk.Entry(root, font=("Arial", 12), width=30)
username_input.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:", font=("Arial", 12)).grid(
    row=2, column=0, padx=10, pady=5, sticky="w"
)
password_input = tk.Entry(root, font=("Arial", 12), show="*", width=30)
password_input.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Content:", font=("Arial", 12)).grid(
    row=3, column=0, padx=10, pady=5, sticky="w"
)
text_box = tk.Text(root, font=("Arial", 12), height=20, width=100, wrap="word")
text_box.grid(row=3, column=1, padx=10, pady=5)


submit_button = tk.Button(root, text="Gửi", font=("Arial", 12), command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)


root.mainloop()
