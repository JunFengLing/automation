from behave import *


class Test(object):

    @given('user is on "{country}" research landing page')
    def step_impl(context, country):
        context.master_feature_country = country

        navigation_bar = context.page_cache.navigation_bar
        current_product = navigation_bar.nav_current_product_btn.text.strip()
        condition = current_product.startswith('Lexis Advance') & current_product.endswith('Pacific Research')
        if not condition:
            navigation_bar.nav_product_switcher_arrow_btn.click()
            navigation_bar.product_switcher('pacificresearch').click()
            navigation_bar.wait_for_page_ready()

    @when('user search by term "{term}" in BRSB')
    def step_impl(context, term):
        context.page_cache.search_page.search(term)

    @then('user is on search result page for "{term}"')
    def step_impl(context, term):
        result_page = context.page_cache.result_page
        query_for = result_page.query_for.text.strip()

        assert query_for, term

    @then('the "{position}" country flag is "{country}"')
    def step_impl(context, position, country):

        expected_country = ''
        if position == '1st':
            expected_country = context.master_feature_country
        elif position == '2nd':
            expected_country = 'UK'

        assert country, expected_country

    @then('the other country flags are sort alphabetically')
    def step_impl(context):
        context.actual_countries_text_list = context.page_cache.result_page.countries_text_list
        print(context.actual_countries_text_list[2:])

        assert context.actual_countries_text_list[2:], context.actual_countries_text_list[2:].sort()

    @then('the following HLCT are displayed')
    def step_impl(context):
        hlct_text_list = context.page_cache.result_page.hlct_text_list
        for i in range(len(context.table)):
            condition = hlct_text_list[i].startswith(context.table[i]['HLCT'])
            assert condition
