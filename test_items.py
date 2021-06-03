class TestProductPage:
    def test_guest_should_see_add_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
        assert button, "Кнопка добавления в корзину отсутствует"
