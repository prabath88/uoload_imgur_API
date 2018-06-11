from flask import Flask
#import urllib.requests
from flask import request, jsonify
from flask import Flask, request, redirect, url_for
import os
from time import gmtime, strftime
import urllib
#from urllib.requests import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 



from imgurpython import ImgurClient
import configparser

import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from time import gmtime, strftime
import configparser

from imgurpython import ImgurClient
from login import login
#import filelist
from datetime import datetime

app = Flask(__name__)
#app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return '''<h1>this is API home</h1>
<p>check the request  request</p>'''

@app.route('/v1/images', methods=['GET'])
def api_my():
    config = configparser.ConfigParser()
    config.read('auth.ini')

    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    client = ImgurClient(client_id, client_secret)
    items = client.get_album_images('5pZ3ISJ')

    myresults = []

    for picc in items:
        myresults.append(picc.link)

    return jsonify({'Uploaded' : myresults})


@app.route('/v1/images/upload', methods=['POST'])
def upload():
    os.system("rm ./pics/* -rf")
    data = request.get_json()
    random_list = data['urls']
    for image_url_down in random_list:
        image_name = strftime("%Y%m%d%H%M%S", gmtime())
        print(image_name)
        image_save = "./pics/"+ image_name +".jpg"
        urllib.urlretrieve(image_url_down, image_save)
    
    job_id = strftime("%Y-%m-%d%H:%M:%S:%Z", gmtime())
    return jsonify({'JOBID':job_id})


#=========================upload===========================================

@app.route('/v1/updatetoimgur', methods=['GET'])
def upload_to_imgur():
    

    id = []

    for root, dirs, files in os.walk("./pics"):
        for pic_path in files:
            pic_path = "./pics/"+ pic_path
            image_path = pic_path

            id.append( UploadPhoto(image_path,['gggg.png'])['id'])

        
    CreateAlbumAndUploadImages('bandualbum','devops',id)
    pass


    return jsonify({'files Upload':'success...!'})


def CreateAlbumAndUploadImages(albumName,albumDescription,images):
    client = logins()
    
    x = {
        'id':'5pZ3ISJ',
        'deletehash': 'rwdf7UfcJwq9Jmg'}

    y = client.album_add_images(x['id'],images)  
    print(y)
    return x
def UploadPhoto(x,images):
    client = logins()
    config = {
        'name':  'image name',

        'title': 'testing',
        'description': 'this is for liq test'}  
    path = x
    image = client.upload_from_path(path, config=config, anon=False)
    print("Done")
    
    return image


    

def logins():
    config = configparser.ConfigParser()
    config.read('auth.ini')

    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    imgur_username = config.get('credentials', 'imgur_username')
    imgur_password = config.get('credentials', 'imgur_password')

    client = ImgurClient(client_id, client_secret)

    authorized_url = client.get_auth_url('pin')
    
    
    driver = webdriver.PhantomJS()
    driver.get(authorized_url)
    

    username = driver.find_element_by_xpath('//*[@id="username"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    username.clear()
    username.send_keys(imgur_username)
    password.send_keys(imgur_password)

    driver.find_element_by_name("allow").click()

    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, 'pin'))
        WebDriverWait(driver,timeout)
        pin_element = driver.find_element_by_id('pin')
        pin = pin_element.get_attribute("value")

    except TimeoutException:
        print("timeout")
    driver.close()

    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
    print("success")
    # print(client)

    return client
#======================================================================================

#app.run()
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
