#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 Andrea Mattioli - License: GNU General Public License v2
# Contact: andrea.mattiols@gmail.com

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
        Dictionary,
        Integer,
        Tuple,
        TextAscii,
        )
from cmk.gui.plugins.wato import (
        CheckParameterRulespecWithItem,
        CheckParameterRulespecWithoutItem,
        rulespec_registry,
        RulespecGroupCheckParametersEnvironment,
        )

def _parameter_valuespec_shelly_status():
    return Dictionary (
            title = _("SHELLY status via API"),
            optional_keys = ["Power", "Used"],
            elements = [
                ("Wifi_Power", Tuple (
                    title = _("Wifi Power signal"),
                    elements = [
                        Integer(title = _("Warning below"), default_value = 60),
                        Integer(title = _("Critical higher"), default_value = 40),
                    ],
                    )),

                ("Fs_Used", Tuple (
                    title = _("File System Used Size"),
                    elements = [
                        Integer(title = _("Warning below"), default_value = 80),
                        Integer(title = _("Critical higher"), default_value = 90),
                    ],
                    )),
                ("Ram_Used", Tuple (
                    title = _("Ram Used Size"),
                    elements = [
                        Integer(title = _("Warning below"), default_value = 80),
                        Integer(title = _("Critical higher"), default_value = 90),
                        ],
                    )),
                ],

            )

rulespec_registry.register (
        CheckParameterRulespecWithoutItem(
            check_group_name = "shelly_status",
            group = RulespecGroupCheckParametersEnvironment,
            match_type = "dict",
            parameter_valuespec = _parameter_valuespec_shelly_status,
            title = lambda: _("SHELLY status via API"),
            )
        )

