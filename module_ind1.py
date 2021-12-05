#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def main(replaceable, replacement):
    def replace(rep_str):
        if replacement == '' or replaceable == '' or rep_str == '':
            return None

        return re.sub(rf'({replaceable})\1+', replacement, rep_str)

    return replace
