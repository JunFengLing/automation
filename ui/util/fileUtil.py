import json


def read_file(path, mode='r'):
    with open(path, mode) as f:
        return f.read()


if __name__ == '__main__':
    path = 'C:\\Users\\daij1\\PycharmProjects\\automation\\ui\\config\\config.json'
    config_str = read_file(path)
    config_json = json.loads(config_str)
    print(config_str)
    print(type(config_str))
    print(config_json)
    print(type(config_json))
    try:
        json.loads('test')
    except json.decoder.JSONDecodeError:
        print('Invalid JSON format')