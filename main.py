from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
import random

with open('messages.txt','r',encoding='utf-8') as messages:
    messagelist = []
    text = messages.read()
    messagelist = text.split('\n')

def start():
    
    driver = webdriver.Firefox()
    # Acilmazsa hemen hata verme 3 saniye bekle
    driver.implicitly_wait(12123)
    driver.get('https://web.whatsapp.com/')
    input('QR  kodu okuttuysaniz bir tusa basip enterlayin')
    message_area = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    while True:
        message_area.click()
        wp_source = driver.page_source
        soup = bs(wp_source, 'lxml')
        search = soup.find_all('div',{'class':['zzgSd' , '_3e6xi']})
        try:
            online = search[0].span.text
            print(online)
            if (online in (["çevrimiçi","online"])):
                print('online')
                msgToSend = messagelist[random.randint(0,len(messagelist)-1)]
                message_area.send_keys(msgToSend)
                message_area.send_keys(Keys.ENTER)
                
            elif online not in ["çevrimiçi","online"]:
                print('suanda cevrimdisi')
        except:
            print('Su an da cevrimdisi')
            flag = False

       





start()
