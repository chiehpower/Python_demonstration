import re
from playwright.sync_api import sync_playwright, expect, Page
import pytest
from dotenv import load_dotenv
import os
load_dotenv()

@pytest.fixture
def context(browser):
    return browser.new_context(ignore_https_errors=True)

@pytest.fixture
def page(context):
    return context.new_page()

@pytest.fixture
def url():
    return os.getenv("URL")

@pytest.fixture
def credentials():
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }

def test_go_to_webpage(page: Page, url: str, credentials: dict):
    # Go to the url
    assert credentials["username"] is not None, "USERNAME 環境變數未設置！"
    assert credentials["password"] is not None, "PASSWORD 環境變數未設置！"

    page.goto(url)

    # Type the username and password
    print(credentials["username"])
    page.fill('input[name="username"]', credentials["username"])
    page.fill('input[name="password"]', credentials["password"])
    
    # Wait for the login button to be visible and enabled, then click it
    button = page.locator('button:has-text("Login")')
    button.click()
    print("Done for Login")

def test_model_center(page: Page):
    # Click the sidebar of the Model Center
    page.click('role=link[name="Model"]')
    h1_locator = page.locator("h1")
    expect(h1_locator).to_have_text("Model List")
    print("Model List")

def test_upload_model(page: Page):
    # Click the Create button
    page.click('role=link[name="Create"]')
    print("Creat Page")
    page.click("button:has-text('Browse on your device')")
    page.set_input_files('input[type="file"]', "./model.onnx")


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(ignore_https_errors=True)
        # test_has_title(page)
        # test_get_started_link(page)
        url = os.getenv("URL")
        credentials = {
            "username": os.getenv("USERNAME"),
            "password": os.getenv("PASSWORD")
        }
        test_go_to_webpage(page, url, credentials)
        test_model_center(page)
        test_upload_model(page)
        input("Press Enter to close...")
        browser.close()
