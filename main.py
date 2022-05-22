from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")


def main(headless=True):
    # Give the exact path of the chromedriver.exe
    if headless:
        driver = webdriver.Chrome('chromedriver.exe', options=options)
    else:
        driver = webdriver.Chrome('chromedriver.exe')
    url = "Enter URL to search" # Enter correct url
    driver.get(url)
    print('Message to print(Succesful)')
    
    # If you are using doing some kind of login then you can use the following code.
    username = driver.find_element_by_id("username")  # Your id may be different. Inspect the page to get the id.
    password = driver.find_element_by_id("password")
    USERNAME = "your username to enter"
    PASSWORD = "Your password"
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    # You can also use the click() function to click on some element
    driver.find_element_by_id("loginbtn").click()
    print("Logged IN..")
    
    driver.quit() # To exit and close chrome.
   
          
main()  # Specify flase to open chrome
