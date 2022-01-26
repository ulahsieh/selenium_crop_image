from PIL import Image
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("開始爬取")

if __name__ == "__main__":
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('lang=zh_TW.UTF-8')
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.set_window_size(1400, 1500) # 設定視窗大小
    
    driver.get("https://www.selenium.dev/projects/")
    time.sleep(1)

    driver.save_screenshot("./scrnsht.png")

    # crop curve table only
    ele = driver.find_elements_by_xpath("/html/body/div/main/div[1]/div")

    left = ele[0].location['x']
    top = ele[0].location['y']
    right = left + ele[0].size['width']
    bottom = top + ele[0].size['height']

    im = Image.open("./scrnsht.png")
    im = im.crop((left, top, right, bottom))
    im.save("./crop.png")

    driver.quit()

print("爬取完成")
