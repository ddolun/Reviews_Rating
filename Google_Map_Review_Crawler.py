from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
import csv
driver = webdriver.Chrome('D:\vscode\python\chromedriver')
url = input('請輸入網址:')
file = open('data37.csv',mode='a', newline='',encoding=('UTF-8'))
headerList = ['Name','Stars','Reviews','Image','Date','numofreviews','ckipnlp','score','modelscore','sub_score']
writer = csv.DictWriter(file,fieldnames=headerList)
writer.writeheader()
image = ''
image_b = 'N'
if image_b != 'Y' and image_b != 'N':
    print('翻開覆蓋的陷阱卡')
    time.sleep(5)
    sys.exit()
driver.get(url)
driver.implicitly_wait(5)

more_review_button = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]')
more_review_button.click()
SCROLL_PAUSE_TIME = 1

sort_button = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[7]/div[2]/button')

sort_button.click()
new_button = driver.find_element(By.XPATH,'//*[@id="action-menu"]/div[2]')
time.sleep(1)
new_button.click()


# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

number = 0
while True:
    number = number+1
    
    # Scroll down to bottom
    
    ele = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]')
    driver.execute_script('arguments[0].scrollBy(0, 5000);', ele)
    
    # Wait to load page

    
    time.sleep(SCROLL_PAUSE_TIME)
    
    # Calculate new scroll height and compare with last scroll height
    # print(f'last height: {last_height}')

    ele = driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]')

    new_height = driver.execute_script("return arguments[0].scrollHeight", ele)

    # print(f'new height: {new_height}')

    if last_height == new_height:
        count = count+1
    else:
        count = 0
    if count == 2:
        break

    # print('cont')
    last_height = new_height



full_button = driver.find_elements(By.CLASS_NAME,'w8nwRe.kyuRq')
for fb in full_button:
    fb.click()
reviews = driver.find_elements(By.CLASS_NAME,'jftiEf.fontBodyMedium')
element = driver.find_elements(By.XPATH,'//span[@class="wiI7pd"]')
stars = driver.find_elements(By.CLASS_NAME,'kvMYJc')
names = driver.find_elements(By.CLASS_NAME,'d4r55')
date = driver.find_elements(By.CLASS_NAME,'rsqaWe')
numofreviews = driver.find_elements(By.CLASS_NAME,'RfnDt')
div = driver.find_elements(By.CLASS_NAME,'KtCyie')
count = 0
for e , s , n , r , d , nor  in zip(element,stars,names,reviews,date,numofreviews):
    if image_b == 'Y':
        # try:
            if div[count].size != 0:
                try:
                    r.find_element(By.CLASS_NAME,'Tya61d')
                    count = count + 1
                    image = 'Y'
                except:
                    image = 'N'
    print(n.text)
    print(s.get_attribute('aria-label'))
    print(e.text)
    print(nor.text)
    if image_b == 'Y':
        print(image)
    if d.text == '3 年前':
        break
    print(d.text)
    writer.writerow({'Name': n.text ,'Stars': s.get_attribute('aria-label'),'Reviews': (e.text).replace('\n',''),'Image': image, 'Date' : d.text,'numofreviews' : nor.text})
    print('\n')
print('J素')
file.close()
driver.quit()
time.sleep(2)
sys.exit()