import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import argparse
import sys
import fgen
import gui

small_letters = 'abcdefghijklmnopqrstuvwxyz'
large_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_signs = '!@#$%&?'


parser = argparse.ArgumentParser()

parser.add_argument('-f', action='store', default=3,
                    dest='force_of_pass', type=int,
                    help="Force of password(1:low, 2:mid, 3:high)")
parser.add_argument('-q', action='store', default=5,
                    dest='passwords_quantity', type=int,
                    help="Quantity of generated password")
parser.add_argument('-l', action='store', default=12,
                    dest='password_length', type=int,
                    help="Length of generated passwords(5 to 60 chars)")
parser.add_argument('-g', action='store_true',
                    default=False, dest='gui_running',
                    help="GUI. In the Future maybe...")

# parser.parse_args(args=None if sys.argv[1:] else ['--help'])

argument = parser.parse_args()

if argument.gui_running == True:
    win = gui.MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
    pass
else:
    if argument.force_of_pass == 1:
        pass_dictionary = fgen.string_to_list(digits + small_letters)
    elif argument.force_of_pass == 2:
        pass_dictionary = fgen.string_to_list(digits + small_letters + large_letters)
    elif argument.force_of_pass == 3:
        pass_dictionary = fgen.string_to_list(digits + small_letters + large_letters + special_signs)
    else:
        parser.print_help()
        sys.exit(0)

    if argument.password_length < 5 and argument.password_length > 60:
        parser.print_help()
        sys.exit(0)

    for i in range(argument.passwords_quantity):
        fgen.password_generator(argument.password_length, pass_dictionary)
