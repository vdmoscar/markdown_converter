from tkinter import *


class Editor:
    def __init__(self, root, width, height, pos_x, pos_y):
        self.root = root
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.is_open = False

    def open(self):
        self.editor_window = Toplevel(self.root)

        self.editor_window.geometry(f"{self.width}x{self.height}+{self.pos_x}+{self.pos_y}")
        self.editor_window.overrideredirect(True)
        self.editor_window.wm_attributes(topmost=True)

        canvas = Canvas(self.editor_window, bg="#000000", highlightthickness=0)
        canvas.pack(fill=BOTH, expand=True)

        self.editor_text = Text(
                    canvas,
                    bg="#000000", fg="#FFFFFF",
                    insertbackground="#FFFFFF",
                    font=("Courier", 11),
                    highlightthickness=0
                )

        self.editor_text.place(x=0, y=0, width=self.width, height=self.height)
        self.is_open = True

    def open_file_in_editor(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            self.editor_text.delete("1.0", END)
            self.editor_text.insert("1.0", content)

    def get_editor_content(self):
        return self.editor_text.get("1.0", END).splitlines(True)
