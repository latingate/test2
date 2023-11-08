import sys
import pytest
from selenium import webdriver
import webbrowser

default_browser = webbrowser.get()
# print(vars(default_browser))
# default_browser_name = default_browser.name
# default_browser_basename = default_browser.basename


@pytest.mark.skipif(sys.platform != "darwin", reason="requires Mac")
def test_basic_options():
    options = webdriver.SafariOptions()
    driver = webdriver.Safari(options=options)
    url = 'https://reva5.co.il'
    driver.get(url)
    driver.get_screenshot_as_file("MAC_screenshotPost.png")
    driver.quit()


@pytest.mark.skipif(sys.platform != "darwin", reason="requires Mac")
def test_enable_logging():
    service = webdriver.SafariService(service_args=["--diagnose"])

    driver = webdriver.Safari(service=service)

    driver.quit()

@pytest.mark.skip(reason="Not installed on Mac GitHub Actions Runner Image")
def test_technology_preview():
    options = webdriver.SafariOptions()
    options.use_technology_preview = True
    service = webdriver.SafariService(
        executable_path='/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver'
    )
    driver = webdriver.Safari(options=options, service=service)

    driver.quit()



test_basic_options()
test_enable_logging()
# test_technology_preview()


