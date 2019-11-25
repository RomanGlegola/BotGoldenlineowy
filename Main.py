from Logowanie import wlacz_przegladarke, wejdz_na_strone, komunikat_rodo, logowanie, wyloguj
from SzukanieOfertPracy import szukaj_ofert

driver = wlacz_przegladarke()
wejdz_na_strone(driver)
komunikat_rodo(driver)
logowanie(driver, "login", "haslo")

szukaj_ofert(driver)



# wyloguj(driver)