from selenium import webdriver
import json
from reddit_user_scraper import RedditUserScraper
from Animal import Dog


driver = webdriver.Chrome()

infantyrbo = RedditUserScraper('Infantrybro', driver)

driver = driver.get(infantyrbo.base_url)

driver = infantyrbo.navigate_to_next_page()


# wolfie = Dog('Pitbull', 'Wolfie')
#
# wolfie.bark()
# #wolfie.__can_bark()
# print(wolfie.collar_color)
