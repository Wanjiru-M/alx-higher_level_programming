#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    visible_attributes = [
        attribute for attribute in dir(hidden_4) if not attribute.startswith('__')
    ]

    for attribute in visible_attributes:
        print(attribute)
