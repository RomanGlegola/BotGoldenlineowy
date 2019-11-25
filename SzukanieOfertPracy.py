
def szukaj_ofert(driver):
    lista = [
        "test",
        "tester",
        "tester+manual",
        "quality+assurance"
    ]

    for i in lista:
        from Logowanie import wejdz_na_strone
        driver.get("https://www.goldenline.pl/praca/szukaj?query="+i)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        from selenium.webdriver.common.by import By
        # print("sdo "+str(driver.find_elements(By.CLASS_NAME, "stats-data-offer")))
        zapisz_linki(
            driver.find_elements(By.CLASS_NAME, "cell.content"), "oferty_pracy.txt")


def zapisz_linki(linki, plik):
    with open("BazaDanych/"+plik, "a") as spis_linkow:

        for odnosnik in linki:
            opis_odnosnika = str(odnosnik.get_attribute("href"))
            if "?engine=datumo&context=work-listing" in opis_odnosnika:
                pass
            else:
                print(opis_odnosnika)
                spis_linkow.writelines(opis_odnosnika + "\n")
