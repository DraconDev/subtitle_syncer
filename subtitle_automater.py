import os
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DOWNLOAD_FOLDER = "H:\\_DL\\"


def setup_Chrome(folder):
    chrome_options = Options()
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": folder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        },
    )
    return chrome_options


def sync_subtitles(value, files, source_folder, target_folder=DOWNLOAD_FOLDER):
    driver = webdriver.Chrome(
        "../../_Tools/webdriver/chromedriver.exe",
        options=setup_Chrome(target_folder),
    )
    driver.get("https://subtitletools.com/subtitle-sync-shifter")
    regex = "(.+\.(srt|ass)$)"

    for file in files:
        if re.search(regex, file):
            #
            upload_subs = driver.find_element(By.ID, "subtitles-input")
            upload_subs.send_keys(f"{source_folder}{file}")

            #
            adjust_sync = driver.find_element(By.CLASS_NAME, "field")
            adjust_sync.send_keys(value)
            adjust_sync.send_keys(Keys.RETURN)

            # find and click download
            download_button = driver.find_element(By.CSS_SELECTOR, "button.a-text2")
            download_button.click()

            # back
            download_button = driver.find_element(By.CSS_SELECTOR, "a.a-text2.text-sm")
            download_button.click()
    # time.sleep(10)

    pass


def show_files_in_folder(folder=os.getcwd()):
    file_list = os.listdir(folder)
    return file_list
