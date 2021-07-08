import random
import qrcode
from selenium.webdriver import Chrome, ChromeOptions
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


otp=0
def genOTP(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    r = random.randint(100000, 999999)
    global otp
    otp = r
    im = qrcode.make("Your OTP Code is:" + str(r))
    im.save(f"authentication/static/qrcodeimages/{request.user.username}" + ".jpg")
    print(otp)
    #create otp file
    file=f"authentication/static/otp/{request.user.username}-otp.txt"
    with open(file,'w') as f:
        f.write(str(otp))
        print(f.name)

def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.3)
