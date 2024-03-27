from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


DEFAULT_URL = "https://fgis.gost.ru/fundmetrology/cm/results?filter_applicability=true&activeYear=%D0%92%D1%81%D0%B5"
PARSING_URL = (
    "https://fgis.gost.ru/fundmetrology/cm/results?"
    "filter_applicability={0}"
    "&filter_mi_mitype={1}"
    "&filter_mi_number={2}"
    "&activeYear=%D0%92%D1%81%D0%B5"
)


class FgisParser:

    def __driver_settings(self) -> webdriver.Chrome:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return driver

    def get_calibration_info(
            self, suitability: bool = True, sensor_type: str = '', sensor_number: str = ''
    ) -> list[list[str]]:
        if sensor_type is None:
            sensor_type = ''
        if sensor_number is None:
            sensor_number = ''

        driver: webdriver.Chrome = self.__driver_settings(self)
        url = PARSING_URL.format(suitability, sensor_type, sensor_number)
        print(url)
        driver.get(url)

        wait = WebDriverWait(driver, 20)

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary"]'))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//tbody/tr')))

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
            raise (f'Информация о поверке не найдена. Ошибка: {e}')
        finally:
            driver.quit()


test_fixture = {
    'self': FgisParser,
    'suitability': True,
    'sensor_type': "ДН-130",
    'sensor_number': 1030,
}

for row in FgisParser.get_calibration_info(**test_fixture):
    print(row)
