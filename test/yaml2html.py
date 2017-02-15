#!/usr/bin/env python
# encoding: utf-8
"""
Convert YAML files to a big HTML file showing all the emoji images
"""
from __future__ import print_function, unicode_literals
import argparse
import glob
import os
import sys
import yaml  # pip install pyyaml


def load_yaml(filename):
    """
    Load YAML data from a file
    """
    with open(filename) as f:
        # yaml.BaseLoader leaves everything as a string,
        # so doesn't convert "no" to False
        data = yaml.load(f, Loader=yaml.BaseLoader)
    return data


def name_from_path(path):
    """Given 'packs/frontend.yaml' return 'frontend'"""
    basename = os.path.basename(path)
    return os.path.splitext(basename)[0]


def yaml2html(yaml_filename):
    """
    Given emojipack YAML filename, print HTML file showing the emoji images
    """

    data = load_yaml(yaml_filename)

    name = name_from_path(yaml_filename)

    print('<h2 id={}><a href=#{}>#</a> {} <a href=#top>{}</a></h2>'.format(
        name, name, yaml_filename, "&#x2191;"))
    print('<ul>')

    for emoji in data["emojis"]:

        print('<li><img src="{}"><p>{}</p></li>'.format(
            emoji['src'], emoji['name']))

    print("</ul>")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Convert YAML files to a big HTML file "
                    "showing all the emoji images",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('inspec', nargs='?',
                        help="Input file spec")
    args = parser.parse_args()

    if args.inspec:
        filenames = glob.glob(args.inspec)
        if not filenames:
            sys.exit("No input files found matching " + args.inspec)

    # Idea: make individual HTML files per YAML instead of one big one.

    print('<link rel="stylesheet" href="style.css">')
    print("<title>emojipacks</title>")
    print('<h1 id="top">emojipacks</h1>')

    print('<ol>')
    for filename in filenames:
        name = name_from_path(filename)
        print('<li><a href="#{}">{}</a></li>'.format(name, name))
    print("</ol>")

    for filename in filenames:
        yaml2html(filename)

# End of file
