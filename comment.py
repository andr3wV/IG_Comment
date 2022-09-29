from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from myid import ID, PW
import time
import random

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://instagram.com')

    time.sleep(2) #If the page loading is slow, the next action cannot be executed and an error occurs.

    #login
    login_id = driver.find_element_by_name('username')
    login_id.send_keys(ID)
    login_pw = driver.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(5)

    #pass popup - If a pop-up window does not appear on the feed page after logging in, comment below and search for hashtags immediately
    popup = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    popup.send_keys(Keys.ENTER)
    time.sleep(3)
    popup = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    popup.send_keys(Keys.ENTER)

    time.sleep(2)

    #searh
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys('#Searching')
    time.sleep(5)
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
    feedCtn = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[2]/span/span').text
    print('Number of Feeds : {}'.format(feedCtn))
    search.send_keys(Keys.ENTER)

    time.sleep(3)

    #select first feed
    feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
    feed.send_keys(Keys.ENTER)

    time.sleep(5)

    feedCtn = 10
    comm_list = [
        'Whats Up',
        'You\'re the goat man!',
        'Great pics brotha!',
        'Good to hear from u bro!'
    ]
    while True:
        #comment
        comm = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div[1]/form/textarea')
        ran_comm = random.choice(comm_list)

        ac = ActionChains(driver)
        ac.move_to_element(comm)
        ac.click()
        ac.pause(3)
        ac.send_keys(ran_comm)
        ac.pause(1)
        ac.send_keys(Keys.ENTER)
        ac.perform()


        time.sleep(3)

        nextFeed = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
        ac = ActionChains(driver)
        ac.move_to_element(nextFeed)
        ac.click()
        ac.perform()

        if feedCtn == 1:
            break
        time.sleep(1)
except Exception as e:
    print(e)
finally:
    driver.quit()
