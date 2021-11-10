#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 Andrea Mattioli - License: GNU General Public License v2
# Contact: andrea.mattiols@gmail.com

from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import (metric_info, graph_info, perfometer_info)

metric_info["Wifi-Power"] = {
        "title": _("Wifi Power Signal"),
        "unit": "db",
        "color": "26/a",
        }

metric_info["Fs_Used"] = {
        "title": _("File System Used Size"),
        "unit": "%",
        "color": "25/a",
        }

metric_info["Ram_Used"] = {
        "title": _("Ram Used Size"),
        "unit": "%",
        "color": "24/a",
        }

perfometer_info.append({ "type": "linear", "segments": ["Wifi-Power"], "total": 100})
perfometer_info.append({ "type": "linear", "segments": ["Fs_Used"], "total": 100})
perfometer_info.append({ "type": "linear", "segments": ["Ram_Used"], "total": 100})
