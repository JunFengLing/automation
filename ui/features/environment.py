import json

from util.fileUtil import read_file
from core.driver_factory import DriverFactory
from pageobjects.login_page import LoginPage
from pageobjects.page_cache import PageCache


def before_all(context):
    print('before all')
    context.config = get_config()
    context.driver = get_driver(context.config)
    context.environment = get_environment(context.config['environment'])
    context.page_cache = PageCache(context.driver)


def after_all(context):
    print('after all')
    context.driver.quit()


def before_tag(context, tag):
    print('before tag')


def after_tag(context, tag):
    print('after tag')


def before_feature(context, feature):
    print('before feature')


def after_feature(context, feature):
    print('after feature')


def before_scenario(context, scenario):
    print('before scenario')
    context.driver.get(context.environment['AppUrl'])
    login_page = context.page_cache.login_page
    login_page.wait_for_page_ready()
    # login
    login = get_login(context.environment, scenario.tags)
    login_page.login(login['Username'], login['Password'])


def after_scenario(context, scenario):
    print('after scenario')
    context.page_cache.navigation_bar.sign_out()


def before_step(context, step):
    print('before step')


def after_step(context, step):
    print('after step')


def get_config():
    config_path = 'C:\\Users\\daij1\\PycharmProjects\\automation\\ui\\config\\config.json'
    config_str = read_file(config_path)

    try:
        config_json = json.loads(config_str)
        browser = config_json['Browser'].strip().lower()
        environment = config_json['Environment'].strip().upper()

        return {
            'browser': browser,
            'environment': environment
        }
    except json.decoder.JSONDecodeError:
        print('Invalid JSON format')
    finally:
        pass


def get_driver(config):
    driver = None
    if config['browser'] == 'chrome':
        driver = DriverFactory.get_chrome_driver()
    elif config['browser'] == 'firefox':
        pass
    elif config['browser'] == 'ie':
        pass
    elif config['browser'] == 'safari':
        pass
    else:
        pass

    return driver


def get_environment(key):
    environment_path = 'C:\\Users\\daij1\\PycharmProjects\\automation\\ui\\config\\environment.json'
    environment_str = read_file(environment_path)

    try:
        environment_json = json.loads(environment_str)

        return environment_json[key]
    except json.decoder.JSONDecodeError:
        print('Invalid JSON format')
    finally:
        pass


def get_login(environment, tags):
    if len(tags) >= 1:
        for tag in tags:
            if tag.strip().lower().startswith('web-'):
                login_key = tag.strip().lower().lstrip('web-')
            else:
                login_key = 'default'
    else:
        login_key = 'default'
    # print(login_key)
    return environment['Logins'][login_key]