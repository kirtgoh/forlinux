#!/usr/bin/env python

# stats.py
#
# This is a helper script to manipulate Marss and DRAMSim2 statistics (YAML,
# time based etc.). Please run --help to list all the options.
#
# This script is provided under LGPL licence.
#
# Author: Kirt Goh (kirtgoh@gmail.com) Copyright 2014
#

import os
import sys
import re
import operator

from optparse import OptionParser,OptionGroup

# Standard Logging and Error reporting functions
def log(msg):
    print(msg)

def debug(msg):
    print("[DEBUG] : %s" % msg)

def error(msg):
    print("[ERROR] : %s" % msg)
    sys.exit(-1)

# Base plugin Metaclass
class PluginBase(type):
    """
    A Metaclass for reader and write plugins.
    """

    def __init__(self, class_name, bases, namespace):
        if not hasattr(self, 'plugins'):
            self.plugins = []
        else:
            self.plugins.append(self)

    def __str__(self):
        return self.__name__

    def get_plugins(self, *args, **kwargs):
        return sorted(self.plugins, key=lambda x: x.order)

    def set_opt_parser(self, parser):
        for plugin in self.plugins:
            assert hasattr(plugin, 'set_options')
            p = plugin()
            p.set_options(parser)

# Reader Plugin Base Class
class Readers(object):
    """
    Base class for all Reader plugins.
    """
    __metaclass__ = PluginBase
    order = 0

    def read(options, args):
        stats = []
        for plugin in Readers.get_plugins():
            p = plugin()
            st = p.read(options, args)
            if type(st) == list:
                stats.extend(st)
            elif st:
                stats.append(st)

        return stats
    read = staticmethod(read)

# Writer Plugin Base Class
class Writers(object):
    """
    Base class for all Writer plugins.
    """
    __metaclass__ = PluginBase
    order = 0

    def write(stats, options):
        for plugin in Writers.get_plugins():
            p = plugin()
            p.write(stats, options)

        return stats
    write = staticmethod(write)

# Filter Plugin Base Class
class Filters(object):
    """
    Base class for all Filter plugins.
    """
    __metaclass__ = PluginBase
    order = 0

    def filter(stats, options):
        for plugin in Filters.get_plugins():
            p = plugin()
            stats = p.filter(stats, options)

        return stats
    filter = staticmethod(filter)

# Process Plugin Base Class
class Process(object):
    """
    Base class for Operator plugins. These plugins are run after filters and
    before writers to perform user specific operations on selected data. For
    example user can add or subtract from selected nodes.
    """
    __metaclass__ = PluginBase
    order = 0

    def process(stats, options):
        for plugin in Process.get_plugins():
            p = plugin()
            stats = p.process(stats, options)

        return stats
    process = staticmethod(process)

def setup_options():
    opt = OptionParser("usage: %prog [options] args")

    opt_setup = lambda x,y: y.set_opt_parser(x) or opt.add_option_group(x)

    read_opt = OptionGroup(opt, "Input Options")
    opt_setup(read_opt, Readers)

    filter_opt = OptionGroup(opt, "Stats Filtering Options")
    opt_setup(filter_opt, Filters)

    process_opt = OptionGroup(opt, "PostProcess Options")
    opt_setup(process_opt, Process)

    write_opt = OptionGroup(opt, "Output Options")
    opt_setup(write_opt, Writers)

    return opt

def execute(options, args):
    """ Run this script with given options to generate user specific output"""

    # First read in all the stats
    stats = Readers.read(options, args)

    stats = Filters.filter(stats, options)

    stats = Process.process(stats, options)

    Writers.write(stats, options)

def load_plugins():
    exec_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    sys.path.append(exec_dir)
    path = "%s/stats_plugins" % (exec_dir)
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".py") and not name.startswith("__"):
                path = os.path.join("stats_plugins", name)
                path = path [1:] if path[0] == '/' else path
                plugin_name = path.rsplit('.',1)[0].replace('/','.')
                # debug("try to load plugin: %s" % plugin_name)
                try:
                    __import__(plugin_name)
                except Exception as e:
                    debug("Unable to load plugin: %s" % plugin_name)
                    debug("Exception %s" % str(e))
                    

if __name__ == "__main__":
    load_plugins()

    opt = setup_options()
    (options, args) = opt.parse_args()

    if args == None or args == []:
        opt.print_help()
        sys.exit(-1)

    execute(options, args)
