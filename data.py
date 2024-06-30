from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os,requests

def getMonthlySunspots():
    try:
        directApiCall()
    except Exception as e:
        print(e)
        webScraper()

def directApiCall():    
    response = requests.get("https://www.sidc.be/SILSO/INFO/snmtotcsv.php")
    print(response.text)
    pass
   
def webScraper(): 
    # Step 1: Set up Chrome options to manage download behavior
    chrome_options = Options()
    download_directory = os.getcwd()  # Replace with your desired download path
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,  # Automatically download without prompt
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Step 2: Initialize the Chrome WebDriver
    service = Service("/path/to/chromedriver")  # Path to your ChromeDriver executable
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Step 3: Navigate to the web page
        driver.get("https://www.sidc.be/SILSO/datafiles")  # Replace with your target URL

        # Step 4: Locate the button and click it
        # Use a suitable selector to find the button
        csv_button = driver.find_element(By.XPATH, "//td/a/button[@class='btn btn-secondary btn-sm' and text()='CSV']")
        csv_button.click()

        # Step 5: Wait for the download to complete
        # This is a simple wait; more sophisticated waits can be implemented
        time.sleep(5)  # Adjust based on expected download time

        # Optionally, verify the file is downloaded
        downloaded_file = os.path.join(download_directory, "expected_filename.csv")  # Replace with expected filename
        if os.path.exists(downloaded_file):
            print(f"File downloaded successfully: {downloaded_file}")
        else:
            print("File download failed or not found.")

    finally:
        # Clean up: Close the browser
        driver.quit()

if __name__=='__main__':
    webScraper()