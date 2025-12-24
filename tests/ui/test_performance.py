import time

def test_homepage_load_performance(page, ui_url):
    start_time = time.time()
    page.goto(ui_url)
    end_time = time.time()

    duration = end_time - start_time
    print(f"\nHomepage loaded in {duration:.2f} seconds")

    # Assert that page loads under 5 seconds
    assert duration < 5.0, f"Page load took too long: {duration}s"