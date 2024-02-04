import tkinter as tk

from frames.City_Tax_Frame import City_Tax_Frame
from frames.Data_Select_Frame import Data_Select_Frame
from frames.Information_Frame import Information_Frame
from frames.Yearly_Income_Frame import Yearly_Income_Frame
from frames.File_Explorer_Frame import File_Explorer_Frame

file_data = {}


class Income_And_Local_Tax_Tool(tk.Tk):
    def __init__(self):
        # inharit Tk Class methods and variables
        super().__init__()
        self.geometry("800x800")
        self.minsize(width=800, height=800)

        self.title("Year Income Info")

        self.rowconfigure(0, weight=0, minsize=35)
        self.rowconfigure(1, weight=1, minsize=35)
        self.rowconfigure(2, weight=5, minsize=35)
        self.rowconfigure(3, weight=10, minsize=35)

        self.columnconfigure(0, weight=1, minsize=200)
        self.columnconfigure(1, weight=1, minsize=200)
        self.columnconfigure(2, weight=1, minsize=200)
        self.columnconfigure(3, weight=1, minsize=200)

        self.tool_data = {
            "file_data": None,
            "info_frm_ref": None,
            "city_tax_frm_ref": None,
            "yearly_income_frm_ref": None,
        }

        self.blockA = GUI_Block_A(self.tool_data, master=self)
        self.blockA.grid(row=0, column=0, columnspan=4, sticky="NSEW")

        self.blockB = GUI_Block_B(self.tool_data, master=self)
        self.blockB.grid(row=1, rowspan=2, column=0, columnspan=2, sticky="NSEW")

        self.blockC = GUI_Block_C(self.tool_data, master=self)
        self.blockC.grid(row=1, rowspan=2, column=2, columnspan=2, sticky="NSEW")


class GUI_Block_A(tk.Frame):
    def __init__(self, tool_data, **kwargs):
        super().__init__(**kwargs, bg="lightblue", height=50)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.file_explorer = File_Explorer_Frame(tool_data=tool_data, master=self)
        self.file_explorer.grid(row=0, column=0, sticky="NSEW")


class GUI_Block_B(tk.Frame):
    def __init__(self, tool_data, **kwargs):
        super().__init__(**kwargs, bg="green")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=25)
        self.columnconfigure(0, weight=1)

        self.data_select = Data_Select_Frame(tool_data=tool_data, master=self)
        self.data_select.grid(row=0, column=0, sticky="NSEW")

        self.info_pane = Information_Frame(master=self)
        self.info_pane.grid(row=1, column=0, sticky="NSEW")

        tool_data["info_frm_ref"] = self.info_pane


class GUI_Block_C(tk.Frame):
    def __init__(self, tool_data, **kwargs):
        super().__init__(**kwargs, bg="red")

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.city_tax_select = City_Tax_Frame(tool_data=tool_data, master=self)
        self.city_tax_select.grid(row=0, column=0, sticky="NSEW")

        self.yearly_income = Yearly_Income_Frame(tool_data=tool_data, master=self)
        self.yearly_income.grid(row=1, column=0, sticky="NSEW")

        tool_data["city_tax_frm_ref"] = self.city_tax_select
        tool_data["yearly_income_frm_ref"] = self.yearly_income
