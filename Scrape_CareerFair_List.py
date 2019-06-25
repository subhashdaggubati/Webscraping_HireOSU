# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:29:47 2019

@author: subha
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os


os.chdir('D:\Spring 2019')


driver = webdriver.Chrome("D:\\softwares\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.hireosugrads.com/StudentsAlumni/Event-STEM.aspx")

newrows =[]

#assert "Python" in driver.title
base_xpath_link = "//*[@id=\"EventsEmployerTable\"]/tbody/tr["
tail_xpath_link = "]/td[1]/a"
list_size = len(driver.find_elements_by_xpath("//*[@id=\"EventsEmployerTable\"]/tbody/tr"))
print("list",list_size)
j=0
for j in range(list_size-2):
    print(j)
    if(j<67):
        xpath_link = base_xpath_link + str(j+2) + tail_xpath_link
    else:
        xpath_link = base_xpath_link + str(j+3) + tail_xpath_link
    print(xpath_link)
    elem = driver.find_element_by_xpath(xpath_link)
    window_before = driver.window_handles[0]
    elem.click()
    window_after = driver.window_handles[j+1]
    driver.switch_to_window(window_after)
    length = len(driver.find_elements_by_xpath("/html/body/div[1]/div/table/tbody/tr"))
    base_xpath ="/html/body/div[1]/div/table/tbody/tr["
    tail_xpath="]/th"
    tail_xpath_data = "]/td"
    header = "NA"
    info ="NA"
    row_dic = {}
    for i in range(length):
        xpath=base_xpath+str(i+1)+tail_xpath
        xpath_data=base_xpath+str(i+1)+tail_xpath_data
        th_elem= driver.find_element_by_xpath(xpath)
        td_elem= driver.find_element_by_xpath(xpath_data)
        header = th_elem.text
        info = td_elem.text
        new_row = {header:info}
        row_dic.update(new_row)    
    newrows.append(row_dic)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL +"w")
    driver.switch_to_window(window_before)    
data = pd.DataFrame(newrows)
data.to_csv("Career Fair2.csv")

#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
#usrname = driver.find_element_by_name("Username")
#pwd = driver.find_element_by_name("Password")
#usrname.send_keys(username)
#pwd.send_keys(pwrd)
#sub_button = driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div[1]/button")
#sub_button.click()
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()  