import random
from time import sleep
from selenium import webdriver
from xhtml2pdf import pisa
import requests # to get image from the web
import shutil # to save it locally
import os

driver = webdriver.Chrome('./chromedriver')
# url login
driver.get('')


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

# url to scrap
driver.get('')

for i in list(range(8,13)):
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
    styles = driver.find_elements_by_tag_name('style')
    style = ''
    for st in styles:
        style += st.get_attribute('innerHTML')
    
    html_to_write = f'<!DOCTYPE html> <html lang="en"> <head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><style>{style}</style><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><div id="sbo-rt-content">{dataHtml}</div></body></html>'
    Html_file= open(f'output{i}.html',"w")
    Html_file.write(html_to_write)
    Html_file.close()
    nextBtn = driver.find_element_by_xpath('//*[@id="container"]/div[2]/section/div[2]/a')
    nextBtn.click()
    sleep(random.uniform(8.0, 10.0))

driver.quit()


