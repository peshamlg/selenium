import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ResponsiveScraper:
    def __init__(self, url:str, screenshot_dir:str):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = url
        self.screenshot_dir = screenshot_dir
        self.screen_sizes = [
            480,
            960,
            1024,
            1366,
            1920
        ]

    def finish(self):
        if self.driver:
            self.driver.quit()
            exit()

    def get_max_height(self):
        self.driver.maximize_window()
        max_window_size = self.driver.get_window_size()
        return max_window_size['height']

    def get_screenshot(self, size:int, max_height:int):
        self.driver.set_window_size(size, max_height)
        scroll_size = self.driver.execute_script("return document.body.scrollHeight")
        total_sections = scroll_size // max_height + 1
        for section in range(total_sections):
            self.driver.execute_script(f"window.scrollTo(0, {section * max_height})")
            time.sleep(1)
            self.driver.save_screenshot(f"screenshots/{size}-{section + 1}.png")

    def run(self):
        self.driver.get(self.url)
        max_height = self.get_max_height()
        for size in self.screen_sizes:
            self.get_screenshot(size, max_height)
        self.finish()

ResponsiveScraper("https://nomadcoders.co/", "screenshots").run()