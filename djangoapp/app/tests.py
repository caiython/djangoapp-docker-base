from django.test import TestCase
from selenium import webdriver

# Create your tests here.


class SeleniumTest(TestCase):
    fixtures = [
        'app/fixtures/app.json',
        ...
    ]

    def start(self):

        selenium_grid_url = "http://selenium:4444/wd/hub"
        options = webdriver.FirefoxOptions()

        # Instantiate an instance of Remote WebDriver with the desired capabilities.
        self.browser = webdriver.Remote(command_executor=selenium_grid_url,
                                        keep_alive=True,
                                        options=options)

    def stop(self):
        self.browser.quit()

    def test_visit_site(self):
        self.browser.get('http://djangoapp:8000/')
        self.assertIn(self.browser.title, 'Home')
