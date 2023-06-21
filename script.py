import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from oauth2client.service_account import ServiceAccountCredentials
import gspread


# Set the path to your ChromeDriver executable
webdriver_service = Service("chromedriver")#path of the chrome webdriver

# Set up the Chrome options
chrome_options = webdriver.ChromeOptions()
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=webdriver_service)

# Navigate to the website
driver.get("link of the website you want to use")
time.sleep(5) #time intervel betweent two data entry
scopes = [
    'httsp://www.googleapis.com/auth/spreadsheet'
    'httsp://www.googleapis.com/auth/drive'

]
Credentials = ServiceAccountCredentials.from_json_keyfile_name("file name of the authintacitation key of gsheet and gdrive")
file = gspread.authorize(credentials=Credentials)#authintication of the cruidential or api key cheaking
sheet = file.open("data")

sheet = sheet.sheet1   #creating a new sheet
#no you data you want to featch from the website
for i in range(1, 50):

    company_name = driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[1]/div[1]/div[1]/ul/li["+str(i)+"]/a").text 
    print(company_name)
    sheet.update_acell("A"+str(i+1), company_name) #entering data into the google sheet
#before running the code make sure you shared your google sheet into the email give in the google cloud console --> api and servise.


