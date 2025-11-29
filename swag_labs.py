from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SwagLabs(BasePage):
    """
    b. в файле создайте класс SwagLabs
    c. класс не имеет атрибутов, конструктор не требуется
    d. наследуйте класс от класса BasePage
    """

    def exist_icon(self):
        """
        e. Создайте метод exist_icon
        i. метод вызывает метод find_element родительского класса и передает в него локатор locator='div.login_logo'
        f. Для красоты кода воспользуемся конструкцией try except
        """
        try:
            self.find_element_by_css(locator='div.login_logo')
        except NoSuchElementException:
            # ii. except NoSuchElementException: return False
            return False
        return True

    def exist_name(self):
        try:
            self.find_element_by_css(locator='#user-name')
        except NoSuchElementException:
            return False
        return True

    def exist_password(self):
        try:
            self.find_element_by_css(locator='#password')
        except NoSuchElementException:
            return False
        return True
