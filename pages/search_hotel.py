import logging

class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.search_hotel_span_xpath = '//*[@id="s2id_autogen8"]/a/span[1]'
        self.search_hotel_input_xpath = '//*[@id="select2-drop"]/div/input'
        self.location_match_xpath = '//*[@id="select2-drop"]/ul/li/ul/li/div'
        self.check_in_input_name = 'checkin'
        self.check_out_input_name = 'checkout'
        self.travellers_input_id = 'travellersInput'
        self.adult_input_id = 'adultInput'
        self.child_input_id = 'childInput'
        self.search_button_xpath = "//button[text()=' Search']"

    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_xpath).click()

    def set_date(self, check_in, check_out):
        self.logger.info("Setting check in {checkin} and check out {checkout} dates".format(checkin=check_in, checkout=check_out))
        self.driver.find_element_by_name(self.check_in_input_name).send_keys(check_in)
        self.driver.find_element_by_name(self.check_out_input_name).send_keys(check_out)

    def set_number_of_travelers(self, adults, child):
        self.logger.info("Setting travellers adults - {adults} and child - {kids}".format(adults=adults, kids=child))
        self.driver.find_element_by_id(self.travellers_input_id).click()
        self.driver.find_element_by_id(self.adult_input_id).clear()
        self.driver.find_element_by_id(self.adult_input_id).send_keys(adults)
        self.driver.find_element_by_id(self.child_input_id).clear()
        self.driver.find_element_by_id(self.child_input_id).send_keys(child)

    def perform_search(self):
        self.logger.info("Performing search")
        self.driver.find_element_by_xpath(self.search_button_xpath).click()