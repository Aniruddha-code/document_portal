import yaml

path_value=r"D:\\PythonCode\\document_portal\\config\\config.yaml"
def load_config(config_path: str = path_value) -> dict:
    print(str)
    with open(config_path, "r") as file:
        config=yaml.safe_load(file)
    return config