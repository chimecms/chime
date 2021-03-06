import unittest
from unittest import TestCase

from acceptance.browser import Browser


class TestBrowser(TestCase):
    def test_creation(self):
        browser = Browser('Windows', '7', "IE", '8.0')
        self.assertEqual('Windows', browser.os)
        self.assertEqual('7', browser.os_version)
        self.assertEqual('IE', browser.browser)
        self.assertEqual('8.0', browser.browser_version)

    def test_as_selenium_capabilities(self):
        browser = Browser('Windows', '7', "IE", '8.0')
        self.assertEqual(
            {'os': 'Windows', 'os_version': '7',
             'browser': 'IE', 'browser_version': '8.0'},
            browser.as_browserstack_capabilities())

    def test_as_browserstack_capabilities_with_extra_info(self):
        browser = Browser('Windows', '7', "IE", '8.0')
        self.assertEqual(
            {'os': 'Windows', 'os_version': '7',
             'browser': 'IE', 'browser_version': '8.0'},
            browser.as_browserstack_capabilities())

    def test_as_saucelabs_capabilities(self):
        browser = Browser('Windows', '7', "IE", '8.0')

        self.assertEqual(
            {'platform': 'Windows 7',
             'browserName': 'internet explorer', 'version': '8.0', 'foo': 'bar'},
            browser.as_saucelabs_capabilities({'foo': 'bar'}))

    def test_doesnt_mutate_extra_info(self):
        browser = Browser('Windows', '7', "IE", '8.0')
        other_info = {'foo': 'bar'}
        self.assertEqual(
            {'os': 'Windows', 'os_version': '7',
             'browser': 'IE', 'browser_version': '8.0', 'foo': 'bar'},
            browser.as_browserstack_capabilities(other_info))
        self.assertEqual(1, len(other_info.keys()))

    def test_from_string_basic(self):
        browsers = Browser.from_string("all")
        self.assertEqual(9, len(browsers))

        browsers = Browser.from_string(None)
        self.assertEqual(None, browsers)

        browsers = Browser.from_string("")
        self.assertEqual(None, browsers)

    def test_from_string_unknown(self):
        with self.assertRaises(ValueError):
            Browser.from_string("arglebargle")

    def test_from_string_supported(self):
        browsers = Browser.from_string("supported")
        self.assertEqual(8, len(browsers))
        self.assertFalse(Browser('Windows', '8.1', "IE", '11.0') in browsers)

    def test_from_string_with_browser(self):
        browsers = Browser.from_string("ie8")
        self.assertEqual([Browser('Windows', '7', "IE", '8.0')], browsers)

        browsers = Browser.from_string("ie11")
        self.assertEqual([Browser('Windows', '8.1', "IE", '11.0'), Browser('Windows', '7', "IE", '11.0')], browsers)

    def test_from_string_with_os(self):
        browsers = Browser.from_string("win8.1")
        for browser in browsers:
            self.assertEqual('Windows', browser.os)
            self.assertEqual('8.1', browser.os_version)

    def test_from_string_with_os_and_browser(self):
        browsers = Browser.from_string("win8.1/ie11")
        self.assertEqual([Browser('Windows', '8.1', "IE", '11.0')], browsers)

    def test_safe_name(self):
        browser = Browser('Windows', '7', "IE", '8.0')
        self.assertEqual("windows_7_ie_8_0", browser.safe_name())

    def test_as_string(self):
        browser = Browser('Windows', '7', 'IE', '8.0')
        self.assertEqual('Windows 7 IE 8.0', str(browser))


if __name__ == '__main__':
    unittest.main()
