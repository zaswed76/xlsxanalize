#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class UserSet:
    def __init__(self, path):
        self.path = path


    @property
    def read_set(self):
        with open(self.path, "r") as json_obj:
            return json.load(json_obj)

    def save_set(self, obj):
        with open(self.path, "w") as json_obj:
            json.dump(obj, json_obj, indent=2)