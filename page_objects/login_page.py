import allure
from page_objects.basic_page import BasicPage


class LoginPage(BasicPage):
    """
    Class for login page. Utilizes basic functionality of a BasicPage class
    """

    """
    CSS Locators=====================================
    """
    user_name_input = '#user-name' # login input field
    user_password_input = '#password' # password input field
    login_btn = '#login-button' # login button
    """
    =================================================
    """

    @allure.step("Redirect to the main page at login")
    def go_to(self) -> None:
        """
        Opens up login page. Same as go_to basic_url. Just for clarity
        :return:
        """
        super().go_to(path="/")

    @allure.step("Perform login operation with username and password")
    def login(self, username: str, password: str) -> None:
        """
        Performs a login operation
        :param username: pass a username
        :param password: pass a password
        :return:
        """
        self.fill(self.user_name_input, username)
        self.fill(self.user_password_input, password)
        self.click(self.login_btn)