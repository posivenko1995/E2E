from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("https://www.saucedemo.com/")
imput_username = browser.find_element(By.XPATH,'//*[@id="user-name"]')
imput_username.send_keys('standard_user')
imput_password = browser.find_element(By.XPATH,'//*[@id="password"]')
imput_password.send_keys('secret_sauce')
click_login = browser.find_element(By.XPATH,'//*[@id="login-button"]').click()
browser.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
browser.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
testcart  = browser.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div').text
testcart1 = 'Sauce Labs Backpack'
def test_additemcart():
        assert testcart == testcart
browser.find_element(By.XPATH,'//*[@id="checkout"]').click()
imput_firstname = browser.find_element(By.XPATH,'//*[@id="first-name"]')
imput_firstname.send_keys('Андрей')
imput_lasttname = browser.find_element(By.XPATH,'//*[@id="last-name"]')
imput_lasttname.send_keys('Посивенко')
imput_zippostalcode = browser.find_element(By.XPATH,'//*[@id="postal-code"]')
imput_zippostalcode.send_keys('12345')
browser.find_element(By.XPATH,'//*[@id="continue"]').click()
browser.find_element(By.XPATH,'//*[@id="finish"]').click()
testorder  = browser.find_element(By.XPATH,'//*[@id="checkout_complete_container"]/h2').text
testorder1 = 'Thank you for your order!'
def test_successfulorder ():
    assert testorder == testorder1











