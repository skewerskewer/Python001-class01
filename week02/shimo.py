from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/welcome')
    # browser.find_element_by_xpath('//button[@class="login-button btn_hover_style_8"]').click()
    # click login button at https://shimo.im/welcome
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/header/nav/div[3]/a[2]/button').click()
    browser.find_element_by_xpath('//input[@type="text"]').send_keys('334334343@qq.com')
    browser.find_element_by_xpath('//input[@type="password"]').send_keys('1239')
    # browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()
    # click login instantly at https://shimo.im/login?from=home
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    cookies = browser.get_cookies()
    print(cookies)

except Exception as e:
    print(e)
finally:    
    browser.close()

# try:
    
#     # 需要安装chrome driver, 和浏览器版本保持一致
#     # http://chromedriver.storage.googleapis.com/index.html
    
#     browser.get('https://www.douban.com')
#     time.sleep(1)

#     browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
#     btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
#     btm1.click()

#     browser.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
#     browser.find_element_by_id('password').send_keys('test123test456')
#     time.sleep(1)
#     browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()

#     cookies = browser.get_cookies() # 获取cookies
#     print(cookies)
#     time.sleep(3)

# except Exception as e:
#     print(e)
# finally:    
#     browser.close()


