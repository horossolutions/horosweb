import sys
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase




class NewVisitorTest(StaticLiveServerTestCase):
	@classmethod
	def setUpClass(cls):  #1
		for arg in sys.argv:  #2
			if 'liveserver' in arg:  #3
				cls.server_url = 'http://' + arg.split('=')[1]  #4
				return  #5
		super().setUpClass()  #6
		cls.server_url = cls.live_server_url

	@classmethod
	def tearDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def get_full_url(self, namespace):
		return self.live_server_url + reverse(namespace)

	def test_home_title(self):
		self.browser.get(self.server_url)
		self.assertIn('Horos', self.browser.title)

	def test_h1_css(self):
		self.browser.get(self.server_url)
		h1 = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(h1.value_of_css_property('color'),
			'rgba(255, 255, 255, 1)')

	#def test_about_page(self):
	#	self.browser.get(self.get_full_url('about'))
	#	self.assertIn('About', self.browser.title)

	def test_portfolio_pages(self):
		pass

