# please download selenium driver for your os, (this code was developed for macOS, that is the driver that you find in this repo)

keep in mind that you must select according to your browser version

https://sites.google.com/a/chromium.org/chromedriver/downloads

# set virtual enviroment

python3 -m venv selenium-test  

# activate eviroment with

source folder-for-enviroment/bin/activate

# when you're done type

deactivate

# install dependencys with 

python3 -m pip install -r requirements.txt

# for gettin html of the page execute 

python obtain-img-html.py

# for getting pdf from html execute

python obtain-pdf.py
