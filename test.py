
from selenium import webdriver

import os

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--headless")

chrome_options.add_argument("--disable-dev-shm-usage")

chrome_options.add_argument("--no-sandbox")

chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

driver = 





print("Finished!")


