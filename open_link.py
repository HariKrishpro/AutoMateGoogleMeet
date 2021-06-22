import os
import time
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def _mic_video_off():

    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    # driver.implicitly_wait(4000)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(2000)


def google_sign_in():
    driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgoogle%26rlz%3D1C1CHZN_enIN954IN954%26oq%3Dgoogle%26aqs%3Dchrome..69i57j69i60l3.5807j0j7%26sourceid%3Dchrome%26ie%3DUTF-8&ec=GAZAAQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    driver.find_element_by_id("identifierId").send_keys("temp.for.sign.in.purpose@gmail.com")
    driver.implicitly_wait(2)
    driver.find_element_by_id('identifierNext').click()

def terminate_google():
    os.system("taskkill /f /im chrome.exe ")


def joinNow():
    time.sleep(1)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

def intialise_option():
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument('--start-maximized')
    option.add_argument("user-data-dir=C:\\Users\\krish\\AppData\\Local\\Google\\Chrome\\User Data")
    #   option.add_argument("--profile-directory=Profile 2")
    #   option.add_argument("--disable-extensions")
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 1
    })
    global driver
    driver = webdriver.Chrome(options=option)
    driver.get("https://meet.google.com/cja-erxx-dsw")
    time.sleep(2)
    _mic_video_off()
    joinNow()





i = input("By doing this All Chrome Process with be killed...For Continue Type 'Yes' or 'NO'\n")

if(i.lower().strip() == 'yes'):
    terminate_google()
    schedule.every().day.at("15:36").do(intialise_option)

    while True:
        schedule.run_pending()
        time.sleep(1)


