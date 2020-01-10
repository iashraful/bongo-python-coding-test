#!/usr/bin/env python

def has_next_label(dictionary):
    if type(dictionary) == dict:
        return True
    return False


def is_a_class_object(data):
    return hasattr(data, '__dict__')


def object_depth_checker(data, depth=1):
    if not isinstance(data, dict):
        return False, 'Expected Dictionary.'
    for _key, _object in data.items():
        # Getting all the members of the class object
        dictionary = vars(_object) if is_a_class_object(_object) else _object
        print('{key} {depth}'.format(key=_key, depth=depth))
        if has_next_label(dictionary):
            object_depth_checker(data=dictionary, depth=depth + 1)


if __name__ == '__main__':
    class Person(object):
        def __init__(self, first_name, last_name, father):
            self.first_name = first_name
            self.last_name = last_name
            self.father = father

    person_a = Person('User', '1', None)
    person_b = Person('User', '2', person_a)
    a = {
        'key1': 1,
            'key2': {
                'key3': 1,
                    'key4': {
                        'key5': 4,
                        'user': person_b,
                    }
                }
            }

    object_depth_checker(a)