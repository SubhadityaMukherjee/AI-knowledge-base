import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import sys

tag = "uncertainty"

class GUI:
    def __init__(self):
        self.file_paths = []
        window = Gtk.Window()
        window.connect('destroy', Gtk.main_quit)

        textview = Gtk.TextView()
        #                      (drag behaviour, targets (leave empty), action)
        textview.drag_dest_set(Gtk.DestDefaults.DROP, [], Gdk.DragAction.COPY)
        # add the ability to receive URIs (e.g. file paths)
        textview.drag_dest_add_uri_targets()
        textview.connect("drag-data-received", self.on_drag_data_received)

        window.add(textview)
        window.show_all()

    def on_drag_data_received(self, widget, drag_context, x,y, data,info, time):
        #print(data.get_uris())
        self.file_paths.extend(data.get_uris())
        #              (context, success, delete_from_source, time)
        Gtk.drag_finish(drag_context, True, False, time)

        # always call Gtk.drag_finish to receive as suggested by documentation

def format_file_paths(file_paths):
    return [i[7::].replace("%20", " ") for i in file_paths]

def add_tag(files, tag):
    for fname in files:
        print(fname)
        temp = []
        with open(fname, "r") as originalfile:
            temp = [x.strip() for x in originalfile.readlines()]
            if "tags" not in temp[2]:
                temp.insert(2,f"tags: {tag}")
            if tag not in str(temp[2]):
                temp[2] = temp[2] + f" {tag}"
        with open(fname, "w") as newfile:
            newfile.write("\n".join(temp))


def main():
    filenames = GUI()
    Gtk.main()
    filenames = format_file_paths(filenames.file_paths)
    print(f"Running on {len(filenames)} files")
    add_tag(filenames, tag)

if __name__ == "__main__":
    sys.exit(main())
