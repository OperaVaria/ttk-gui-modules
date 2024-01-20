"""
menu_class.py

Tkinter.ttk (main) menu as a class.

By OperaVaria, 2024.
"""

# Built-in module imports:
from tkinter import ttk


class Menu(ttk.Frame):
    """Ttk GUI (main) menu as a Python class.
       General purpose, multi-platform, optimized for 1080p resolution."""
    def __init__(self, window, parent, font):
        """Menu widget structure to be placed into a parent container (frame).
           6 Buttons in 2 rows + Exit button."""
        super().__init__(parent)

        # Grid weight setup (6 rows, 3 columns)
        parent.grid_rowconfigure(0, weight=2)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=1)
        parent.grid_rowconfigure(3, weight=1)
        parent.grid_rowconfigure(4, weight=1)
        parent.grid_rowconfigure(5, weight=2)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

        # Titles
        self.lbl_title = ttk.Label(parent, text="Title",
                                   font=(font, 48), justify="center")
        self.lbl_title.grid(row=0, column=0, columnspan=3)

        self.lbl_subtitle = ttk.Label(parent, text="Subtitle\n",
                                      font=(font, 24))
        self.lbl_subtitle.grid(row=1, column=0, columnspan=3)

        # Buttons
        self.btn_1 = ttk.Button(parent, text="Button 1",
                                command=self.placeholder_button_method)
        self.btn_1.grid(row=2, column=0, columnspan=1)

        self.btn_2 = ttk.Button(parent, text="Button 2",
                                command=self.placeholder_button_method)
        self.btn_2.grid(row=2, column=1, columnspan=1)

        self.btn_3 = ttk.Button(parent, text="Button 3",
                                command=self.placeholder_button_method)
        self.btn_3.grid(row=2, column=2, columnspan=1)

        self.btn_4 = ttk.Button(parent, text="Button 4",
                                command=self.placeholder_button_method)
        self.btn_4.grid(row=3, column=0, columnspan=1)

        self.btn_5 = ttk.Button(parent, text="Button 5",
                                command=self.placeholder_button_method)
        self.btn_5.grid(row=3, column=1, columnspan=1)

        self.btn_6 = ttk.Button(parent, text="Button 6",
                                command=self.placeholder_button_method)
        self.btn_6.grid(row=3, column=2, columnspan=1)

        self.btn_exit = ttk.Button(parent, text="Exit", command=window.destroy)
        self.btn_exit.grid(row=4, column=0, columnspan=3)

        # Version number widget
        self.lbl_version = ttk.Label(parent, text="App version", font=(font, 18))
        self.lbl_version.grid(row=5, column=0, columnspan=3)

    def placeholder_button_method(self):
        """A placeholder method for button commands."""
    pass


# Display message when accidentally run:
if __name__ == "__main__":
    print("This file is an importable module and cannot be run.")
