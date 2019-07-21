from selenium import webdriver
import os
import time
import configparser
import random

class InstagramBot:


    def __init__(self,username,password):

        """
        To find buttons | //button[contains(text(), 'Follow')] |

        Initialization an instance of class InstagramBot class.
        Call the login method to login into IG.

        Args:
            username:str: The instagram username for user.
            password:str: The instagram password for user.

        Attributes:
            driver.selenium.webdriver.Chrome: To control chrome.

        """

        self.password = password
        self.username = username
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome()

        self.login()


    def login(self):

        self.driver.get('{}/accounts/login/'.format(self.base_url))

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()

        time.sleep(2)


    def nav_user(self,user):

        #Navigating to a given profile

        self.driver.get('{}/{}/'.format(self.base_url, user))


    def follow_user(self,user):

        #Follwing the single user only

        self.nav_user(user)
        follow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
        follow_button.click()


    def commenting(self,hashtag):

        # NOT WORKING YET #

        #Going to hashtag webpage
        self.driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.driver.find_elements_by_xpath('//span[@aria-label="Like"]').click()
        time.sleep(2)
        comm = 'Hey, Nice post. Mind if you guys visit my page @enterpreneurtics.'
        self.driver.send_keys(self.comm)
        post = self.driver.find_elements_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > button')
        post.click()


    def To_follow_followers_of_celebs(self,username):

        # Going to user profile and opening followers list
        self.driver.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        self.driver.find_element_by_tag_name('a').click()
        time.sleep(2)

        # Following the user in that followers list
        for i in range(1,14):

            try:
                follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[i]
                follow_button.click()
                time.sleep(2)
                try:
                    self.driver.find_element_by_css_selector('body > div:nth-child(20) > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
                    time.sleep(2)
                except:
                    continue
            except:
                continue


    def unfollow_users(self,username):

        # Going to profile
        self.driver.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        self.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a').click()
        time.sleep(2)

        for i in range(1,9999):

            follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[i]
            follow_button.click()
            time.sleep(1)
            self.driver.find_element_by_css_selector('body > div:nth-child(20) > div > div > div.mt3GC > button.aOOlW.-Cab_').click()
            time.sleep(2)


if  __name__ == '__main__':


    #Reading username and password
    config = './config_.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config)
    cparser['IG_AUTH']['USERNAME']
    cparser['IG_AUTH']['PASSWORD']


    # Declaring Tags & Usernames For later usage


    # Instagramtags
    tags = ['love' , 'instagood' , 'photooftheday' , 'fashion' , 'beautiful' , 'happy' , 'cute' , 'tbt' , 'like4like' , 'followme' ,
                'picoftheday', 'follow', 'me', 'selfie', 'summer', 'art', 'instadaily', 'friends', 'repost', 'nature', 'girl', 'fun',
                'style', 'smile', 'food', 'instalike', 'likeforlike', 'family', 'travel', 'fitness', 'igers', 'tagsforlikes', 'follow4follow',
                'nofilter', 'life', 'beauty', 'amazing', 'instamood', 'instagram', 'photography', 'vscocam', 'sun', 'photo', 'music',
                'beach', 'followforfollow', 'bestoftheday', 'sky', 'ootd', 'sunset', 'dog', 'vsco', 'l4l', 'makeup', 'f4f', 'foodporn',
                'hair', 'pretty', 'swag', 'cat', 'model', 'motivation', 'girls', 'baby', 'party', 'cool', 'lol', 'gym', 'design', 'instapic',
                'funny', 'healthy', 'night', 'tflers', 'yummy', 'flowers', 'lifestyle', 'hot', 'instafood', 'wedding', 'fit', 'handmade',
                'black', 'pink', 'blue', 'work', 'workout', 'blackandwhite' , 'drawing' , 'inspiration' , 'home' , 'holiday' ,
                'christmas' , 'nyc' , 'london' , 'sea' , 'instacool' , 'goodmorning' , 'iphoneonly']

    # Usernames
    famous_usernames = ['selenagomez','leomessi','kyliejenner','beyonce','kendalljenner','cristiano','arianagrande','Instagram',
                                        'instagram','neymarjr','billieeilish','zendaya','shawnmendes','badgalriri','taylorswift','therock',
                                        'virat.kohli','emmawatson','drivetowardsuccess','bussinessdaily','millionare_mentor',
                                        'grayveee','sarcastic_us','lilnasx']


    # Using created functions

    # Logging in
    ig_bot =  InstagramBot('Your_username','Your_password')
    time.sleep(7)

    for i in famous_usernames:
       ig_bot.To_follow_followers_of_celebs(i)
