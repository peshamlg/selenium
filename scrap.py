from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class GoogleScraper:
    def __init__(self, keyword:str, screenshot_dir:str, max_page:int=1):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.keyword = keyword
        self.screenshot_dir = screenshot_dir
        self.max_page = max_page

    def finish(self):
        if self.driver:
            self.driver.quit()
            exit()

    def run(self):
        self.driver.get("https://www.google.com")

        search_bar = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.submit()

        try:
            screenshot_count = 0
            for page in range(self.max_page):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".N54PNb.BToiNc"))
                )

                search_results = self.driver.find_elements(By.CSS_SELECTOR, ".N54PNb.BToiNc")
                for index, result in enumerate(search_results):
                    screenshot_count += 1
                    result.screenshot(f"{self.screenshot_dir}/{self.keyword}-{page + 1}-{index + 1}.png")
                
                if page < self.max_page - 1:
                    next_button = self.driver.find_element(By.ID, "pnnext")
                    next_button.click()
            print("Done!")
            print(f"You've taken {screenshot_count} screenshots for {self.keyword}.")
            self.finish()
        except NoSuchElementException:
            print("No more pages found.")
            print(f"You've taken {screenshot_count} screenshots for {self.keyword}.")
            self.finish()
        except TimeoutException:
            print("Timeout: No search results found")
            print(f"You've taken {screenshot_count} screenshots for {self.keyword}.")
            self.finish()
        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"You've taken {screenshot_count} screenshots for {self.keyword}.")
            self.finish()

GoogleScraper("Selenium with Python", "screenshots", max_page=10).run()
