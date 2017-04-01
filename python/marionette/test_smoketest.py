from selenium import webdriver

def test_smoketest():
    driver = webdriver.Firefox(
        executable_path="/Users/wwu/Desktop/geckodriver",
    )
    driver.get('http://www.google.com')
    driver.quit()
