from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        """
        c. При инициализации у класса есть 2 атрибута:
        i. driver - принимается в качестве аргумента
        ii. base_url - не принимается, установлен значение по умолчанию, "https://www.saucedemo.com/"
        """
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"

    def visit(self):
        """
        d. Создайте метод visit который возвращает переход на страницу (.get())
        """
        return self.driver.get(self.base_url)

    def find_element_by_css(self, locator):
        """
        e. Создайте метод find_element
        i. метод принимает аргумент locator
        ii. возвращает поиск элемента (find_element())
        """

        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def find_element_by_xpath(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def find_element_by_id(self, locator):
        return self.driver.find_element(By.ID, locator)

    def find_element_by_class_name(self, locator):
        return self.driver.find_element(By.CLASS_NAME, locator)

    def get_text(self, locator):
        """
        1. в классе компонентов создайте метод для получения текста с элементов get_text(self).
        текст из элемента cчитывайте так str(self.find_element().text)
        """
        element = self.find_element_by_css(locator)
        return str(element.text)
