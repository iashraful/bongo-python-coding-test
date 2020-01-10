#!/usr/bin/env python

def has_next_label(dictionary):
    if type(dictionary) == dict:
        return True
    return False


def depth_checker(data, depth=1):
    if not isinstance(data, dict):
        return False, 'Expected Dictionary.'
    for _key, dictionary in data.items():
        print('{key} {depth}'.format(key=_key, depth=depth))
        if has_next_label(dictionary):
            depth_checker(data=dictionary, depth=depth + 1)


if __name__ == '__main__':
    test_dict = {
        'a': 10,
        'b': {
            'c': {
                'd': {
                    'e': {
                        'f': 10,
                        'g': 'test'
                    }
                },
                'x': 'wow',
                'y': 'lol',
                'z': 'final'
            }
        },
        'ab': 'Good Bye'
    }
    depth_checker(test_dict)
