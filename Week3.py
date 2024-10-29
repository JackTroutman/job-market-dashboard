import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "chromedriver.exe"
# failed/ more complicated URL
#url = "https://en.wikipedia.org/wiki/Main_Page"
url = "https://en.wikipedia.org/wiki/Randomness"

# Set up driver
chrome_options = webdriver.ChromeOptions()
# Headless browser (don't pull up webpage)
# chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
driver.implicitly_wait(10)  # Wait 10 seconds

# Visit target website
driver.get(url)

# failed try later
#hidder_button = driver.find_element(By.XPATH, "//*[@id='p-search']/a")
#driver.implicitly_wait(10)
#hidder_button.click()

#driver.implicitly_wait(10)
#search_bar = driver.find_element(By.ID, "searchInput")
#search_button = driver.find_element(By.XPATH, "//*[@id='searchform']/div/button")
#driver.implicitly_wait(10)
#search_bar.send_keys("Randomness")
#driver.implicitly_wait(10)
#search_button.click()



# random page selection
for counter in range(0,10):
    try:

        # Click on the buttons
        hamburger = driver.find_element(By.ID, "vector-main-menu-dropdown-checkbox")
        random_button = driver.find_element(By.XPATH, "//*[@id='n-randompage']/a")

        hamburger.click()
        driver.implicitly_wait(10)  # This line might not be necessary
        random_button.click()

        # Get the new page title after clicking the random button
        page_name = driver.find_element(By.CLASS_NAME, "mw-page-title-main").text
        print(f'page name: {page_name}')
        print(f'current URL: {driver.current_url}')
        print()

    except:
        print('error')
        print(f'current URL: {driver.current_url}')
        print()
