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

driver.get("https://restaurant.uberinternal.com/manager/menumaker/7334592c-c294-5058-9e29-7295b1fde5ad/overview")

search = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[3]/form/div/div[1]/input")
search.send_keys("wweng")
search.send_keys(Keys.RETURN)

search = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[3]/form/div/div[2]/input")
search.send_keys("Whatsupwegener17676")
search.send_keys(Keys.RETURN)

import time
time.sleep(30)

input("輸入驗證碼後按enter繼續執行:")
end = int(input("請輸入要跑幾次:"))

#按菜單
search = driver.find_element(By.ID,"tabs-bui3-tab-3").click() 


# 進入迴圈
namelist=['Honyaradoh 溫感晚安眼膜 白麝香(附白麝香精油膠囊) 3枚入 @18 @4991936385070','Honyaradoh 限定版溫感眼膜 银荆 3枚入 @18 @4991936385285','DONKI 3用 USB充電線 黑 2m @12 @4549777108343','SK JAPAN 星之卡比 閃亮亮沐浴球 N 1入 @15 @4544815060904','BANDAI 麵包超人大家的好朋友篇入浴球 1個 @15 @4549660318774','Minimo 貓妖精逗貓棒 白精靈 @15 @4580471868027','CIAO 啾嚕肉泥(鮪魚+海膽+鰹魚+雞肉)  14g x4入 @15 @4901133354205','CIAO 啾嚕肉泥(鮪魚) 14g x4入 @15 @4901133716577','CIAO 啾嚕肉泥-下部尿路配慮(鮪魚)  14g x4入 @15 @4901133718830','CIAO 啾嚕肉泥-電解質水分補給(鮪魚) 14g x4入 @15 @4901133719387','Q-PET巧沛 御貓-胺基酸泌尿道保健雞丁 30g @15 @4941605020580','Q-PET巧沛 御貓-胺基酸皮毛保健雞丁 30g @15 @4941605020597','Q-PET巧沛 御貓-胺基酸腸道保健雞丁 30g @15 @4941605020603','情熱價格 可折疊水桶 7.5L @16 @4545244547974','DONKI 防脫落衣架(顏色隨機出貨) 10入 @16 @4549777512355','情熱價格 坐墊(黑/藍/綠/卡其色隨機出貨) @16 @4549777512775','DONKI Donpen.Donko 手帕 1入 @16 @4967213156411','DONKI Donpen.Donko 手帕 1入 @16 @4967213156428','Pearl 大蒜削皮器 @16 @4976790203159','超快適 長時間舒適安心醫療口罩 S紫 5枚入 @18 @4710054861026','超快適 長時間舒適安心醫療口罩 M黑 5枚入 @18 @4710054861132','小林製藥 退熱貼(未滅菌)-嬰兒用 6枚入 @18 @4987072003718','小林製藥 退熱貼(未滅菌)-成人用 6枚入 @18 @4987072008676','小林製藥 退熱貼(未滅菌)-兒童用 6枚入 @18 @4987072008683','Honyaradoh 溫感熱敷眼膜薰衣草香(狐狸/兔子/熊各2枚) 6枚入 @18 @4991936384622','Honyaradoh 溫感眼膜(花香/薰衣草/白麝香各2) 6枚入 @18 @4991936385124','阿根廷红蝦(8L20尾入)(生食級） 400g @02 @4515316007392','北海道産冷凍干貝4S(生食級） 1盒 @02 @4582378421015','北海道産醤油調味鯡魚卵 120g @02 @4993578961155']
picturelist=['C:/Users/wweng/Desktop/donkey upload/圖檔/4991936385070.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4991936385285.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4549777108343.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4544815060904.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4549660318774.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4580471868027.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4901133354205.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4901133716577.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4901133718830.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4901133719387.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4941605020580.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4941605020597.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4941605020603.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4545244547974.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4549777512355.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4549777512775.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4967213156411.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4967213156428.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4976790203159.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4710054861026.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4710054861132.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4987072003718.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4987072008676.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4987072008683.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4991936384622.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4991936385124.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4515316007392.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4582378421015.jpg','C:/Users/wweng/Desktop/donkey upload/圖檔/4993578961155.jpg']
discriptionlist=['※本商品出貨時有效期限大於365天。※若屬進口商品多數有效期限較短，敬請見諒。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品出貨時有效期限大於365天。※若屬進口商品多數有效期限較短，敬請見諒。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','尺寸約為40x40x3.5cm。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','約25x25cm。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','約25x25cm。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品出貨時有效期限大於365天。※若屬進口商品多數有效期限較短，敬請見諒。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品出貨時有效期限大於365天。※若屬進口商品多數有效期限較短，敬請見諒。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品出貨時有效期限大於365天。※若屬進口商品多數有效期限較短，敬請見諒。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品出貨時有效期限大於365天。※若屬進口商品多數有效期限較短，敬請見諒。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品出貨時有效期限大於365天。※若屬進口商品多數有效期限較短，敬請見諒。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品出貨時有效期限大於365天。※若屬進口商品多數有效期限較短，敬請見諒。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品出貨時有效期限大於365天。※若屬進口商品多數有效期限較短，敬請見諒。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品為冷凍商品。※原產地：阿根廷。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品為冷凍商品。※原產地：日本北海道。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。','※本商品為冷凍商品。※原產地：日本北海道。※商品成分與適用注意事項，製造日期與有效期限皆標示於包裝或產品中。※本產品網頁因拍攝關係，圖檔略有差異，實際以出貨為主。※本產品文案若有變動敬請參照實際商品為準。']
subsectionlist=['蒸氣眼罩','蒸氣眼罩','充電傳輸線','泡澡入浴劑','泡澡入浴劑','寵物用品','貓食','貓食','貓食','貓食','貓食','貓食','貓食','家用清潔用品','衣物洗滌','枕頭/坐墊','毛巾浴巾織品','毛巾浴巾織品','料理用具','口罩','口罩','冷暖敷具','冷暖敷具','冷暖敷具','蒸氣眼罩','蒸氣眼罩','冷凍海鮮','冷凍海鮮','冷凍海鮮製品']
pricelist=['189','189','329','180','160','179','89','79','89','89','115','115','115','299','289','288','109','109','199','59','59','149','149','149','290','290','980','2380','598']
externalidlist=['4991936385070','4991936385285','4549777108343','4544815060904','4549660318774','4580471868027','4901133354205','4901133716577','4901133718830','4901133719387','4941605020580','4941605020597','4941605020603','4545244547974','4549777512355','4549777512775','4967213156411','4967213156428','4976790203159','4710054861026','4710054861132','4987072003718','4987072008676','4987072008683','4991936384622','4991936385124','4515316007392','4582378421015','4993578961155']

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




