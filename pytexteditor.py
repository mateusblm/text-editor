import platform
from tkinter import*
from tkinter.filedialog import asksaveasfile, askopenfilename
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


class PyTextEditor:
    def __init__(self):
        self.condicsave = False
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font9 = "Arial 9 bold"

        self.top = tk.Tk()
        self.top.resizable(False, False)
        self.top.geometry("600x449+654+190")
        self.top.minsize(1, 1)
        self.top.maxsize(1905, 1050)
        self.top.resizable(False, False)
        self.top.title("Document")
        self.top.configure(relief="ridge")
        self.top.configure(background="#383838")
        self.menubar = tk.Menu(self.top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.top.configure(menu=self.menubar)

        self.Entry1 = ScrolledText(self.top)
        self.Entry1.place(
            relx=0.02, rely=0.089,height=400, relwidth=0.96)
        self.Entry1.configure(background="#494949")
        self.Entry1.configure(font="Arial 12")
        self.Entry1.configure(foreground="white")
        self.Entry1.configure(relief="flat")
        self.Entry1.configure(selectbackground="white")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(insertborderwidth="3")
        self.Entry1.configure(wrap="none")

        self.Button1 = tk.Button(self.top, command=self.Clear, padx=40, pady=20)
        self.Button1.place(relx=0.02, rely=0.018, height=28, width=58)
        self.Button1.configure(background="#494949")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(relief="flat")
        self.Button1.configure(text='''Clear''')

        self.Button2 = tk.Button(self.top, command=self.SaveButton, padx=40, pady=20)
        self.Button2.place(relx=0.13, rely=0.018, height=28, width=58)
        self.Button2.configure(background="#494949")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(relief="flat")
        self.Button2.configure(text='''Save''')

        self.Button3 = tk.Button(self.top, command=self.Exit)
        self.Button3.place(relx=0.35, rely=0.018, height=28, width=58)
        self.Button3.configure(background="#ff0000")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(relief="flat")
        self.Button3.configure(text='''Exit''')

        self.Button4 = tk.Button(self.top, command=self.Open)
        self.Button4.place(relx=0.24, rely=0.018, height=28, width=58)
        self.Button4.configure(background="green")
        self.Button4.configure(font=font9)
        self.Button4.configure(foreground="#ffffff")
        self.Button4.configure(relief="flat")
        self.Button4.configure(text='''Open''')
        """ Working on!
        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.8, rely=0.028, height=18, width=59)
        self.Label1.configure(background="#383838")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Font Size''')
        self.Spinbox1 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.9, rely=0.022, relheight=0.045
                            , relwidth=0.078)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(font="TkDefaultFont")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(selectbackground="blue")
        self.Spinbox1.configure(selectforeground="white")
        """
        self.top.mainloop()
        self.top = tk.Tk

    def ExitPage(self):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {helvetica} -size 11 -weight bold"
        font12 = "-family {lucida} -size 9"
        font13 = "-family {charter} -size 9"

        self.exitpage = tk.Tk()
        self.exitpage.resizable(False, False)
        self.exitpage.geometry("426x151+985+452")
        self.exitpage.minsize(1, 1)
        self.exitpage.maxsize(1905, 1050)
        self.exitpage.resizable(1, 1)
        self.exitpage.title("")
        self.exitpage.configure(background="#383838")

        self.LabelExit1 = tk.Label(self.exitpage)
        self.LabelExit1.place(relx=0.082, rely=0.0, height=56, width=355)
        self.LabelExit1.configure(background="#383838")
        self.LabelExit1.configure(font=font10)
        self.LabelExit1.configure(foreground="#ffffff")
        self.LabelExit1.configure(text='''Save changes to document before closing?''')

        self.menubar = tk.Menu(self.exitpage,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.exitpage.configure(menu = self.menubar)

        self.ButtonExit1 = tk.Button(self.exitpage, command=self.Exit1)
        self.ButtonExit1.place(relx=0.0, rely=0.662, height=48, width=143)
        self.ButtonExit1.configure(background="#c11111")
        self.ButtonExit1.configure(font=font13)
        self.ButtonExit1.configure(foreground="#ffffff")
        self.ButtonExit1.configure(relief="flat")
        self.ButtonExit1.configure(text='''Close without saving''')

        self.ButtonExit2 = tk.Button(self.exitpage, command=self.Exit2)
        self.ButtonExit2.place(relx=0.34, rely=0.662, height=48, width=143)
        self.ButtonExit2.configure(activebackground="#f9f9f9")
        self.ButtonExit2.configure(background="#4f4f4f")
        self.ButtonExit2.configure(font=font12)
        self.ButtonExit2.configure(foreground="#ffffff")
        self.ButtonExit2.configure(relief="flat")
        self.ButtonExit2.configure(text='''Cancel''')

        self.ButtonExit3 = tk.Button(self.exitpage, command=self.Exit3)
        self.ButtonExit3.place(relx=0.681, rely=0.662, height=48, width=143)
        self.ButtonExit3.configure(activebackground="#f9f9f9")
        self.ButtonExit3.configure(background="#4f4f4f")
        self.ButtonExit3.configure(foreground="#ffffff")
        self.ButtonExit3.configure(relief="flat")
        self.ButtonExit3.configure(text='''Save As...''')

        self.LabelExit2 = tk.Label(self.exitpage)
        self.LabelExit2.place(relx=0.164, rely=0.265, height=18, width=285)
        self.LabelExit2.configure(background="#383838")
        self.LabelExit2.configure(font=font12)
        self.LabelExit2.configure(foreground="#ffffff")
        self.LabelExit2.configure(text='''If you don't save, all data will be lost''')

    def Open(self):
        self.openFileName = askopenfilename(filetypes=(("*", "*.txt"), ("All files", "*.*")))
        self.Entry1.delete("1.0", END)
        archive = open(self.openFileName)
        for line in archive:
            self.Entry1.insert(INSERT, line)
        archive.close()

    def SaveButton(self):
        try:
            self.saveplace = asksaveasfile(mode='w', defaultextension=".txt")
            text = (self.Entry1.get('1.0', 'end-1c') + "\n")
            self.saveplace.write(text)
            self.condicsave = True
            self.saveplace.destroy()
        except:
            pass
        finally:
            try:
                self.saveplace.close()
            except AttributeError:
                pass

    def Clear(self):
        self.Entry1.delete('1.0', 'end-1c')

    def Exit(self):
        if not self.condicsave:
            self.ExitPage()
        else:
            self.top.destroy()

    def Exit1(self):
        return sys.exit()

    def Exit2(self):
        return self.exitpage.destroy()

    def Exit3(self):
        self.SaveButton()
        self.exitpage.destroy()


class AutoScroll(object):
    def __init__(self, master):
        global vsb
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped


def _create_container(func):
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


PyTextEditor()
