from utils import scrap_op as scrap
import os

screen_path = "Screenshots\\"
os.makedirs("Screenshots", exist_ok=True)

driver = scrap.init_driver()
with open("student_urls.txt") as f:
    urls = f.readlines()
for url in urls[:3]:
    print(url.strip().replace("http://", "").replace("/", ""))

    # scrap.save_screenshot(driver, url, save_path)
    driver.get(url)
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(total_width, total_height)
    file_path = screen_path + url.strip().replace("http://", "").replace("/", "") + ".png"
    print(file_path)
    driver.save_screenshot(file_path)


scrap.close_driver(driver)


