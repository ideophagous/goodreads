from   selenium                           import webdriver
from   selenium.webdriver.firefox.options import Options
from   selenium.webdriver.common.keys     import Keys
from   bs4                                import BeautifulSoup

EMAIL = '############'
PASSWORD = '#######'

def gr_login(driver):
    username = driver.find_element_by_id("userSignInFormEmail").send_keys(EMAIL)
    print(username)
    password = driver.find_element_by_id("user_password")
    password.send_keys(PASSWORD)
    print(password)
    password.submit()
    #ff = driver.find_element_by_id("u_0_3").click()
    return driver

def get_my_books_page():
    pass

if __name__ == '__main__':
    LINK                    = 'https://www.goodreads.com/'
    options                 = webdriver.ChromeOptions()
    options.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    options.add_argument('--headless')
    driver                  = webdriver.Chrome(chrome_options=options)
    driver.get(LINK)
    soup                    = BeautifulSoup(driver.page_source, 'lxml')
    #print(soup.prettify())
    driver = gr_login(driver)
    soup                    = BeautifulSoup(driver.page_source, 'lxml')
    title                   = soup.find_all('title')[0].text
    print(title)
    driver.quit()
