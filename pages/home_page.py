from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        # Selectors for product elements
        self.product_cards = page.locator(".card")
        self.first_product_link = page.locator(".card-title a").first
        self.product_price_label = page.locator(".card-block h5").first
        self.add_to_cart_btn = page.locator("a.btn-success:has-text('Add to cart')")

    def navigate(self, url: str):
        # Load the page and wait for the main content
        self.page.goto(url, wait_until="load")
        # Ensure the catalog is actually loaded
        self.first_product_link.wait_for(state="visible", timeout=5000)

    def get_product_details(self):
        # Fetch name and price from the first card
        name = self.first_product_link.inner_text()
        price = self.product_price_label.inner_text()
        return {"name": name.strip(), "price": price.strip()}

    def add_product_to_cart(self):
        # Listen for the browser dialog (alert) before clicking
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.add_to_cart_btn.click()