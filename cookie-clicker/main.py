import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

upgrade_list = []
upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")
for upgrade in upgrades:
    upgrade_details = upgrade.text.split(" -")
    if len(upgrade_details) == 2:
        name = upgrade_details[0]
        cost = upgrade_details[1].strip(' ').replace(',','')
        upgrade_list.append([name, cost])

bought_list = []

def check_upgrade():
    money = int(driver.find_element(By.ID, "money").text.replace(',',''))
    global upgrade_to_buy
    for upgrade in upgrade_list:
            if int(upgrade[1]) < money:
                upgrade_to_buy = upgrade[0]
    return upgrade_to_buy


def upgrade():
    upgrade_to_buy = check_upgrade()
    buying_upgrade = driver.find_element(By.ID, f"buy{upgrade_to_buy}")
    buying_upgrade.click()

game_start = time.time()
game_end = game_start + 60 * 5
check = game_start + 5
while time.time() < game_end:
    cookie.click()
    if time.time() >= check:
        upgrade()
        check = time.time() + 5
cookies_per_second = driver.find_element(By.ID, "cps").text.split(":")[1].strip()
print(f"Cookies per second: {cookies_per_second}")
driver.close()
