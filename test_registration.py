
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "http://localhost:8081"


@pytest.fixture
def driver():
    browser = webdriver.Chrome()

    browser.get(BASE_URL)

    yield browser

    browser.quit()


# Test Case 1: Check page title
def test_page_title(driver):
    assert driver.title == "Event Registration"


# Test Case 2: Check registration form
def test_form_display(driver):
    assert driver.find_element(By.ID, "name").is_displayed()
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "phone").is_displayed()


# Test Case 3: Successful registration
def test_registration(driver):

    driver.find_element(By.ID, "name").send_keys("Imran")

    driver.find_element(By.ID, "email").send_keys(
        "imran@gmail.com"
    )

    driver.find_element(By.ID, "phone").send_keys(
        "9876543210"
    )

    event = Select(
        driver.find_element(By.ID, "event")
    )

    event.select_by_visible_text("Hackathon")

    driver.find_element(
        By.XPATH, "//button[@type='submit']"
    ).click()

    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    assert "Registration Successful" in alert.text

    alert.accept()


# Test Case 4: Check required field validation
def test_required_field(driver):

    name = driver.find_element(By.ID, "name")
    assert name.get_attribute("required") is not None

    email = driver.find_element(By.ID, "email")
    assert email.get_attribute("required") is not None
