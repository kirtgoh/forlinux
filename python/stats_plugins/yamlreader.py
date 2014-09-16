import sys
import os
stats = sys.modules['__main__']

import yaml
try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader

# YAML Stats Reader class
class YAMLReader(stats.Readers):
    """
    Read the input file as YAML format.
    """

    def __init__(self):
        pass

    def set_options(self, parser):
        """ Add options to parser"""
        parser.add_option("-y", "--yaml", action="store_true", default=False,
                dest="yaml_file",
                help="Treat arguments as input YAML files")

    def load_yaml(self, file):
        docs = []

        for doc in yaml.load_all(file, Loader=Loader):
            doc['_file'] = file.name
            doc['_name'] = os.path.splitext(file.name)[0]
            docs.append(doc)

        return docs

    def read(self, options, args):
        """ Read yaml file if user give that option"""
        if options.yaml_file == True:
            docs = []
            for yf in args:
                l = lambda x: [ doc for doc in yaml.load_all(x, Loader=Loader)]
                with open(yf, 'r') as st_f:
                    docs += self.load_yaml(st_f)
            return docs
