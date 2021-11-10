#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 Andrea Mattioli - License: GNU General Public License v2
# Contact: andrea.mattiols@gmail.com

# Agent output:
#<<<shelly_status>>>
#NAME : cucina
#Wifi_Power : -65
#Ipv4_Method : static
#UpToDate : False
#Ram_Total : 50872
#Ram_Free : 39420
#Ram_Used : 11
#Fs_Size : 233681
#Fs_Free : 150098
#Fs_Used : 20
#Uptime : 262293

from .agent_based_api.v1 import *
import pprint
import datetime

intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)

def display_time(seconds, granularity=5):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ' '.join(result[:granularity])

def parse_shellystatus(string_table):
    shellyname = "Shelly"
    name = " "
    parsed = []
    for line in string_table:
        if line[0] == "NAME":
            try:
              name = line[2]
            except:
              name = None
        if line[0] in ["Wifi_Power", "Ipv4_Method", "UpToDate", "Ram_Used", "Fs_Used", "Uptime"]:
            element = []
            description = "UNKNOWN"
            if (line[0] == "Wifi_Power"):
               description = "Wifi Power Signal"
            elif (line[0] == "Ipv4_Method"):
                description = "Ipv4 Method"
            elif (line[0] == "UpToDate"):
                description = "New Update Available"
            elif (line[0] == "Ram_Used"):
                description = "Ram In Use"
            elif (line[0] == "Fs_Used"):
                description = "File System In Use"
            elif (line[0] == "Uptime"):
                description = "Uptime"                
            if name != None:
                element.append(name + " " + description)
            else:
                element.append(shellyname + " " + description)
            element.append(line[0])
            element.append(line[2])
            parsed.append(element)
    return parsed

def discover_shellystatus(section):
    for sector, used, slots in section:
        yield Service(item=sector)

def check_shellystatus(item,params,section):
    Wifi_Power_warn = params['Wifi_Power'][0]
    Wifi_Power_crit = params['Wifi_Power'][1]
    Ram_Used_warn = params['Ram_Used'][0]
    Ram_Used_crit = params['Ram_Used'][1]
    Fs_Used_warn = params['Fs_Used'][0]
    Fs_Used_crit = params['Fs_Used'][1]
    for sector, used, slots in section:
        if sector == item:
            s = State.UNKNOWN;
            report = "not found"
            if used == "Wifi_Power":
                slots = int(slots)
                report = str(slots) + " db"
                if slots <= Wifi_Power_crit:
                    s = State.CRIT
                elif slots <= Wifi_Power_warn:
                    s = State.WARN
                else:
                    s = State.OK
                yield Metric( "Wifi_Power", slots, boundaries=(-100, 100), levels=(Wifi_Power_warn, Wifi_Power_crit))
            elif used == "Ipv4_Method":
                report = slots
                if slots == "static":
                    s = State.OK
                else:
                    s = State.WARN
            elif used == "UpToDate":
                if slots == "True":
                    report = "False"
                    s = State.OK
                else:
                    report = "True"
                    s = State.WARN                    
            elif used == "Ram_Used":
                slots = float(slots)
                report = str(slots) + "%"
                if slots >= Ram_Used_crit:
                    s = State.CRIT
                elif slots >= Ram_Used_warn:
                    s = State.WARN
                else:
                    s = State.OK
                yield Metric( "Ram_Used", slots, boundaries=(0, 100),levels=(Ram_Used_warn, Ram_Used_crit))

            elif used == "Fs_Used":
                slots = float(slots)
                report = str(slots) + "%"
                if slots >= Fs_Used_crit:
                    s = State.CRIT
                elif slots >= Fs_Used_warn:
                    s = State.WARN
                else:
                    s = State.OK
                yield Metric( "Fs_Used", slots, boundaries=(0, 100),levels=(Fs_Used_warn, Fs_Used_crit))
            
            elif used == "Uptime":
                report = "Uptime: "+display_time(int(slots))
                s = State.OK
                yield Metric("Uptime", int(slots))
            
            yield Result(state=s, summary=report)
            return

register.agent_section(
        name="shelly_status",
        parse_function=parse_shellystatus,
)

register.check_plugin(
        name = "shelly_status",
        service_name = "Shelly %s",
        discovery_function = discover_shellystatus,
        check_function = check_shellystatus,
        check_default_parameters = {
            'Wifi_Power': (-67, -100),
            'Ram_Used': (80, 90),
            'Fs_Used': (80, 90)},
        check_ruleset_name = "shelly_status",
)
