import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from oauth2client.service_account import ServiceAccountCredentials
import gspread


# Set the path to your ChromeDriver executable
webdriver_service = Service("chromedriver")

# Set up the Chrome options
chrome_options = webdriver.ChromeOptions()
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=webdriver_service)

# Navigate to the website
driver.get("https://dhan.co/all-stocks-list/")
time.sleep(5)
scopes = [
    'httsp://www.googleapis.com/auth/spreadsheet'
    'httsp://www.googleapis.com/auth/drive'

]
Credentials = ServiceAccountCredentials.from_json_keyfile_name("auth.json")
file = gspread.authorize(credentials=Credentials)
sheet = file.open("data")

sheet = sheet.sheet1
for i in range(1, 50):

    company_name = driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[1]/div[1]/div[1]/ul/li["+str(i)+"]/a").text
    print(company_name)
    sheet.update_acell("A"+str(i+1), company_name)


