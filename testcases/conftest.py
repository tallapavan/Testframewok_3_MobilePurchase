import os.path
import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager
from utilities.utilis import Utils


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--env")

@pytest.fixture(scope="function", autouse= True)
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture(scope="function", autouse= True)
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="function", autouse= True)
def setup(browser, env , request):
    log = Utils.custom_logger()
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        print("enter valid browser")

    if env == 'test':
        driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    else:
        log.error("Enter valid env")

    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://www.google.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time()*1000)))+".png"
            #file_name = report.nodeid.replace("::","_")+".png"
            destinationFile = os.path.join(report_directory,file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt = "screenshot" style = "width:300px; height=200px"' \
                'onclick = "window.open(this.src)" align = "right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra

def pytest_html_report_title(report):
    report.title = "TEST REPORT"




#
# @pytest.fixture(autouse=True)
# def setup(request):
#     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     driver.get("https://rahulshettyacademy.com/angularpractice/shop")
#     # driver.maximize_window()
#     driver.implicitly_wait(10)
#     request.cls.driver = driver
#     yield
#     driver.close()