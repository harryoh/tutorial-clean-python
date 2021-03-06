from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)

        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.browser.find_element_by_id('id_new_item').send_keys('우유 사기\n')
        self.check_for_row_in_list_table('1: 우유 사기')

#        self.browser.find_element_by_id('id_new_item').send_keys('\n')
#        self.check_for_row_in_list_table('1: 우유 사기')
#        error = self.browser.find_element_by_css_selector('.has-error')
#        self.assertEqual(error.text, "You can't have an empty list item")

        self.browser.find_element_by_id('id_new_item').send_keys('tea 만들기\n')
        self.check_for_row_in_list_table('1: 우유 사기')
        self.check_for_row_in_list_table('2: tea 만들기')
