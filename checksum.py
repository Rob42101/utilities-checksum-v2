#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Jan 12, 2024 02:06:25 AM GMT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import checksum_support

_bgcolor = "#d9d9d9"  # X11 color: 'gray85'
_fgcolor = "#000000"  # X11 color: 'black'
_tabfg1 = "black"
_tabfg2 = "white"
_bgmode = "light"
_tabbg1 = "#d9d9d9"
_tabbg2 = "gray40"

_style_code_ran = 0


def _style_code():
    global _style_code_ran
    if _style_code_ran:
        return
    checksum_support.root.tk.eval("set ::xframe #d9d9d9")
    checksum_support.root.tk.eval("set ::xfore #000000")
    checksum_support.root.tk.eval("set ::ana2color beige")
    checksum_support.root.tk.eval("set ::_tabfg1 black")
    checksum_support.root.tk.eval("set ::_tabfg2 white")
    checksum_support.root.tk.eval("set ::_tabbg1 #d9d9d9")
    checksum_support.root.tk.eval("set ::_tabbg2 gray40")
    checksum_support.root.tk.eval("set ::_bgmode light")
    try:
        checksum_support.root.tk.call(
            "source", os.path.join(_location, "themes", "page-legacy.tcl")
        )
    except:
        pass
    style = ttk.Style()
    style.theme_use("page-legacy")
    style.configure(".", font="-family {DejaVu Sans} -size 12")
    checksum_support.root.tk_setPalette(
        foreground="#000000",
        background="#d9d9d9",
        activeForeground="black",
        activeBackground="#d9d9d9",
        selectForeground="black",
        selectBackground="#d9d9d9",
    )
    _style_code_ran = 1


