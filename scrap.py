import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

KEYWORD = "Hello, Selenium!"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")

search_bar = driver.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys(KEYWORD)
search_bar.submit()

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".N54PNb.BToiNc"))
    )

    search_results = driver.find_elements(By.CSS_SELECTOR, ".N54PNb.BToiNc")
    for index, result in enumerate(search_results):
        result.screenshot(f"screenshots/{KEYWORD}-{index}.png")

    driver.execute_script("alert('Done!')")

    input("Press Enter to close the browser...")

    driver.quit()
except TimeoutException:
    print("Timeout: No search results found")
    driver.quit()
    exit()
