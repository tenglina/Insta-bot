#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:12:32 2020

@author: nandinitengli
"""

from selenium import webdriver 
import time 

class InstaBot:
    
    def __init__(self, username, Password):
        self.driver = webdriver.Chrome("/Users/nandinitengli/Downloads/chromedriver")
        self.username = username 
        self.Password = Password 
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name= \"username\"]")\
            .send_keys(username)
        
        self.driver.find_element_by_xpath("//input[@name= \"password\"]")\
            .send_keys(Password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]')\
            .click()
        self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]')\
            .click()
    def get_unfollowers (self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username))\
            .click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, 'following')]")\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print (not_following_back)
        
            
        
    def _get_names(self):
        time.sleep(2)
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]');
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        time.sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                 arguments[0].scrollTo(0, arguments[0].scrollHeight);
                 return arguments[0].scrollHeight;
                 """, scroll_box)
        links = scroll_box.find_element_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        print(names)
        # close button for "following" scroll-box 
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button/div/svg")\
            .click()
        return names 
    
    
        
        
            
#creating an instance/calling the bot:
#create and store username and password in respective variables-- username and Password or directly enter username and password as strings when creating an instance of the bot 
bot1 = InstaBot(username, Password)
