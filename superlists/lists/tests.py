"""Unit tests for TO DO app."""
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item, List


class HomePageTest(TestCase):
    """Test class for TO DO app home page."""

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


class NewListTest(TestCase):
    """Test class for new lists."""

    def test_saving_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')


class ListViewTest(TestCase):
    """Test class for list views."""

    def test_displays_all_items(self):
        _list = List.objects.create()
        Item.objects.create(text='itemey 1', list=_list)
        Item.objects.create(text='itemey 2', list=_list)

        response = self.client.get('/lists/the-only-list-in-the-world/')
        print(response.content)

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

    def test_uses_list_templates(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')


class ListAndItemModelTest(TestCase):
    """Test class for TO DO item and list models."""

    def test_saving_and_retrieving_items(self):
        """Test saving and retrieving items."""
        _list = List()
        _list.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = _list
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = _list
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, _list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, _list)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, _list)
