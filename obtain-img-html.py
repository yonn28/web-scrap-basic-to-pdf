import random
from time import sleep
from selenium import webdriver
from xhtml2pdf import pisa
import requests # to get image from the web
import shutil # to save it locally
import os

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.oreilly.com/member/login/?next=%2Fapi%2Fv1%2Fauth%2Fopenid%2Fauthorize%2F%3Fclient_id%3D235442%26redirect_uri%3Dhttps%3A%2F%2Flearning.oreilly.com%2Fcomplete%2Funified%2F%26state%3DD7qyJpyBD2zQOiMkvHaZW2QAqCX5L90w%26response_type%3Dcode%26scope%3Dopenid%2Bprofile%2Bemail&locale=en')


#user
sleep(random.uniform(8.0, 10.0))
email = driver.find_element_by_xpath('/html/body/div[1]/main/section/div[1]/form/div[1]/label/input')
email.send_keys('')
#password
sleep(random.uniform(8.0, 10.0))
password = driver.find_element_by_xpath('/html/body/div[1]/main/section/div[1]/form/div[3]/label/input')
password.send_keys('')

singinBtn = driver.find_element_by_xpath('//*[@id="main"]/section/div[1]/form/button[2]')
singinBtn.click()
sleep(random.uniform(8.0, 10.0))


driver.get('')

for i in list(range(30,32)):
    pages = driver.find_elements_by_id('sbo-rt-content')
    images = pages[0].find_elements_by_tag_name('img')
    for img in images:
        image_url = img.get_attribute('src')
        filename = image_url.split("/")[-1]
        r = requests.get(image_url, stream = True)
    
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',filename)
        else:
            print('Image Couldn\'t be retreived')

    dataHtml = pages[0].get_attribute('innerHTML')
    Html_file= open(f'output{i}.html',"w")
    Html_file.write(dataHtml)
    Html_file.close()
    nextBtn = driver.find_element_by_xpath('//*[@id="container"]/div[2]/section/div[2]/a')
    nextBtn.click()
    sleep(random.uniform(8.0, 10.0))




