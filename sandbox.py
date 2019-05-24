from selenium import webdriver
import json
from reddit_user_scraper import RedditUserScraper
from Animal import Dog
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

s = RedditUserScraper('h')
user = RedditUserScraper('ConstantDeclamation', driver)

driver = driver.get(user.base_url)


user.navigate_all_pages()
print("sub, sub_comment_count")
for sub in user.comment_sub_count:
    print(sub + "," + str(user.comment_sub_count[sub]["comment_count"]))


print()
print('sub,commented_time')
for sub in user.comment_sub_count:
    for time in user.comment_sub_count[sub]['times_posted']:
        print(sub + ',' + time)


# wolfie = Dog('Pitbull', 'Wolfie')
#
# wolfie.bark()
# #wolfie.__can_bark()
# print(wolfie.collar_color)

# with open('hello.html') as html:
#     my_html_file = BeautifulSoup(html)
#     a = 6
#
# print(my_html_file.get_text)
# print(a)