from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def setup_browser():
    # Setup the Chrome browser using ChromeDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver

def test_google_search():
    # Initialize the browser
    driver = setup_browser()

    try:
        # Navigate to Google
        driver.get("https://www.google.com")

        # Find the search box
        search_box = driver.find_element(By.NAME, "q")

        # Type a query and hit enter
        search_box.send_keys("OpenAI")
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load and display the title
        driver.implicitly_wait(5)  # Waits for 5 seconds

        # Check if the search results contain the expected text
        assert "OpenAI" in driver.title
        print("Test Passed: 'OpenAI' found in the page title")

    except AssertionError:
        print("Test Failed: 'OpenAI' not found in the page title")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_google_search()
