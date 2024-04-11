# Ayham Huq

from settings import Settings
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import sys
from sys import argv
import os
import logging as log

import pandas as pd

application_path = os.path.dirname(sys.executable)
final_path = os.path.join(application_path, 'flights.csv')

log_level = os.environ.get('LOG_LEVEL', 'INFO')
log.basicConfig(level=log_level)

SLEEP_TIME = .5


class Flights:

    # Initialzies Flights scraping
    def __init__(self, passengers, departure_date, ret_date, srcs, dest_pairs, max_cost=1500, max_duration=10):
        self.options = Settings()
        self.passengers = passengers
        self.departure_date = departure_date
        self.ret_date = ret_date
        self.srcs = srcs
        self.dest_pairs = dest_pairs
        self.max_cost = max_cost
        self.max_duration = max_duration

    # Sets the correct number of passengers

    def set_passengers(self):
        try:
            passengers = self.options.driver.find_element(
                By.CSS_SELECTOR, 'div.cQnuXe.k0gFV > div > button')
            passengers.click()

            increment = self.options.driver.find_element(
                By.CSS_SELECTOR, 'div.ZGEB9c.yRXJAe.iWO5td > ul > li:nth-child(1) > div > div > span:nth-child(3) > button')
            for i in range(self.passengers - 1):
                increment.click()

            done = self.options.driver.find_element(
                By.CSS_SELECTOR, 'div.IUKzPc > button:nth-child(1)')
            done.click()
        except Exception as e:
            log.error(e)
    # Process departure and ret

    def process_airports(self, src, dest_pair):
        try:
            # Inputs the correct location for the source
            departure = self.options.driver.find_element(
                By.CSS_SELECTOR, 'div.cQnuXe.k0gFV > div > div > input')
            departure.clear()
            departure.send_keys(src)
            self.options.driver.find_element(
                By.CSS_SELECTOR, 'div.XOeJFd.rHFvzd > ul > li').click()

            # Set first destination
            dest_1 = self.options.driver.find_element(
                By.CSS_SELECTOR, 'div.e5F5td.vxNK6d > div > div > div.cQnuXe.k0gFV > div > div > input')
            dest_1.send_keys(dest_pair[0])
            self.options.driver.find_element(
                By.CSS_SELECTOR, 'div.ZGEB9c.yRXJAe.P0ukfb.a4gL0d.TFC9me.PRvvEd.WKeVIb.Otspu.iWO5td.BDJ8fb > div.XOeJFd.rHFvzd > ul > li:nth-child(1)').click()

            # Make multi city
            self.options.driver.find_element(
                By.CSS_SELECTOR, 'div.VfPpkd-TkwUic').click()
            self.options.driver.find_element(
                By.CSS_SELECTOR, 'div.VfPpkd-xl07Ob-XxIAqe.VfPpkd-xl07Ob.VfPpkd-YPmvEd.s8kOBc.dmaMHc.VfPpkd-xl07Ob-XxIAqe-OWXEXe-uxVfW-FNFY6c-uFfGwd.VfPpkd-xl07Ob-XxIAqe-OWXEXe-FNFY6c > ul > li:nth-child(4)').click()

            # Set second destination
            sleep(SLEEP_TIME)
            dest_2 = self.options.driver.find_element(
                By.XPATH, '    /html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input')
            dest_2.clear()
            dest_2.send_keys(dest_pair[1])
            self.options.driver.find_element(
                By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[1]/div[6]/div[3]/ul/li[1]').click()
        except Exception as e:
            log.error(e)
    # Process dates

    def process_dates(self, departure_date, ret_date):
        try:
            # Set departure date
            departure_window = self.options.driver.find_element(
                By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input')
            departure_window.click()

            departure = self.options.driver.find_element(
                By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/input')
            sleep(SLEEP_TIME)
            departure.send_keys(Keys.BACKSPACE * 11)
            sleep(SLEEP_TIME)
            departure.send_keys(departure_date)
            sleep(SLEEP_TIME)
            self.options.driver.find_element(
                By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/button').click()

            # Set ret date
            sleep(SLEEP_TIME)
            ret = self.options.driver.find_element(
                By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/input')
            sleep(SLEEP_TIME)
            ret.send_keys(Keys.BACK_SPACE * 11)
            sleep(SLEEP_TIME)
            ret.send_keys(ret_date)
            sleep(SLEEP_TIME)
            ret.click()
            sleep(SLEEP_TIME)
            self.options.driver.find_element(
                By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/button').click()

            # Submit
            self.options.driver.find_element(
                By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button').click()
        except Exception as e:
            log.error(e)

    # Puts data in CSV file
    def _put_in_csv(self, src, dest_pair, dep_time_pair, ret_time_pair, cost, initial_duration, final_duration):
        try:
            flights = pd.DataFrame(
                {
                    'Cost': [cost],
                    'Departure': [src],
                    'Departure Times': [f'{dep_time_pair[0]}-{dep_time_pair[1]}'],
                    'Initial Duration': initial_duration,
                    'First Destination': [dest_pair[0]],
                    'Second Destination': [dest_pair[1]],
                    'Return Times': [f'{ret_time_pair[0]}-{ret_time_pair[1]}'],
                    'Final Duration': final_duration
                }
            )
            flights.to_csv(final_path, mode='a', index=False, header=False)
        except Exception as e:
            log.error(e)

    # Checks cost and reports it in CSV
    def check_compliance(self, src, dest_pair):
        try:
            sleep(SLEEP_TIME)
            specific_flight = self.options.driver.find_element(
                By.CSS_SELECTOR, 'div.yR1fYc')
            sleep(SLEEP_TIME)
            cost = self.max_cost
            i = 0
            while cost <= self.max_cost:
                cost = int(specific_flight.find_element(
                    By.XPATH, './div/div[9]/div[2]/span').get_attribute("textContent").removeprefix('$').replace(',', ''))
                dep_time_pair = (specific_flight.find_element(By.XPATH, './div/div[4]').get_attribute("textContent").replace(
                    '\u202f', ''), specific_flight.find_element(By.XPATH, './div/div[6]').get_attribute("textContent").replace('\u202f', ''))
                initial_duration = int(specific_flight.find_element(
                    By.XPATH, './div/div[2]/div[3]/div').get_attribute('textContent')[0:2])
                if cost < self.max_cost and initial_duration < self.max_duration:
                    specific_flight.click()
                    specific_ret_flights = self.options.driver.find_elements(
                        By.CSS_SELECTOR, 'div.yR1fYc')
                    for specific_ret_flight in specific_ret_flights:
                        full_cost = int(specific_ret_flight.find_element(
                            By.XPATH, './div/div[9]/div[2]/span').get_attribute("textContent").removeprefix('$').replace(',', ''))
                        if full_cost < self.max_cost:
                            ret_time_pair = (specific_ret_flight.find_element(By.XPATH, './div/div[4]').get_attribute("textContent").replace(
                                '\u202f', ''), specific_ret_flight.find_element(By.XPATH, './div/div[6]').get_attribute("textContent").replace('\u202f', ''))
                            final_duration = int(specific_ret_flight.find_element(
                                By.XPATH, './div/div[2]/div[3]/div').get_attribute('textContent')[0:2])
                            if final_duration < self.max_duration:
                                self._put_in_csv(
                                    src, dest_pair, dep_time_pair, ret_time_pair, full_cost, initial_duration, final_duration)
                            else:
                                log.info(
                                    f'This flight is {final_duration} many hours')
                        else:
                            log.info(f'This flight costs {full_cost}')
                            break
                    self.options.driver.back()
                    sleep(SLEEP_TIME)
                i += 1
                specific_flight = self.options.driver.find_elements(
                    By.CSS_SELECTOR, 'div.yR1fYc')[i]
        except Exception as e:
            log.error(e)
            log.error(src)
            log.error(dest_pair)

    # Processes the flights

    def process_flights(self):
        try:
            # Clear csv file
            with open(final_path, 'w') as file:
                pass
            # Process flights pre reqs
            for src in self.srcs:
                for dest_pair in self.dest_pairs:
                    self.set_passengers()
                    self.process_airports(src, dest_pair)
                    self.process_dates(self.departure_date, self.ret_date)
                    self.check_compliance(src, dest_pair)
                    self.options.driver.get(
                        'https://www.google.com/travel/flights')

            # Sort csv file
            # Read the CSV file into a DataFrame
                    
            data = pd.read_csv(final_path)

            # Sort the DataFrame based on a specific column
            data.columns = ['Cost', 'Departure', 'Departure Times', 'Initial Duration',
                            'First Destination', 'Second Destination', 'Return Times',  'Final Duration']
            sorted_data = data.sort_values(by='Cost')

            # Save the sorted DataFrame back to a CSV file
            sorted_data.to_csv(final_path, index=False, header=True)
        except Exception as e:
            log.error(e)


def main():
    flights = Flights(
        max_cost=300,
        max_duration=8,
        passengers=1,
        departure_date='May 25, 2024',
        ret_date='May 30, 2024',
        srcs=["CMH", "CVG", "CLE", "DAY", "ORD"],
        dest_pairs=[('SEA', 'SEA')]
    )
    flights.options.driver.get('https://www.google.com/travel/flights')
    flights.process_flights()
    flights.options.driver.quit()


if __name__ == "__main__":
    main()
