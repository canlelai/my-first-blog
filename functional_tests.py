from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool guy. She goes
        # to check out his CV
        self.browser.get('http://127.0.0.1:8000/cv/')

        # She notices the page title and header mention Canle's CV
        self.assertIn("Canle's CV", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Canle's CV", header_text)
        self.fail('Finish the test!')

        # She is invited to enter a CV straight away

if __name__ == '__main__':
    unittest.main(warnings='ignore')
