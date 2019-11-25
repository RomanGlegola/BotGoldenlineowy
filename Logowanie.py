from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


def wlacz_przegladarke():
    return webdriver.Chrome(
        "Przegladarka/chromedriver.exe")


def wejdz_na_strone(driver, strona="https://www.goldenline.pl/"):
    driver.get(
        strona)


def komunikat_rodo(driver):
    from selenium.webdriver.common.by import By
    from time import sleep
    sleep(3)
    if driver.find_element(By.XPATH,
                           "/html/body/div/div/div[5]/div[2]/div[4]/form/button"):
        driver.find_element(By.XPATH,
                            "/html/body/div/div/div[5]/div[2]/div[1]/div/button/div[2]"). \
            click()


def logowanie(driver, login, haslo):
    from selenium.webdriver.common.by import By
    # Klikamy Zaloguj się
    driver.find_element(By.XPATH,
                        "/html/body/div/div/div[2]/header/div/div[4]/nav/div[1]/a"). \
        click()
    # Wpisujemy login
    driver.find_element(By.ID,
                        "login"). \
        send_keys(login)
    # Wpisujemy hasło
    driver.find_element(By.ID,
                        "passwd"). \
        send_keys(haslo)
    # Wciskamy enter
    driver.find_element(By.ID,
                        "passwd"). \
        send_keys(Keys.ENTER)


def wyloguj(driver):
    wejdz_na_strone(driver,
        "https://www.goldenline.pl/wylogowanie")
    driver.close()
