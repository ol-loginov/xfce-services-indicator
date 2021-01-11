#!/usr/bin/env python
#
# Copyright 2009-2012 Canonical Ltd.
#
# Authors: Neil Jagdish Patel <neil.patel@canonical.com>
#          Jono Bacon <jono@ubuntu.com>
#          David Planella <david.planella@ubuntu.com>
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of either or both of the following licenses:
#
# 1) the GNU Lesser General Public License version 3, as published by the 
# Free Software Foundation; and/or
# 2) the GNU Lesser General Public License version 2.1, as published by 
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the applicable version of the GNU Lesser General Public 
# License for more details.
#
# You should have received a copy of both the GNU Lesser General Public 
# License version 3 and version 2.1 along with this program.  If not, see 
# <http://www.gnu.org/licenses/>
#

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk
from gi.repository import AppIndicator3 as AppIndicator

import subprocess
import re

service_menu_items = list()


class ServicesCommand:
    def list(self):
        output = subprocess.check_output(['service', '--status-all']).decode('utf-8')
        for line in output.split('\n'):
            parts = re.match('\\s\\[(.*)]\\s+(.*)', line)
            if parts is not None:
                status = parts.group(1).strip()
                name = parts.group(2)
                yield name, status


def menu_quit(w):
    Gtk.main_quit()


def menu_refresh(w):
    refresh_services_list()


def menu_activate_noop(w):
    pass


def menuitem_create(label, activate_callback=menu_activate_noop):
    item = Gtk.MenuItem(label=label)
    item.connect("activate", activate_callback)
    item.show()
    return item


def refresh_services_list():
    for mi in menu_services:
        menu.remove(mi)

    for (name, status) in get_command().list():
        menuitem = menuitem_create('%s [%s]' % (name, status))
        menu_services.append(menuitem)

        menu.append(menuitem)


def get_command():
    return ServicesCommand()


if __name__ == "__main__":
    ind = AppIndicator.Indicator.new("Services List", "indicator-messages", AppIndicator.IndicatorCategory.APPLICATION_STATUS)
    ind.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    # ind.set_attention_icon("indicator-messages-new")

    # create a menu
    menu = Gtk.Menu()
    menu_services = list()

    # create some
    menu.append(menuitem_create("Refresh", menu_refresh))
    menu.append(menuitem_create("Quit", menu_quit))

    separator = Gtk.SeparatorMenuItem()
    separator.show()
    menu.append(separator)

    # menuitem_register("Test-undermenu - %d" % 1)
    # menuitem_register("Test-undermenu - %d" % 2)
    # menuitem_register("Test-undermenu - %d" % 3)

    ind.set_menu(menu)

    refresh_services_list()

    Gtk.main()
