from playwright.sync_api import sync_playwright, expect, Page
import pytest
from dotenv import load_dotenv
import os
import time
load_dotenv()


@pytest.fixture(scope="module")
def shared_data():
    return {"model_name": None}


@pytest.fixture
def context(browser):
    return browser.new_context(ignore_https_errors=True)


@pytest.fixture
def page(context):
    return context.new_page()


@pytest.fixture
def url():
    return os.getenv("url")


@pytest.fixture
def credentials():
    return {
        "username": os.getenv("username"),
        "password": os.getenv("password")
    }


def test_go_to_webpage(page: Page, url: str, credentials: dict):
    # Go to the url
    assert credentials["username"] is not None, "username 環境變數未設置！"
    assert credentials["password"] is not None, "password 環境變數未設置！"

    page.goto(url)

    # Type the username and password
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
        page.mouse.move(source_box["x"] + source_box["width"] / 2, source_box["y"] + source_box["height"] / 2)
        page.mouse.down()
        page.mouse.move(target_box["x"] + target_box["width"] / 2, target_box["y"] + target_box["height"] + 70)
        page.mouse.up()
    print("Add a state")

    source1 = page.locator(".flex.gap-2.justify-between.items-center.w-full")
    source1.click()
    print("Click an AI tool.")
    # instanceSeg = page.locator(".iconify.i-my-icon\\3A instance.min-size-14.size-14.rounded-lg")

    # start_node = page.locator(".vue-flow__node.vue-flow__node-start.nopan.draggable.selected.selectable")
    # instanceSeg.drag_to(start_node)


def test_model_center(page: Page):
    # Click the sidebar of the Model Center
    page.click('role=link[name="Model"]')
    h1_locator = page.locator("h1")
    expect(h1_locator).to_have_text("Model List")
    print("Model List")


def test_upload_model(page: Page, shared_data: dict):
    # Click the Create button
    page.click('role=link[name="Create"]')
    print("Create a Model Page")
    page.wait_for_timeout(1000)
    # If you use this one, you cannot close the UI uploading dialog
    # page.click("button:has-text('Browse on your device')")

    file_path = os.getenv("file_path")
    assert file_path is not None, "please set up a value for file_path."
    page.set_input_files('input[type="file"]', file_path)
    page.wait_for_timeout(20000)
    print("Upload a sol model")

    model_name = f"model_{time.strftime('%Y%m%d_%H%M%S')}"
    page.fill('#v-3-64', model_name)
    print("Give a model name")
    shared_data["model_name"] = model_name

    try:
        page.wait_for_selector('button:has-text("Upload"):not([disabled])', timeout=10000)
        page.click('button:has-text("Upload")')
        print("Successfully click the Upload button")
    except Exception as e:
        print(f"Click Upload button failure: {e}")

    page.wait_for_timeout(30000)
    print("Done pressing the upload button")
    # model_name = "model_20250304_094706" # for testing

    # Get the name of the active model
    displayed_model_name = page.inner_text('.model-list-card__item.active span.text-xs')
    print(f"Displayed model name: {displayed_model_name}")

    # Verify if it matches
    if model_name in displayed_model_name:  # Use 'in' to handle possible suffixes
        print(f"Verification successful! Uploaded model name '{model_name}' appears in the list")
    else:
        print(f"Verification failed! Expected '{model_name}', but got '{displayed_model_name}'")
        raise Exception("Verification failed!")

    return shared_data


def test_delete_model(page: Page, shared_data: dict):

    model_name = shared_data["model_name"]
    if model_name is None:
        raise Exception("model_name is None!")

    # Get the name of the active model
    displayed_model_name = page.inner_text('.model-list-card__item.active span.text-xs')
    print(f"Displayed model name: {displayed_model_name}")
    if model_name in displayed_model_name:  # Use 'in' to handle possible suffixes
        print(f"Verification successful! Uploaded model name '{model_name}' appears in the list")
    else:
        print(f"Verification failed! Expected '{model_name}', but got '{displayed_model_name}'")
        raise Exception("Verification failed!")

    more_button_selector = '.model-list-card__item.active button:has(> span.i-heroicons\\:ellipsis-horizontal-20-solid)'
    page.click(more_button_selector)

    delete_button_selector = '[role="menuitem"]:has-text("Delete")'
    page.wait_for_selector(delete_button_selector, timeout=5000)
    page.click(delete_button_selector)

    confirm_delete_selector = 'button.bg-primary-500:has-text("Delete")'
    page.wait_for_selector(confirm_delete_selector, timeout=5000)
    page.click(confirm_delete_selector)

    try:
        page.wait_for_selector('.model-list-card__item.active', state="detached", timeout=10000)
        print("Model deletion successful!")
    except Exception as e:
        print(f"Model deletion failed: {e}")
        raise Exception("Model deletion failed!")


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        new_page = browser.new_page(ignore_https_errors=True)
        url = os.getenv("url")
        credentials = {
            "username": os.getenv("username"),
            "password": os.getenv("password")
        }
        test_go_to_webpage(new_page, url, credentials)
        test_model_center(new_page)
        model_shared_data = {"model_name": None}
        # model_shared_data = {"model_name": "model_20250304_095844"}
        model_shared_data = test_upload_model(new_page, model_shared_data)
        test_delete_model(new_page, model_shared_data)

        # test_project_center(new_page)

        input("Press Enter to close...")
        browser.close()
