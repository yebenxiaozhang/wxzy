import yaml

with open("wxzy.ini.yaml", encoding="utf-8") as fs:
    data = yaml.load(fs, yaml.FullLoader)
    print(data)
    for key, value in data.items():
        print(key)
        print(value)


