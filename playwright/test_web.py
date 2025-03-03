import re
from playwright.sync_api import sync_playwright, expect, Page
import pytest
from dotenv import load_dotenv
import os
import time 
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

def test_project_center(page: Page):
    # Click the sidebar of the Project Center
    page.click('role=link[name="Project"]')
    h1_locator = page.locator("h1")
    expect(h1_locator).to_have_text(" Create your AI Project. ")
    print("Create Project")

    # Click the Create button
    page.click('role=link[name="Create"]')
    print("Create a project")

    # source = page.locator(".flow-bar__item.flow-state")
    # target = page.locator(".vue-flow__node.vue-flow__node-flow-start.nopan.draggable.selectable")
    # source.drag_to(target)
    source_box = page.locator(".flow-bar__item.flow-state").bounding_box()
    target_box = page.locator(".vue-flow__node.vue-flow__node-flow-start.nopan.draggable.selectable").bounding_box()
    if source_box and target_box:
        page.mouse.move(source_box["x"] + source_box["width"]/2, source_box["y"] + source_box["height"]/2)
        page.mouse.down()
        page.mouse.move(target_box["x"] + target_box["width"]/2, target_box["y"] + target_box["height"]+70) 
        page.mouse.up()
    print("Add a state")
    
    source1 = page.locator(".flex.gap-2.justify-between.items-center.w-full")
    source1.click()
    print("Click an AI tool.")
    # instanceSeg = page.locator(".iconify.i-my-icon\\3A instance.min-size-14.size-14.rounded-lg")

    # start_node = page.locator(".vue-flow__node.vue-flow__node-start.nopan.draggable.selected.selectable")
    # instanceSeg.drag_to(start_node)


# def test_model_center(page: Page):
#     # Click the sidebar of the Model Center
#     page.click('role=link[name="Model"]')
#     h1_locator = page.locator("h1")
#     expect(h1_locator).to_have_text("Model List")
#     print("Model List")

# def test_upload_model(page: Page):
#     # Click the Create button
#     page.click('role=link[name="Create"]')
#     print("Create Page")
#     page.click("button:has-text('Browse on your device')")
#     page.set_input_files('input[type="file"]', "./model.onnx")


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
        test_project_center(page)
        # test_model_center(page)
        # test_upload_model(page)
        input("Press Enter to close...")
        browser.close()
