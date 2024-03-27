from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def get_calibration_info(
        suitability: bool = True,
        sensor_type: str = '',
        sensor_number: str = '',
     ):
    if sensor_type is None:
        sensor_type = ''
    if sensor_number is None:
        sensor_number = ''
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)

    url = f"https://fgis.gost.ru/fundmetrology/cm/results?filter_applicability={suitability}&filter_mi_mitype={sensor_type}&filter_mi_number={sensor_number}&activeYear=%D0%92%D1%81%D0%B5"
    # url = f"https://fgis.gost.ru/fundmetrology/cm/results?filter_applicability=true&activeYear=%D0%92%D1%81%D0%B5"
    driver.get(url)

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary"]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//tbody/tr')))
        # sleep(5)

        table_rows = driver.find_elements(By.XPATH, '//tbody/tr')

        calibration_dates = [
            ['Дата', 'Организация', 'Тип СИ', 'Заводской номер']
        ]
        for row in table_rows:
            organization_element = row.find_element(By.XPATH, './td[1]')
            ci_element = row.find_element(By.XPATH, './td[4]')
            ci_number = row.find_element(By.XPATH, './td[6]')
            calibration_date_element = row.find_element(By.XPATH, './td[7]')
            calibration_dates.append(
                [
                    calibration_date_element.text,
                    organization_element.text,
                    ci_element.text,
                    ci_number.text
                ]
            )

        return calibration_dates
    except Exception as e:
        print("Информация о поверке не найдена.")
        raise e
    finally:
        driver.quit()


suitability = True
sensor_type = "ДН-130"
# sensor_type = ""
# sensor_type = None
sensor_number = None

for row in get_calibration_info(suitability, sensor_type, sensor_number):
    if row[0] == '':
        continue
    print(row)
