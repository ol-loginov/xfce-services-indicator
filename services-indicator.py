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


def menu_activate_quit(w):
    Gtk.main_quit()


def menu_activate_noop(w):
    pass


def menuitem_register(label, activate_callback=menu_activate_noop):
    menu_items = Gtk.MenuItem(label=label)
    menu_items.connect("activate", activate_callback)
    menu_items.show()

    menu.append(menu_items)


if __name__ == "__main__":
    ind = AppIndicator.Indicator.new("Services List", "indicator-messages", AppIndicator.IndicatorCategory.APPLICATION_STATUS)
    ind.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    # ind.set_attention_icon("indicator-messages-new")

    # create a menu
    menu = Gtk.Menu()

    # create some
    menuitem_register("Test-undermenu - %d" % 1)
    menuitem_register("Test-undermenu - %d" % 2)
    menuitem_register("Test-undermenu - %d" % 3)
    menuitem_register("Quit", menu_activate_quit)

    ind.set_menu(menu)

    Gtk.main()
