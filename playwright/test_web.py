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
    div_locator = page.locator('div.min-w-\[150px\].relative.flex.items-center.gap-4')
    div_text = div_locator.inner_text()
    assert "Project" in div_text, "Expect to contain 'Project'"
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

    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)

    # Get InstanceSeg node
    instance_seg_node = page.locator("//div[contains(@class, 'AI-node__node')]//p[text()='InstanceSeg']/..")
    print(f"Found {instance_seg_node.count()} InstanceSeg nodes")
    if instance_seg_node.count() == 0:
        raise Exception("InstanceSeg node not found!")
    if not instance_seg_node.is_visible():
        instance_seg_node.scroll_into_view_if_needed()
        if not instance_seg_node.is_visible():
            raise Exception("InstanceSeg node is not visible!")

    # Get Start node
    start_node = page.locator("//div[contains(@class, 'vue-flow__node-start')][contains(., 'Start')]")
    print(f"Found {start_node.count()} Start nodes")
    if start_node.count() == 0:
        raise Exception("Start node not found!")

    handle_right = start_node.locator(".vue-flow__handle-right")
    if handle_right.count() == 0:
        raise Exception("Start node does not have a right handle!")

    # 取得 Start Node 的座標 (Bounding Box)
    start_node_box = start_node.bounding_box()
    if not start_node_box:
        raise Exception("Failed to get bounding box of Start node!")

    # 計算 Start Node 的右邊邊緣位置並向右偏移
    offset = 50  # 偏移量，例如向右偏移 50 像素
    target_x = start_node_box["x"] + start_node_box["width"] + offset
    target_y = start_node_box["y"] + (start_node_box["height"] / 2)
    print(f"Target drop position: ({target_x}, {target_y})")

    # 將 InstanceSeg node 拖曳到偏移後的右邊位置
    instance_seg_box = instance_seg_node.bounding_box()
    page.mouse.move(instance_seg_box['x'] + instance_seg_box['width'] / 2, 
                    instance_seg_box['y'] + instance_seg_box['height'] / 2)
    page.mouse.down()

    page.mouse.move(target_x, target_y)
    page.mouse.up()
    # instance_seg_node.drag_to(handle_right)

    # Turn on the right sidebar
    target_element = page.locator('span[class="absolute text-[9px] text-[#63707B] inset-0 p-[1px] truncate"]')
    if target_element.count() == 0:
        raise Exception("Target span element not found!")
    elif target_element.count() > 1:
        print(f"Warning: Found {target_element.count()} matching elements, using the first one")
        target_element = target_element.first
    target_element.wait_for(state="visible")
    target_element.dblclick()
    page.wait_for_timeout(100)
    print("Turn on the right sidebar")

    # Turn on the model center
    select_button = page.locator('button[class*="focus:outline-none"][class*="rounded-md"][class*="text-xs"] span:has-text("Select")').locator('..')
    if select_button.count() == 0:
        raise Exception("Select button not found!")
    select_button.wait_for(state="visible")
    select_button.click()
    page.wait_for_timeout(100)
    print("Turn on the model center")

    # Select the first model card
    card_item = page.locator('div.model-list-card__item')
    if card_item.count() == 0:
        raise Exception("Model list card item not found!")
    elif card_item.count() > 1:
        print(f"Warning: Found {card_item.count()} matching card items, using the first one")
        card_item = card_item.first
    card_item.wait_for(state="visible")
    card_item.click()
    page.wait_for_timeout(100)
    print("Select the first model card")

    # Click the confirm button
    confirm_button = page.locator('button[class*="focus:outline-none"][class*="rounded-md"][class*="bg-primary-500"] span:has-text("Confirm")').locator('..')
    if confirm_button.count() == 0:
        raise Exception("Confirm button not found!")
    confirm_button.wait_for(state="visible")
    confirm_button.click()
    page.wait_for_timeout(100)
    print("Click the confirm button")

    # Close the right sidebar
    target_element = page.locator('span[class="absolute text-[9px] text-[#63707B] inset-0 p-[1px] truncate"]')
    if target_element.count() == 0:
        raise Exception("Target span element not found!")
    elif target_element.count() > 1:
        print(f"Warning: Found {target_element.count()} matching elements, using the first one")
        target_element = target_element.first
    target_element.wait_for(state="visible")
    target_element.click()
    page.wait_for_timeout(100)
    print("Close the right sidebar")

    # Start to connect a line from start node to InstanceSeg node
    start_handle = page.locator('div[data-handlepos="right"].vue-flow__handle-right.source').nth(1)
    if start_handle.count() != 1:
        raise Exception(f"Expected 1 element, but found {start_handle.count()}")

    start_box = start_handle.bounding_box()
    start_x = start_box["x"] + start_box["width"] / 2
    start_y = start_box["y"] + start_box["height"] / 2
    print(f"Start node right handle position: ({start_x}, {start_y})")

    InstanceSeg_handle = page.locator('div.vue-flow__handle-left.target').nth(2)  # 或 nth(1), nth(2)
    if InstanceSeg_handle.count() != 1:
        raise Exception(f"Expected 1 element for InstanceSeg Handle, but found {InstanceSeg_handle.count()}")
    InstanceSeg_box = InstanceSeg_handle.bounding_box()
    InstanceSeg_x = InstanceSeg_box["x"] + InstanceSeg_box["width"] / 2
    InstanceSeg_y = InstanceSeg_box["y"] + InstanceSeg_box["height"] / 2
    print(f"InstanceSeg left Handle position: ({InstanceSeg_x}, {InstanceSeg_y})")

    page.mouse.move(start_x, start_y)
    page.mouse.down()
    page.wait_for_timeout(1000)
    page.mouse.move(InstanceSeg_x, InstanceSeg_y)
    page.wait_for_timeout(1000)
    page.mouse.up()
    print("Line has been successfully drawn from the start handle to the InstanceSeg left handle.")
    print("-----")

    # Start to connect a line from InstanceSeg node to end node
    InstanceSeg_right_handle = page.locator('div[data-handlepos="right"].vue-flow__handle-right.source').nth(2)
    if InstanceSeg_right_handle.count() != 1:
        raise Exception(f"Expected 1 element for InstanceSeg right handle, but found {InstanceSeg_right_handle.count()}")
    InstanceSeg_right_box = InstanceSeg_right_handle.bounding_box()
    InstanceSeg_right_x = InstanceSeg_right_box["x"] + InstanceSeg_right_box["width"] / 2
    InstanceSeg_right_y = InstanceSeg_right_box["y"] + InstanceSeg_right_box["height"] / 2
    print(f"InstanceSeg right handle position: ({InstanceSeg_right_x}, {InstanceSeg_right_y})")

    end_left_handle = page.locator('div[data-handlepos="left"].vue-flow__handle-left.target').nth(1)
    end_left_box = end_left_handle.bounding_box()
    end_left_x = end_left_box["x"] + end_left_box["width"] / 2
    end_left_y = end_left_box["y"] + end_left_box["height"] / 2
    print(f"End left handle position: ({end_left_x}, {end_left_y})")

    page.mouse.move(InstanceSeg_right_x + 1, InstanceSeg_right_y)
    page.mouse.down()
    page.wait_for_timeout(1000)
    page.mouse.move(end_left_x, end_left_y)
    page.wait_for_timeout(1000)
    page.mouse.up()
    print("Line has been successfully drawn from InstanceSeg right handle to end left handle.")
    print("-----")

    # Now we need to connect a line in the State level from Start node to InstanceSeg state
    bottom_handle = page.locator('div[data-handlepos="bottom"].vue-flow__handle-bottom.source').nth(0)
    if bottom_handle.count() != 1:
        raise Exception(f"Expected 1 element for bottom handle, but found {bottom_handle.count()}")
    bottom_handle.wait_for(state="visible")
    bottom_box = bottom_handle.bounding_box()
    bottom_x = bottom_box["x"] + bottom_box["width"] / 2
    bottom_y = bottom_box["y"] + bottom_box["height"] / 2
    print(f"Bottom handle position: ({bottom_x}, {bottom_y})")

    top_handle = page.locator('div[data-handlepos="top"].vue-flow__handle-top.target').nth(0)
    if top_handle.count() != 1:
        raise Exception(f"Expected 1 element for top handle, but found {top_handle.count()}")
    top_handle.wait_for(state="visible")
    top_box = top_handle.bounding_box()
    top_x = top_box["x"] + top_box["width"] / 2
    top_y = top_box["y"] + top_box["height"] / 2
    print(f"Top handle position: ({top_x}, {top_y})")

    page.mouse.move(bottom_x, bottom_y)
    page.mouse.down()
    page.wait_for_timeout(1000)
    page.mouse.move(top_x, top_y)
    page.wait_for_timeout(1000)
    page.mouse.up()
    print("Line has been successfully drawn from bottom handle to top handle.")
    print("-----")

    # Need to choose a mode
    button = page.locator('button.relative.w-full').nth(1)
    button.wait_for(state="visible")
    button.click()
    print("Clicked the main button.")

    page.wait_for_timeout(500)  
    default_option = page.locator('li:has-text("Default")')    
    default_option.wait_for(state="visible")
    default_option.click()
    print("Selected the Default option.")

    # Click the Upload button
    upload_button = page.locator('button span:has-text("Upload")').locator('..')
    upload_button.wait_for(state="visible")
    upload_button.click()
    print("Upload button clicked.")
    print("Successfully create a project.")

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
    # page.wait_for_timeout(10000)
    print("Upload a sol model")

    model_name = f"model_{time.strftime('%Y%m%d_%H%M%S')}"
    page.fill('input[type="text"][name="name"]', model_name)
    print("Give a model name")
    shared_data["model_name"] = model_name

    try:
        page.wait_for_selector('button:has-text("Upload"):not([disabled])', timeout=10000)
        page.click('button:has-text("Upload")')
        print("Successfully click the Upload button")
    except Exception as e:
        print(f"Click Upload button failure: {e}")

    page.wait_for_timeout(30000)
    # page.wait_for_timeout(20000)
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
        # test_model_center(new_page)
        # model_shared_data = {"model_name": "model_20250304_095844"}
        # model_shared_data = {"model_name": None}
        # model_shared_data = test_upload_model(new_page, model_shared_data)
        # test_delete_model(new_page, model_shared_data)

        test_project_center(new_page)

        input("Press Enter to close...")
        browser.close()
