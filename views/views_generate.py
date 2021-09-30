from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

# Configurations
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)


def urls_views(url, delay):
    page = ''
    output = {}
    # Check url
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, url) is not None:
        while page == '':
            try:
                page = driver.get(url)
                #print(f"Conexión exitosa con --> {url}")
                output = {'Visitado -->': url}
                break
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(delay)
                print("Was a nice sleep, now let me continue...")
                continue
    else:
        #print(f"La direccion web es incorrecta --> {url}")
        output = {'Error': url}
    return output


def close_connection():
    driver.close()
