import tkinter as tk

def celcius_to_fahrenheit(temp_celcius: float) -> float:
    return temp_celcius * 9/5 + 32

class MyTempApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # A couple of stringvars to store our data

        self.celcius_var = tk.StringVar()
        self.fahrenheit_var = tk.StringVar()

        self.celcius_var.set('0')

        # Describe our main structural elements

        self.top_frame = TopFrame(self)
        self.bottom_left_frame = BottomLeftFrame(self, self.celcius_var)
        self.bottom_right_frame = BottomRightFrame(self, self.fahrenheit_var)
        self.command_frame = CommandFrame(self, self.do_conversion)

        # Layout in grid

        self.top_frame.grid(row=0, column=0, columnspan=2, sticky='nesw')
        self.bottom_left_frame.grid(row=1, column=0, sticky='nesw')
        self.bottom_right_frame.grid(row=1, column=1, sticky='')
        self.command_frame.grid()

        # Describe grid

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def do_conversion(self):
        celcius = float(self.celcius_var.get())
        fahrenheit = celcius_to_fahrenheit(celcius)
        self.fahrenheit_var.set(
            str(
                fahrenheit
            )
        )

class TopFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='blue')

        # A title label

        self.title_label = tk.Label(self, text='Temperature App')

        # Place it

        self.title_label.grid(row=0, column=0, pady=10)

        # Describe layout

        self.columnconfigure(0, weight=1)
class BottomLeftFrame(tk.Frame):
    def __init__(self, master, celcius_strvar: tk.StringVar):
        super().__init__(master, bg='red')

        # Elements

        self.celcius_label = tk.Label(self, text='Celcius')
        self.celcius_entry = tk.Entry(self, textvariable=celcius_strvar)

        # Layout

        self.celcius_label.grid(row=0, pady=10, sticky='s')
        self.celcius_entry.grid(row=1, pady=10, sticky='n')

        # Describe

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

class BottomRightFrame(tk.Frame):
    def __init__(self, master, fahrenheit_stringvar: tk.StringVar):
        super().__init__(master, bg='green')

        # Elements

        self.fahrenheit_label = tk.Label(self, text='Fahrenheit')
        self.fahrenheit_entry = tk.Entry(self, textvariable=fahrenheit_stringvar)

        # Layout

        self.fahrenheit_label.grid(row=0, pady=10)
        self.fahrenheit_entry.grid(row=1, pady=10)

        # Describe

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
class CommandFrame(tk.Frame):
    def __init__(self, master, command_to_run):
        super().__init__(master)
        self.command = command_to_run
        self.conv_button = tk.Button(self, text="Convert", command=self.command)

        self.conv_button.grid()


root = tk.Tk()

temp_app = MyTempApp(root)
temp_app.grid(sticky='nesw')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
