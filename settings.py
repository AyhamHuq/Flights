# Ayham Huq

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from sys import argv


class Settings:
    def __init__(self):
        # Path of chrome driver
        _path = r'C:\VS Code\chromedriver'
        _service = Service(executable_path=_path)

        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=_service, options=self.options)
        # self.urls = argv
        # self.urls = ['https://www.facebook.com/marketplace/columbus/vehicles/?minPrice=5000&maxPrice=14000&maxMileage=150000&minYear=2009&sortBy=creation_time_descend&make=280909549507187&topLevelVehicleType=car_truck&exact=false',
        #              'https://www.facebook.com/marketplace/columbus/vehicles?minPrice=5000&maxPrice=14000&maxMileage=150000&minYear=2012&sortBy=creation_time_descend&make=308436969822020&model=651174758670055&topLevelVehicleType=car_truck&exact=false',
        #              'https://www.facebook.com/marketplace/columbus/vehicles?minPrice=5000&maxPrice=14000&maxMileage=150000&minYear=2016&sortBy=creation_time_descend&make=308436969822020&model=337357940220456&topLevelVehicleType=car_truck&exact=false',
        #              'https://www.facebook.com/marketplace/columbus/vehicles/?minPrice=5000&maxPrice=14000&maxMileage=150000&minYear=2009&sortBy=creation_time_descend&make=2101813456521413&topLevelVehicleType=car_truck&exact=false',
        #              'https://www.facebook.com/marketplace/columbus/vehicles?minPrice=5000&maxPrice=14000&maxMileage=150000&minYear=2009&sortBy=creation_time_descend&make=2318041991806363&model=2212785999032506&topLevelVehicleType=car_truck&exact=false',
        #              'https://www.facebook.com/marketplace/columbus/vehicles?minPrice=5000&maxPrice=14000&maxMileage=150000&minYear=2014&sortBy=creation_time_descend&make=2318041991806363&model=582109948940125&topLevelVehicleType=car_truck&exact=false'
        #             ]

        self._selenium_settings()
        self._chromium_settings()

    # Sets settings for selenium

    def _selenium_settings(self):
        # Wait for elements on page to load
        self.driver.implicitly_wait(10)

        # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

    # Sets settings from chrome driver

    def _chromium_settings(self):

        # Headless mode
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.headless = True
