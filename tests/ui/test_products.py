from playwright.sync_api import expect
from pages.home_page import HomePage

def test_product_display_and_navigation(page, ui_url): # Added ui_url fixture
    home_page = HomePage(page)

    # Pass base_url to navigate
    home_page.navigate(ui_url)

    # Verify that product cards are visible
    expect(home_page.product_cards.first).to_be_visible()

    # Get details before clicking
    product_info = home_page.get_product_details()

    # Navigation to details
    home_page.first_product_link.click()

    # Wait for the details page to load
    expect(page.locator(".name")).to_be_visible(timeout=10000)

    # Validate details
    expect(page.locator(".name")).to_contain_text(product_info["name"])
    expect(page.locator(".price-container")).to_contain_text(product_info["price"].split()[0])

def test_add_product_to_cart(page, ui_url): # Added ui_url fixture
    home_page = HomePage(page)
    home_page.navigate(ui_url)
    home_page.first_product_link.click()

    # Verify Add to Cart and handle popup
    home_page.add_product_to_cart()

    # Optional: verify cart navigation
    page.locator("#cartur").click()
    expect(page.locator("#tbodyid")).to_be_visible()