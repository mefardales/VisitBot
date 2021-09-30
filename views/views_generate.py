from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configurations
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)


def urls_views(url, delay):
    time.sleep(delay)
    driver.get(url)
    print(f"Conected !!! to --> {url}")
    # driver.quit()
    print(f"Closed connection !!! from --> {url}")


def close_connection():
    driver.close()
