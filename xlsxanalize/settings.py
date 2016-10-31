#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml


def load_config(file):
    return yaml.load(open(file))


if __name__ == '__main__':
    print(load_config(r'D:\0SYNC\python_projects\xlsxanalize\xlsxanalize\etc\settings'))