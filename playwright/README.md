# Playwright

## Env

1. Install UV
2. Start an env. `uv venv playwright`
    Output: 
    ```
    Using CPython 3.9.6 interpreter at: /Library/Developer/CommandLineTools/usr/bin/python3
    Creating virtual environment at: playwright
    Activate with: source playwright/bin/activate
    ```
3. Activate it. `source playwright/bin/activate`
    Then install the library.

## Installation

```
uv pip install pytest-playwright dotenv
playwright install
```

## Example:

```python
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
```

Run it.

```
pytest -s
```


## Usage

Please copy the `.env.sample` to `.env`.

Run it.

```
python test_web.py
```
