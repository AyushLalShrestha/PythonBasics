import argparse

parser = argparse.ArgumentParser()
parser.add_argumet('-u', '--user')
parser.add_argumet('-c', '--color')
namespace = parser.parse_args([])

d = ChainMap(dict_1, dict_2, dict_3)