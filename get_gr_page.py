from   selenium                           import webdriver
from   selenium.webdriver.firefox.options import Options
from   selenium.webdriver.common.keys     import Keys
from   bs4                                import BeautifulSoup

EMAIL    = '############'
PASSWORD = '############'
LINK     = 'https://www.goodreads.com/'

def load_access():
    with open('access.txt','r') as ac:
        data       = ac.read()
        data_parts = data.split('\n')
        EMAIL      = data_parts[0].strip()
        PASSWORD   = data_parts[1].strip()

    return EMAIL,PASSWORD

def gr_login(driver):
    EMAIL,PASSWORD = load_access()
    username       = driver.find_element_by_id("userSignInFormEmail").send_keys(EMAIL)
    #print(username)
    password       = driver.find_element_by_id("user_password")
    password.send_keys(PASSWORD)
    #print(password)
    password.submit()
    #ff = driver.find_element_by_id("u_0_3").click()
    return driver

def get_my_books_page():
    pass

if __name__ == '__main__':
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
    print('Title: '+str(title))
    driver.quit()
