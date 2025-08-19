import allure
from page_objects.basic_page import BasicPage

class InventoryPage(BasicPage):
    """
    Class for Inventory page related actions
    """

    """
    CSS Locators=====================================
    """
    inventory_item_name_list = '[data-test="inventory-item-name"]' # list of all items names
    inventory_exact_title_elm = '[data-test="inventory-item-name"]:has-text("{0}")' # exact name
    """
    =================================================
    """

    @allure.step("Check if inventory list is visible")
    def is_inventory_loaded(self) -> bool:
        """
        Returns true if list of elements is presented on the Inventory page
        :return: True if loaded, False otherwise
        """

        return self.is_visible(self.inventory_item_name_list)

    @allure.step("Perform click on the item`s title")
    def inventory_title_click(self, item_name: str) -> None:
        """
        Performs click operation on element of a list with exact title
        :param item_name: title to filter
        :return:
        """

        self.click(selector=self.inventory_exact_title_elm.format(item_name))

    @allure.step("Return item inner text")
    def get_item_name(self) -> str:
        """
        Returns inner text if presented
        :return:
        """

        return self.get_inner_text(selector=self.inventory_item_name_list)