#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scr import setting

import base64



class UserPwd:
    def __init__(self):
        self.master_state = False
        self.master_pwd = None
        self.mail_pwd = None

        self.user_obj = setting.UserSet("../scr/etc/users.json")
        try:
            self.user = self.user_obj.read_set
        except:
            self.user = dict()

    def set_master_pwd(self, pwd):
        self.master_pwd = str(pwd)

    @property
    def get_master_pwd(self):
        return self.master_pwd

    def set_pwd(self, pwd):
        self.mail_pwd = str(pwd)

    def get_pwd_user(self, mail):
        pwd = self.user.get(mail)
        if pwd is not None:
            return self.user.get(mail)[0]
        return None

    def set_pwd_in_file(self, key_mail):
        try:
            self.mail_pwd = self.user.get(key_mail)[0]
        except TypeError:
            return None

    @property
    def get_pwd(self):
        print(self.mail_pwd, "3333")
        return self.mail_pwd

    def set_master_state(self, state):
        self.master_state = state

    def compare_master_pwd(self, master_pwd, key_mail):
        if self.user.get(key_mail) is not None:
            m = base64.standard_b64decode(
                    self.user.get(key_mail)[1])
            if master_pwd == m:
                return True

    def get_decode_pwd(self, key_mail):
        p = self.user.get(key_mail)[0]
        print(p, 333)
        return base64.standard_b64decode(self.user.get(key_mail)[0])

    def save_pwd(self, key_mail):
        pwd = self.get_pwd
        master = self.get_master_pwd
        if pwd is not None or master is not None:
            pwd_encode = base64.standard_b64encode(pwd)
            master_encode = base64.standard_b64encode(master)
            self.user[key_mail] = [pwd_encode, master_encode]
            self.user_obj.save_set(self.user)

    def del_user(self, mail):
        try:
            del (self.user[mail])
        except KeyError:
            return
        else:
            self.user_obj.save_set(self.user)


if __name__ == '__main__':
    pwd = UserPwd()
    pwd.set_pwd_in_file("zaswed76@gmail.com")
    passw = pwd.get_pwd
    pwd.save_pwd("zaswed76@gmail.com")
