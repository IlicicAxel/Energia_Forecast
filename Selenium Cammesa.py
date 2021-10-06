from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
    
# Pagina de Cammesa
server_endpoint = "https://microfe.cammesa.com/demandaregionchart/#/operaciones"
# PATH de guardado
local_file_path = "C:\\Users\\ilici\\Documents\\Cammesa\\"

def regiones_csv (server_endpoint, local_file_path):
    options = Options()
    options.add_experimental_option("prefs", {
      "download.default_directory": local_file_path,
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome(('C:/Users/ilici/AppData/Local/SeleniumBasic/chromedriver'), options= options)
    driver.get(server_endpoint)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="btnCsv"]/div').click()
    for i in range(1,10):
        driver.find_element_by_xpath('/html/body/app-root/app-single-selection/div/div/div[1]/div[2]/dx-drop-down-box/div[1]/div/div[2]/div[2]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div/dx-tree-view/div[2]/div/div/div[1]/ul/li/ul/li["+str(i)+"]/div[1]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="btnCsv"]/div').click()
        time.sleep(1)
        print("Status: Download Complete "+str(i))
    time.sleep(2)    
    driver.quit()
            
regiones_csv(server_endpoint, local_file_path)