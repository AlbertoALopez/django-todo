"""General functional tests for To Do list app."""
from selenium import webdriver
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
django.setup()
from selenium.webdriver.common.keys import Keys
from lists.models import Item
import unittest


class NewVisitorTest(unittest.TestCase):
    """Test a new user story."""

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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # She hits enter, the page updates and now the page lists
        # "1: Buy peacock feathers" as an item in a to do lists
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # Page updates again, now shows both items on her lists
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )

        # Edith wonders whether the site will remember her list. Then she
        # sees that the site has generated a unique URL for her.
        self.fail('Finish the test')

        # She visits that url and the list is still There

        # Satisfied she goes back to sleep

        self.browser.quit()


class ItemModelTest(unittest.TestCase):
    """Test model for items in TO DO list."""

    def test_saving_and_retrieving_items(self):
        """Test saving and retrieving items."""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
