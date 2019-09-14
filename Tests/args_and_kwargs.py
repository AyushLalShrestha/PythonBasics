


def method(**kwargs):
    print kwargs


dict_1 = {
    'name': "Ayush Lal Shrestha",
    'l_name': "Shrestha"
}

dict_1.pop('name')
method(name="Ayush", **dict_1)

