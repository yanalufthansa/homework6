import pytest
from selenium.common.exceptions import NoSuchElementException


class TestSwagLabs:

    def test_check_icon(self, swag_labs):
        """
        6. реализуйте тест кейс
        a. в файле test_check_swag.py реализуйте следующий тест кейс:
        i. перейти на страницу https://www.saucedemo.com/
        ii. проверить наличие иконки
        """
        swag_labs.visit()
        print("Перешли на страницу https://www.saucedemo.com/")

        # ii. проверить наличие иконки
        icon_exists = swag_labs.exist_icon()
        assert icon_exists, "Иконка не найдена на странице"

    def test_check_username_field(self, swag_labs, driver):
        """
        7. реализуйте тест кейс
        a. в файле test_check_swag.py реализуйте следующий тест кейс:
        i. перейти на страницу https://www.saucedemo.com/
        ii. проверить наличие поля имени.
        """

        # i. перейти на страницу
        swag_labs.visit()

        # ii. проверить наличие поля имени
        try:
            username_field = swag_labs.exist_name()
            assert username_field is not None, "Поле имени не найдено"

        except NoSuchElementException:
            pytest.fail("Поле имени не найдено на странице")

    def test_check_password_field(self, swag_labs, driver):
        """
        8. реализуйте тест кейс
        a. в файле test_check_swag.py реализуйте следующий тест кейс:
        i. перейти на страницу https://www.saucedemo.com/
        ii. проверить наличие поля пароля
        """

        # i. перейти на страницу
        swag_labs.visit()
        print("Перешли на страницу https://www.saucedemo.com/")

        # ii. проверить наличие поля пароля
        try:
            password_field = swag_labs.exist_password()
            assert password_field is not None, "Поле пароля не найдено"

        except NoSuchElementException:
            pytest.fail("Поле пароля не найдено на странице")
