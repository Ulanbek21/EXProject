                                            # WORKING WITH MULTIPLE WINDOWS [HOW TO SWITCH AND CLOSE AND GETING HANDLE VALUE[ID]]
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://demo.automationtesting.in/Windows.html')
driver.maximize_window()

print(driver.current_window_handle)# # give you handle value of single window which is open currently
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

time.sleep(5)

handles = driver.window_handles # it will give you open all windows handle values
print(handles)

# driver.switch_to.window('') # will help to switch to second window by...
                                                                    # handle value<--will be always uniq handle value
# for handle in handles:
#     driver.switch_to_window(handle)
#     print(driver.title)
#     if driver.title == 'Sakinalium | Home':
#         driver.find_element_by_xpath('//*[@id="container"]/header/div/div/div[2]/ul/li[4]/a').click()
#         print('PASS')
#     else:
#         print('FAILE')

                       #I want to clase windows depens of my chois HOW CAN I DO?
for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title)

    
    if driver.title == 'Sakinalium | Home':
        break
        driver.close() #<-----------will close second window