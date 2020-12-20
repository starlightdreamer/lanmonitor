from abc import ABCMeta, abstractmethod
from tkinter import messagebox


def inform(self, message="", is_warning=False):
    if is_warning:
        messagebox.showwarning("Warning", message)
    else:
        messagebox.showinfo("Information", message)

