#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2015             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.
#
#
# file: shelly_services.py
#
# created: 11/2021
#
# Author: Andrea Mattioli
# email: andrea.mattiols@gmail.com
#
#

group = "datasource_programs"
register_rule(group,
              "special_agents:shelly_status",
              Dictionary(elements=[
                  ("username", TextAscii(title=_("Username"),
                                         allow_empty=True,
                                         )
                   ),
                  ("password", Password(title=_("Password"),
                                        allow_empty=True,
                                        )
                   ),

                  ("hostname", TextAscii(title=_("Custom SHELLY name"),
                                        allow_empty=True,
                                        )
                   )]),
              title=_("Check SHELLY Services "),
              help=_("This rule selects the Shelly agent instead of the "
                     "Check_MK Agent and allows monitoring of the Shelly "
                     "status using its HTTP API. "
                     "You can configure your connection settings here."),
              )
