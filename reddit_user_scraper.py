import selenium
import json


class RedditUserScraper:

    def __init__(self, username, driver):

        self.username = username
        self.has_next_page = None
        self.driver = driver
        self.current_page_json = None
        self.on_first_page = None
        self.comment_sub_count = {}
        self.children = None

    @property
    def base_url(self):
        return 'https://www.reddit.com/user/{}.json'.format(self.username)

    @staticmethod
    def get_before_value(json_data):
        return json_data['data']['before']


    # The 'after' value is a string value which existences indicates another page is available to request
    # If there is no 'after' string value, a null entry (None for python) is used

    @staticmethod
    def get_after_value(json_text):
        return json_text['data']['after']

    @staticmethod
    def __is_comment(child):
        return child["kind"] == "t1"

    @staticmethod
    def get_sub_commented_in(child):
        return child["data"]["subreddit"]

    def __is_on_first_page(self, json_data):
        if self.get_before_value(json_data) is None:
            return True
        return False

    def __get_json_data(self, driver):
        body_text = driver.find_element_by_tag_name('body').text
        json_data = json.loads(body_text)
        return json_data

    def __has_after_value(self, json_text):
        if self.get_after_value(json_text) is None:
            return False
        else:
            return True

    # Returns a driver object of the next json page

    def navigate_to_next_page(self):
        json_data = self.__get_json_data(self.driver)

        self.add_comment_info_to_dict()

        if self.__has_after_value(json_data):
            after_val = self.get_after_value(json_data)
            self.driver.get(self.base_url + '?after=' + after_val)
        return self.driver

    def navigate_all_pages(self):
        while self.__has_after_value(self.__get_json_data(self.driver)):
            self.navigate_to_next_page()

    def __get_current_children_list(self):
        json_data = self.__get_json_data(self.driver)
        return json_data["data"]["children"]

    def add_comment_info_to_dict(self):
        child_list = self.__get_current_children_list()
        i = 0
        while i < len(child_list):
            if self.__is_comment(child_list[i]):
                sub = self.get_sub_commented_in(child_list[i])

                if sub in self.comment_sub_count:
                    self.comment_sub_count[sub] = self.comment_sub_count[sub] + 1
                else:
                    self.comment_sub_count[sub] = 1
            i = 1 + i
