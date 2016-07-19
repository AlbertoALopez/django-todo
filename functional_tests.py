"""General functional tests for To Do list app."""
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """Class for testing a new user story."""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a new online to do app. She checks out its
        # homepage
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to do item straight away

        # She types "buy peacock feathers" into a text box

        # She hits enter, the page updates and now the page lists
        # "1: Buy peacock feathers" as an item in a to do lists

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"

        # Page updates again, now shows both items on her lists

        # Edith wonders whether the site will remember her list. Then she
        # sees that the site has generated a unique URL for her.

        # She visits that url and the list is still There

        # Satisfied she goes back to sleep

        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
