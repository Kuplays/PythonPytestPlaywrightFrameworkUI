class BasicPage:
    """
    Basic Page for any tests with given application. Place any application-wide methods which are true for every page.
    """
    def __init__(self, page, base_url):
        """
        Initialization method
        :param page: pass a fixture of a page here
        :param base_url: basic url for constructing more complex ones. Pass as a fixture
        """
        self.page = page
        self.base_url = base_url

    def go_to(self, path: str = "/") -> None:
        """
        Redirect method to access different pages
        :param path: other resources locations that is specified as /some-other-resource
        :return:
        """
        self.page.goto(self.base_url + path)

    def click(self, selector: str) -> None:
        """
        Performs click interaction within a page. Using playwright click mechanism
        :param selector: pass any string css selector as a parameter
        :return:
        """
        self.page.click(selector)

    def fill(self, selector: str, text: str) -> None:
        """
        Performs fill operation with input fields that supports this action.
        :param selector: CSS selector of an input
        :param text: text to fill in
        :return:
        """
        self.page.fill(selector, text)

    def get_inner_text(self, selector: str) -> str:
        """
        Returns an inner text of a given page element
        :param selector: CSS selector
        :return:
        """
        return self.page.inner_text(selector)

    def is_visible(self, selector: str) -> bool:
        """
        Returns a state of an element if it is visible or not
        :param selector: CSS selector
        :return: True if visible, False otherwise
        """
        return self.page.is_visible(selector)
