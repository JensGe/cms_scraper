from utils import scrap_op as scrap

driver = scrap.init_driver()

soup = scrap.get_soup_from_url(driver, "http://cms-ss19.co.nf")



driver.close_driver()