class Toplevel1:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
        top is the toplevel containing window."""

        top.geometry("696x676+586+222")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(0, 0)
        top.title("File Checksum V2")
        top.configure(background="#efefef")
        top.configure(highlightbackground="#efefef")

        self.top = top
        self.sha256h_Dgst = tk.StringVar()
        self.sha1h_Dgst = tk.StringVar()
        self.file_path = tk.StringVar()
        self.path = tk.StringVar()
        self.file_attributes = tk.StringVar()
        self.md5h_Dgst = tk.StringVar()
        self.sha512h_Dgst = tk.StringVar()
        self.status_txt = tk.StringVar()
        self.path_save = tk.IntVar()

        _style_code()
        self.TopLevel = ttk.Frame(self.top)
        self.TopLevel.place(x=0, y=0, height=676, width=696)
        self.TopLevel.configure(relief="sunken")
        self.TopLevel.configure(borderwidth="3")
        self.TopLevel.configure(relief="sunken")

        self.SHA256_Tf = ttk.Frame(self.TopLevel)
        self.SHA256_Tf.place(x=12, y=332, height=98, width=670)
        self.SHA256_Tf.configure(relief="sunken")
        self.SHA256_Tf.configure(borderwidth="2")
        self.SHA256_Tf.configure(relief="sunken")

        self.SHA256_Lbl = ttk.Label(self.SHA256_Tf)
        self.SHA256_Lbl.place(x=10, y=7, height=30, width=647)
        self.SHA256_Lbl.configure(font="-family {DejaVu Sans} -size 16")
        self.SHA256_Lbl.configure(relief="sunken")
        self.SHA256_Lbl.configure(anchor="center")
        self.SHA256_Lbl.configure(justify="center")
        self.SHA256_Lbl.configure(text="""SHA-256""")
        self.SHA256_Lbl.configure(compound="none")

        self.SHA256_Txt = tk.Text(self.SHA256_Tf)
        self.SHA256_Txt.place(x=10, y=67, height=25, width=648)
        self.SHA256_Txt.configure(background="#efefef")
        self.SHA256_Txt.configure(exportselection="0")
        self.SHA256_Txt.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.SHA256_Txt.configure(selectbackground="#d9d9d9")
        self.SHA256_Txt.configure(wrap="word")

        self.SHA256_Dgst = ttk.Label(self.SHA256_Tf)
        self.SHA256_Dgst.place(x=10, y=40, height=21, width=647)
        self.SHA256_Dgst.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.SHA256_Dgst.configure(relief="sunken")
        self.SHA256_Dgst.configure(anchor="w")
        self.SHA256_Dgst.configure(justify="left")
        self.SHA256_Dgst.configure(textvariable=self.sha256h_Dgst)
        self.sha256h_Dgst.set("""""")
        self.SHA256_Dgst.configure(compound="left")

        self.SHA1_Tf = ttk.Frame(self.TopLevel)
        self.SHA1_Tf.place(x=12, y=225, height=98, width=670)
        self.SHA1_Tf.configure(relief="sunken")
        self.SHA1_Tf.configure(borderwidth="2")
        self.SHA1_Tf.configure(relief="sunken")

        self.SHA1_Lbl = ttk.Label(self.SHA1_Tf)
        self.SHA1_Lbl.place(x=10, y=7, height=31, width=647)
        self.SHA1_Lbl.configure(font="-family {DejaVu Sans} -size 16")
        self.SHA1_Lbl.configure(relief="sunken")
        self.SHA1_Lbl.configure(anchor="center")
        self.SHA1_Lbl.configure(justify="center")
        self.SHA1_Lbl.configure(text="""SHA-1""")
        self.SHA1_Lbl.configure(compound="none")

        self.SHA1_Dgst = ttk.Label(self.SHA1_Tf)
        self.SHA1_Dgst.place(x=10, y=43, height=21, width=647)
        self.SHA1_Dgst.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.SHA1_Dgst.configure(relief="sunken")
        self.SHA1_Dgst.configure(anchor="w")
        self.SHA1_Dgst.configure(justify="left")
        self.SHA1_Dgst.configure(textvariable=self.sha1h_Dgst)
        self.sha1h_Dgst.set("""""")
        self.SHA1_Dgst.configure(compound="left")

        self.SHA1_Txt = tk.Text(self.SHA1_Tf)
        self.SHA1_Txt.place(x=10, y=68, height=25, width=648)
        self.SHA1_Txt.configure(background="#efefef")
        self.SHA1_Txt.configure(exportselection="0")
        self.SHA1_Txt.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.SHA1_Txt.configure(selectbackground="#d9d9d9")
        self.SHA1_Txt.configure(wrap="word")

        self.file_objects = ttk.Frame(self.TopLevel)
        self.file_objects.place(x=12, y=10, height=95, width=670)
        self.file_objects.configure(relief="sunken")
        self.file_objects.configure(borderwidth="1")
        self.file_objects.configure(relief="sunken")

        self.file_selector = ttk.Combobox(self.file_objects)
        self.file_selector.place(x=85, y=30, height=21, width=580)
        self.file_selector.configure(exportselection="0")
        self.file_selector.configure(font="-family {DejaVu Sans} -size 10")
        self.file_selector.configure(textvariable=self.file_path)

        self.dir_selector = ttk.Combobox(self.file_objects)
        self.dir_selector.place(x=85, y=5, height=21, width=580)
        self.dir_selector.configure(exportselection="0")
        self.dir_selector.configure(font="-family {DejaVu Sans} -size 10")
        self.dir_selector.configure(textvariable=self.path)

        self.name_Lbl = ttk.Label(self.file_objects)
        self.name_Lbl.place(x=3, y=30, height=21, width=80)
        self.name_Lbl.configure(font="-family {DejaVu Sans} -size 11")
        self.name_Lbl.configure(relief="sunken")
        self.name_Lbl.configure(anchor="w")
        self.name_Lbl.configure(justify="left")
        self.name_Lbl.configure(text="""File name:""")
        self.name_Lbl.configure(compound="left")

        self.path_Lbl = ttk.Label(self.file_objects)
        self.path_Lbl.place(x=3, y=5, height=21, width=80)
        self.path_Lbl.configure(font="-family {DejaVu Sans} -size 11")
        self.path_Lbl.configure(relief="sunken")
        self.path_Lbl.configure(anchor="w")
        self.path_Lbl.configure(justify="left")
        self.path_Lbl.configure(text="""File path:""")
        self.path_Lbl.configure(compound="left")

        self.path_save_check = tk.Checkbutton(self.file_objects)
        self.path_save_check.place(x=587, y=57, height=33, width=75)
        self.path_save_check.configure(activebackground="#d9d9d9")
        self.path_save_check.configure(background="#efefef")
        self.path_save_check.configure(command=checksum_support.on_path_save)
        self.path_save_check.configure(compound="left")
        self.path_save_check.configure(font="-family {DejaVu Sans} -size 12")
        photo_location = os.path.join(_location, "./icons/switchoff75.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.path_save_check.configure(image=_img0)
        self.path_save_check.configure(indicatoron="0")
        self.path_save_check.configure(justify="left")
        self.path_save_check.configure(offrelief="flat")
        self.path_save_check.configure(overrelief="flat")
        photo_location = os.path.join(_location, "./icons/switchon75.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.path_save_check.configure(selectimage=_img1)
        self.path_save_check.configure(variable=self.path_save)
        self.path_save_check_tooltip = ToolTip(
            self.path_save_check, """When on, the file path\nwill be saved, on exit."""
        )

        self.file_attributes_Lbl = ttk.Label(self.file_objects)
        self.file_attributes_Lbl.place(x=92, y=55, height=21, width=450)
        self.file_attributes_Lbl.configure(font="-family {DejaVu Sans} -size 11")
        self.file_attributes_Lbl.configure(relief="flat")
        self.file_attributes_Lbl.configure(anchor="w")
        self.file_attributes_Lbl.configure(justify="left")
        self.file_attributes_Lbl.configure(textvariable=self.file_attributes)
        self.file_attributes.set("""""")
        self.file_attributes_Lbl.configure(compound="left")

        self.MD5_Tf = ttk.Frame(self.TopLevel)
        self.MD5_Tf.place(x=12, y=116, height=98, width=670)
        self.MD5_Tf.configure(relief="sunken")
        self.MD5_Tf.configure(borderwidth="2")
        self.MD5_Tf.configure(relief="sunken")

        self.MD5H_Dgst = ttk.Label(self.MD5_Tf)
        self.MD5H_Dgst.place(x=10, y=41, height=21, width=648)
        self.MD5H_Dgst.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.MD5H_Dgst.configure(relief="sunken")
        self.MD5H_Dgst.configure(anchor="w")
        self.MD5H_Dgst.configure(justify="left")
        self.MD5H_Dgst.configure(textvariable=self.md5h_Dgst)
        self.md5h_Dgst.set("""""")
        self.MD5H_Dgst.configure(compound="left")

        self.MD5_Lbl = ttk.Label(self.MD5_Tf)
        self.MD5_Lbl.place(x=10, y=5, height=31, width=647)
        self.MD5_Lbl.configure(font="-family {DejaVu Sans} -size 16")
        self.MD5_Lbl.configure(relief="sunken")
        self.MD5_Lbl.configure(anchor="center")
        self.MD5_Lbl.configure(justify="center")
        self.MD5_Lbl.configure(text="""MD5""")
        self.MD5_Lbl.configure(compound="none")

        self.MD5_Txt = tk.Text(self.MD5_Tf)
        self.MD5_Txt.place(x=10, y=67, height=25, width=648)
        self.MD5_Txt.configure(background="#efefef")
        self.MD5_Txt.configure(exportselection="0")
        self.MD5_Txt.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.MD5_Txt.configure(selectbackground="#d9d9d9")
        self.MD5_Txt.configure(wrap="word")

        self.SHA512_Tf = ttk.Frame(self.TopLevel)
        self.SHA512_Tf.place(x=12, y=439, height=142, width=670)
        self.SHA512_Tf.configure(relief="sunken")
        self.SHA512_Tf.configure(borderwidth="2")
        self.SHA512_Tf.configure(relief="sunken")

        self.SHA512_Txt = tk.Text(self.SHA512_Tf)
        self.SHA512_Txt.place(x=10, y=90, height=43, width=648)
        self.SHA512_Txt.configure(background="#efefef")
        self.SHA512_Txt.configure(exportselection="0")
        self.SHA512_Txt.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.SHA512_Txt.configure(selectbackground="#d9d9d9")
        self.SHA512_Txt.configure(wrap="word")

        self.SHA512_Dgst = ttk.Label(self.SHA512_Tf)
        self.SHA512_Dgst.place(x=10, y=42, height=43, width=647)
        self.SHA512_Dgst.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.SHA512_Dgst.configure(relief="sunken")
        self.SHA512_Dgst.configure(anchor="w")
        self.SHA512_Dgst.configure(justify="left")
        self.SHA512_Dgst.configure(wraplength="642")
        self.SHA512_Dgst.configure(textvariable=self.sha512h_Dgst)
        self.sha512h_Dgst.set("""""")
        self.SHA512_Dgst.configure(compound="left")

        self.SHA512_Lbl = ttk.Label(self.SHA512_Tf)
        self.SHA512_Lbl.place(x=10, y=7, height=31, width=647)
        self.SHA512_Lbl.configure(font="-family {DejaVu Sans} -size 16")
        self.SHA512_Lbl.configure(relief="sunken")
        self.SHA512_Lbl.configure(anchor="center")
        self.SHA512_Lbl.configure(justify="center")
        self.SHA512_Lbl.configure(text="""SHA-512""")
        self.SHA512_Lbl.configure(compound="none")

        self.SaveBtn = ttk.Button(self.TopLevel)
        self.SaveBtn.place(x=210, y=595, height=30, width=170)
        self.SaveBtn.configure(command=checksum_support.on_save)
        self.SaveBtn.configure(text="""Save Hash Values""")
        self.SaveBtn.configure(compound="left")

        self.QuitBtn = ttk.Button(self.TopLevel)
        self.QuitBtn.place(x=510, y=610, height=30, width=120)
        self.QuitBtn.configure(command=checksum_support.on_quit)
        self.QuitBtn.configure(text="""Exit""")
        self.QuitBtn.configure(compound="left")

        self.status_Lbl = ttk.Label(self.TopLevel)
        self.status_Lbl.place(x=25, y=637, height=24, width=355)
        self.status_Lbl.configure(font="-family {DejaVu Sans} -size 12")
        self.status_Lbl.configure(relief="sunken")
        self.status_Lbl.configure(anchor="w")
        self.status_Lbl.configure(justify="left")
        self.status_Lbl.configure(textvariable=self.status_txt)
        self.status_txt.set("""""")
        self.status_Lbl.configure(compound="none")

        self.VerifyBtn = ttk.Button(self.TopLevel)
        self.VerifyBtn.place(x=25, y=595, height=30, width=170)
        self.VerifyBtn.configure(command=checksum_support.on_verify)
        self.VerifyBtn.configure(text="""Verify Hash Values""")
        self.VerifyBtn.configure(compound="left")


from time import time, localtime, strftime


class ToolTip(tk.Toplevel):
    """Provides a ToolTip widget for Tkinter."""

    def __init__(self, wdgt, msg=None, msgFunc=None, delay=0.5, follow=True):
        self.wdgt = wdgt
        self.parent = self.wdgt.master
        tk.Toplevel.__init__(self, self.parent, bg="black", padx=1, pady=1)
        self.withdraw()
        self.overrideredirect(True)
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set("No message provided")
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        self.msg = tk.Message(
            self,
            textvariable=self.msgVar,
            bg=_bgcolor,
            fg=_fgcolor,
            font="-family {DejaVu Sans} -size 12",
            aspect=1000,
        )
        self.msg.grid()
        self.wdgt.bind("<Enter>", self.spawn, "+")
        self.wdgt.bind("<Leave>", self.hide, "+")
        self.wdgt.bind("<Motion>", self.move, "+")

    def spawn(self, event=None):
        self.visible = 1
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        self.lastMotion = time()
        if self.follow is False:
            self.withdraw()
            self.visible = 1
        self.geometry("+%i+%i" % (event.x_root + 20, event.y_root - 10))
        try:
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        self.visible = 0
        self.withdraw()

    def update(self, msg):
        self.msgVar.set(msg)

    def configure(self, **kwargs):
        backgroundset = False
        foregroundset = False
        # Get the current tooltip text just in case the user doesn't provide any.
        current_text = self.msgVar.get()
        # to clear the tooltip text, use the .update method
        if "debug" in kwargs.keys():
            debug = kwargs.pop("debug", False)
            if debug:
                for key, value in kwargs.items():
                    print(f"key: {key} - value: {value}")
        if "background" in kwargs.keys():
            background = kwargs.pop("background")
            backgroundset = True
        if "bg" in kwargs.keys():
            background = kwargs.pop("bg")
            backgroundset = True
        if "foreground" in kwargs.keys():
            foreground = kwargs.pop("foreground")
            foregroundset = True
        if "fg" in kwargs.keys():
            foreground = kwargs.pop("fg")
            foregroundset = True

        fontd = kwargs.pop("font", None)
        if "text" in kwargs.keys():
            text = kwargs.pop("text")
            if (text == "") or (text == "\n"):
                text = current_text
            else:
                self.msgVar.set(text)
        reliefd = kwargs.pop("relief", "flat")
        justifyd = kwargs.pop("justify", "left")
        padxd = kwargs.pop("padx", 1)
        padyd = kwargs.pop("pady", 1)
        borderwidthd = kwargs.pop("borderwidth", 2)
        wid = self.msg  # The message widget which is the actual tooltip
        if backgroundset:
            wid.config(bg=background)
        if foregroundset:
            wid.config(fg=foreground)
        wid.config(font=fontd)
        wid.config(borderwidth=borderwidthd)
        wid.config(relief=reliefd)
        wid.config(justify=justifyd)
        wid.config(padx=padxd)
        wid.config(pady=padyd)


#                   End of Class ToolTip


def start_up():
    checksum_support.main()


if __name__ == "__main__":
    checksum_support.main()
