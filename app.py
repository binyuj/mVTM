#!/usr/bin/env python
# coding:utf-8

import os
import pygtk
pygtk.require('2.0')
import gtk
import vte

apps = {"goagent": ['/usr/bin/env', 'python', './goagent/local/proxy.py'],
        "gsnova": ['./gsnova/gsnova'],
        "shadowsocks": ['/usr/bin/env', 'python', './shadowsocks/local.py'],
        "ssh": ['./ssh/auto_ssh.sh']}
        
logo_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app.png")
LOGO_DATA = "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"
pos = 2   #(0, 1, 2, 3) (POS_LEFT, POS_RIGHT, POS_TOP, POS_BOTTOM)  #tab显示位置

if not os.path.isfile(logo_file):
    import base64
    with open(logo_file, 'wb') as fp:
        fp.write(base64.b64decode(LOGO_DATA))

class App(object):
    """docstring for App"""
    def __init__(self):
        super(App, self).__init__()
        #Create a window
        self.window = gtk.Window()
        self.window.connect("destroy", lambda x: gtk.main_quit())
        self.window.set_size_request(600, 400)
        self.window.set_border_width(5)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_icon_from_file(logo_file)
        self.window.connect('delete-event', self.delete_event)

        #Create a notebook
        self.notebook = gtk.Notebook()
        self.notebook.set_tab_pos(pos)
        self.notebook.set_scrollable(True)
        #self.notebook.set_show_border(True)
        self.window.add(self.notebook)

        for item in sorted(apps):
            self.create_tab(item + "窗口", apps[item])

        #Show everything
        self.window.show_all()

        self.trayicon = gtk.StatusIcon()
        self.trayicon.set_from_file(logo_file)
        self.trayicon.connect('popup-menu', lambda i, b, t: self.make_menu().popup(None, None, gtk.status_icon_position_menu, b, t, self.trayicon))
        self.trayicon.connect('activate', self.show_hide_toggle)
        self.trayicon.set_tooltip('APP is running')
        self.trayicon.set_visible(True)


    def create_tab(self, title, command):
        #hbox will be used to store a label and button, as notebook tab title
        hbox = gtk.HBox(False, 0)
        label = gtk.Label(title)
        hbox.pack_start(label)

        #get a stock close button image
        close_image = gtk.image_new_from_stock(gtk.STOCK_CLOSE, gtk.ICON_SIZE_MENU)
        image_w, image_h = gtk.icon_size_lookup(gtk.ICON_SIZE_MENU)
        
        #make the close button
        btn = gtk.Button()
        btn.set_relief(gtk.RELIEF_NONE)
        btn.set_focus_on_click(False)
        btn.add(close_image)
        hbox.pack_start(btn, False, False)
        
        #this reduces the size of the button
        style = gtk.RcStyle()
        style.xthickness = 0
        style.ythickness = 0
        btn.modify_style(style)

        hbox.show_all()
        
        #tab content
        vbox = gtk.VBox()
        vbox.show()

        ### my vte
        #command  = ['/usr/bin/env', 'python', '-V']
        self.terminal = vte.Terminal()
        self.childpid = self.terminal.fork_command(command[0], command, os.getcwd())

        vbox.pack_start(self.terminal)
        
        #add the tab
        self.notebook.append_page(vbox, hbox)
        
        #connect the close button
        btn.connect('clicked', self.on_closetab_button_clicked, vbox)

    def on_closetab_button_clicked(self, sender, vbox):
        #get the page number of the tab we wanted to close
        pagenum = self.notebook.page_num(vbox)
        #and close it
        self.notebook.remove_page(pagenum)
    

           
    def make_menu(self):
        menu = gtk.Menu()
        itemlist = [(u'\u663e\u793a', self.on_show),
                    (u'\u9690\u85cf', self.on_hide),
                    (u'\u9000\u51fa', lambda x:gtk.main_quit())]
        for text, callback in itemlist:
            item = gtk.MenuItem(text)
            item.connect('activate', callback)
            item.show()
            menu.append(item)
        menu.show()
        return menu


    def on_show(self, widget, data=None):
        self.window.show_all()
        self.window.present()

    def on_hide(self, widget, data=None):
        self.window.hide_all()
    
    def show_hide_toggle(self, widget, data= None):
        if self.window.get_property('visible'):
            self.on_hide(widget, data)
        else:
            self.on_show(widget, data)

    def delete_event(self, widget, data=None):
        self.on_hide(widget, data)
        # 默认最小化至托盘
        return True

if __name__ == '__main__':
    app = App()
    gtk.main()