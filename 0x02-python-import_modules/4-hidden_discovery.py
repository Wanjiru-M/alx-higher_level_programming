#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    module_dir = dir(hidden_4)
    visible_attributes = [item for item in module_dir if not item.startswith('__')]
    for attribute in visible_attributes:
        print(attribute)
