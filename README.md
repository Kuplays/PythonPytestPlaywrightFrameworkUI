# Python Pytest Playwright UI Automation Framework

Simple demo project for UI automation framework powered by [pytest](https://docs.pytest.org/en/stable/ "Go to pytest docs") and [playwright](https://playwright.dev/ "Go to playwright page"). <br>
***
## Features

- Python 3.12, Pytest, Playwright
- Page Object Model ([POM](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/ "Go to example definition at Selenium"))
- Using [Fixtures](https://docs.pytest.org/en/6.2.x/fixture.html "Open to read about fixtures")
- Cross-browser support: Chromium, Firefox, Safari
- [Allure](https://allurereport.org/ "Open to read about this awesome report tool") Reports generation
- Screenshots and running environment in reports
- CI/CD using [Github Actions](https://github.com/features/actions "Open to read about GA")
- Matrix and CLI runs
- Live reports on Github Pages: [Report](https://kuplays.github.io/PythonPytestPlaywrightFrameworkUI/)

## Installation

~~~
# clone repository
git clone https://github.com/Kuplays/PythonPytestPlaywrightFrameworkUI.git
cd PythonPytestPlaywrightFrameworkUI

# Create Virtual Environment (venv)
python -m venv my_venv
my_venv\Scripts\activate      # Activating on Windows
source my_venv/bin/activate   # Activating on Unix

# install required dependencies
pip install -r requirements.txt

# install playwright browsers
playwright install

# Install Allure reports for Python
pip install allure-pytest

# Install Allure CLI
https://allurereport.org/docs/install-for-windows/ # For Windows
https://allurereport.org/docs/install-for-linux/   # For Linux
~~~

## Test run example

~~~
# Run smoke tests on Chromium and generate Allure report with given directory
pytest -m smoke --headed --browser=chromium --alluredir=reports/allure-reports --clean-alluredir
# Serve reports to a browser page
allure serve .\reports\allure-reports 
~~~

## License

[MIT License](https://opensource.org/license/mit "Read about mit") – Feel free to use in any way.
***
[![CI](https://github.com/Kuplays/PythonPytestPlaywrightFrameworkUI/actions/workflows/ci.yml/badge.svg)](https://github.com/Kuplays/PythonPytestPlaywrightFrameworkUI/actions) <br>
ALLURE REPORT: https://kuplays.github.io/PythonPytestPlaywrightFrameworkUI/
