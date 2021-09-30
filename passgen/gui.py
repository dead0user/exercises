import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import fgen


class MainWindow(Gtk.Window):

    def __init__(self) -> None:
        Gtk.Window.__init__(self, title="Gtk password generator")
        self.layout()

    def layout(self):
        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(5)
        self.grid.set_row_spacing(5)
        self.add(self.grid)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_hexpand(False)
        self.scrolled_window.set_vexpand(True)
        self.scrolled_window.set_min_content_width(250)
        self.scrolled_window.set_max_content_width(250)
        self.display = Gtk.TextView(editable=False)
        self.text_buffer = self.display.get_buffer()
        self.scrolled_window.add(self.display)
                
        self.exit_button = Gtk.Button(label="Exit")

        self.generate_button = Gtk.Button(label="Generate")

        self.password_length = Gtk.SpinButton()

        self.passwords_quantity = Gtk.SpinButton()

        self.grid.attach(self.display, 0, 0, 1, 5)
        self.grid.attach(self.exit_button, 1, 4, 1, 1)
        self.grid.attach(self.generate_button, 2, 4, 1, 1)
        self.grid.attach(self.password_length, 2, 0, 1, 1)
        self.grid.attach(self.passwords_quantity, 2, 1, 1, 1)
        
