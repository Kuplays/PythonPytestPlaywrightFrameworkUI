import pytest
from page_objects.inventory_page import InventoryPage

@pytest.mark.smoke
@pytest.mark.parametrize(
    "item_name",
    [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
     ]
)
def test_open_inventory_item(get_logged_page, basic_url, item_name):
    """
    Test performs click on a given element with given name and checks if corresponding element was loaded. Uses
    parametrize to perform same operation with every element to ensure correct loading of different elements.
    TODO: load data from csv/json
    :param get_logged_page: page with login
    :param basic_url: basic url
    :param item_name: item to compare
    :return:
    """

    inventory_page = InventoryPage(get_logged_page, basic_url)
    inventory_page.inventory_title_click(item_name=item_name)
    title_actual = inventory_page.get_inner_text(selector=inventory_page.inventory_item_name_list)
    assert item_name == title_actual