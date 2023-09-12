from django.test import TestCase, Client

class MainTest(TestCase):
    # test URL
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code,200)

    # test views
    def test_main_using_item_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    # test HTML
    def test_template_has_checklist(self):
        response = Client().get('/main/')
        self.assertContains(response, 'App Name: ', html=True)
        self.assertContains(response, 'Name: ', html=True)
        self.assertContains(response, 'Class: ', html=True)