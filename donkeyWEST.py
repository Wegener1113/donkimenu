from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#不閃退 - 下兩行 + driver = webdriver.Chrome(PATH,options=option)
option = webdriver.ChromeOptions() 
option.add_experimental_option("detach", True) 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=option)

#最多等網頁加載15秒
driver.implicitly_wait(15)

#輸入進入的網站
driver.get("https://restaurant.uberinternal.com/manager/menumaker/7334592c-c294-5058-9e29-7295b1fde5ad/overview")

search = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[3]/form/div/div[1]/input")
#輸入帳號
search.send_keys("wweng")
search.send_keys(Keys.RETURN)

search = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[3]/form/div/div[2]/input")
#輸入密碼
search.send_keys("Whatsupwegener17676")
search.send_keys(Keys.RETURN)

import time
time.sleep(30)

input("輸入驗證碼後按enter繼續執行:")
end = int(input("請輸入要跑幾次:"))

#按菜單
search = driver.find_element(By.ID,"tabs-bui3-tab-3").click() 


# 進入迴圈
namelist=[]
picturelist =[]
discriptionlist =[]
subsectionlist = []
pricelist = []
externalidlist =[]


i = 0

while i < end :
    search = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/button').click()

    picture = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div/input")
    picture.send_keys(picturelist[i])


    discription = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/div/div/div/div/textarea')
    discription.send_keys(discriptionlist[i])

    subsection = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[5]/div[1]/div/div[1]/div/div[2]/div[1]/input")
    subsection.send_keys(subsectionlist[i])
    subsection.send_keys(Keys.RETURN)

    price = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[5]/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/input')
    price.send_keys(pricelist[i])

    tax = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[6]/div/div/div/div/div[1]/input')
    tax.send_keys(Keys.CONTROL, 'a')
    tax.send_keys('0')

    #永久售完
    # soldout = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[8]/div/div/div[1]/div/div/label/span')
    # soldout.click()
    # soldout = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[8]/div/div/div[2]/div/div/label[1]/div[1]')
    # soldout.click()


    button =driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/div').click()

    externalid = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/div[2]/div[3]/div/div[2]/div/div/div/input')
    externalid.send_keys(externalidlist[i])

    #滑鼠轉到網頁最上面
    js = "window.scrollTo(0,0)"
    driver.execute_script(js)
    
    name = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div/header/div/div/div[2]/div/div[1]/div[1]/input')
    name.send_keys(namelist[i])
    
    #顯示程式跑到第幾個品項
    print(namelist[i])

    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div/header/div/div/div[1]/div/button').click()

    time.sleep(7)

    search = driver.find_element(By.ID,"tabs-bui3-tab-3").click() 

    i = i+1




