# Stepik TASK: Different interface languages

# INSTRUCTION:
# You may use any language, that are in 'languages' dictionary (e.g.: 'en-gb', 'uk', 'es')
#    pytest -sv --language=uk test_items.py
# Also ypu may use different browsers ('chrome' or 'firefox'). By default is used 'chrome' browser.
#    pytest -sv --browser_name=firefox --language=uk test_items.py
# By running script without '-sv' arguments will show the result, without showing 'print()' outputs in terminal
#    pytest --language=uk test_items.py

# Dependencies
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Test class
class TestsDifferentInterfaceLanguages(object):
    def test_different_interface_languages(self, browser, request) -> None:
        try:
            # ARRANGE
            # Variables
            link: str = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
            languages = {'ar':'أضف الى سلة التسوق',
                         'ca':'Afegeix a la cistella',
                         'cs':'Vložit do košíku',
                         'da':'Læg i kurv',
                         'de':'In Warenkorb legen',
                         'en-gb':'Add to basket',
                         'el':'Προσθήκη στο καλάθι',
                         'es':'Añadir al carrito',
                         'fi':'Lisää koriin',
                         'fr':'Ajouter au panier',
                         'it':'Aggiungi al carrello',
                         'ko':'장바구니 담기',
                         'nl':'Voeg aan winkelmand toe',
                         'pl':'Dodaj do koszyka',
                         'pt':'Adicionar ao carrinho',
                         'pt-br':'Adicionar à cesta',
                         'ro':'Adauga in cos',
                         'ru':'Добавить в корзину',
                         'sk':'Pridať do košíka',
                         'uk':'Додати в кошик',
                         'zh-hans':'Add to basket'}
            user_language = request.config.getoption("language")
            
            # ACT
            # Opening link in browser
            browser.get(link)
            
            # ASSERT
            # Actual and expected variables
            actualAnswer = WebDriverWait(browser, 10) \
                .until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket"))).text
            expectedAnswer = languages[user_language]

        finally:
            # FOR STEPIK PRESENTATION ON GITHUB ONLY!
            # FOR REAL TESTs, IT's NOT A GOOD PRACTICE TO USE SLEEPs!
            time.sleep(30)

            # Show the result in terminal (e.g. for debug mode)
            print(f"\n\tFor [ {user_language} ] correct button name is [ {languages[user_language]} ]\n")

        # Verification that actual result is as expected
        assert actualAnswer == expectedAnswer, \
            f"\n  Actual result: {actualAnswer}\n   didn't mutch\nExprcted result: {expectedAnswer}"
