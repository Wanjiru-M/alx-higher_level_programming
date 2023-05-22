#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util
    module_name = "hidden_4"
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print(f"Module {module_name} not found.")
    else:
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        visible_attributes = [
            attribute for attribute in dir(module) if not attribute.startswith("__")
        ]
        for attribute in visible_attributes:
            print(attribute)
