from tkinter import *
from tkinter import filedialog
import os
import sys
from converter import convert_to_html
from gui.animation import Animation
from gui.editor import Editor

class GUI:
    def __init__(self, root, screen_width, screen_height, window_height):
        self.input_file_path = StringVar()
        self.output_file_path = StringVar()
        self.status = StringVar()
        self.root = root
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.window_height = window_height

        self.asset_path = os.path.join(os.path.dirname(__file__), "gui/assets/")

        self.SCALE_RATIO = 48
        self.scale = max(1, self.window_height // self.SCALE_RATIO)

        self.markdown_editor = Editor(self.root, self.screen_width // 2, self.screen_height - self.window_height, 0, 0)
        self.html_editor = Editor(self.root, self.screen_width // 2, screen_height - window_height, self.screen_width // 2, 0)



        self.load_images()


    def start(self):
        self.load_widgets()
        self.layout_widgets()
        self.style_widgets()

    def quit_app(self, event=None):
        sys.exit(0)


    def get_input_file(self, event=None):
        self.input_file_path.set(filedialog.askopenfilename(
                initialdir = os.getcwd(),
                filetypes = [("markdown", "*.md"), ("all file types", "*.*")]))
        if self.input_file_path.get():
            self.btn_open_image = self.load_image("OPEN_USED.png")
            self.btn_open.config(image=self.btn_open_image)

            self.markdown_editor.open()
            try:
                with open(self.input_file_path.get(), "r", encoding="utf-8") as file:
                    self.markdown_editor.open_content_in_editor(file.read())

                self.make_convert_available()

            except Exception:
                self.status.set("failed to load file into editor")

    def save_as_file(self, widget=None):
        if self.html_editor.is_open:
            self.output_file_path.set(filedialog.asksaveasfilename(
                initialdir=os.path.dirname(self.input_file_path.get()),
                defaultextension=".html"))
            if self.output_file_path.get():
                self.btn_save_image = self.load_image("SAVE_USED.png")
                self.btn_save.config(image=self.btn_save_image)
                with open(self.output_file_path.get(), "w", encoding="utf-8") as save_file:
                    html = self.html_editor.get_editor_content()
                    save_file.writelines(html)


    def convert_file(self, event=None):
        if not self.input_file_path.get():
            self.status.set("Please give an input file")
        else:
            try:
                markdown = self.markdown_editor.get_editor_content()

                html = convert_to_html(markdown)

                self.status.set("conversion completed")
                self.btn_convert_image = self.load_image("CONVERT_SUCCES.png")
                self.btn_convert.config(image=self.btn_convert_image)
                self.html_editor.open()
                self.html_editor.open_content_in_editor(html)
                self.make_save_available()
            except Exception as error:
                self.status.set("conversion failed :(")
                print(error)

    def load_widgets(self):
        self.canvas = Canvas(self.root, highlightthickness=0)

        self.border_placeholder = self.canvas.create_rectangle(
            0, 0,
            self.screen_width, self.window_height,
            outline="white", width=10
        )

        # Text Displays
        self.lbl_input = Label(self.canvas, textvariable=self.input_file_path, bg="#000000", fg="#FFFFFF", font=("Courier", 12))
        self.lbl_output = Label(self.canvas, textvariable=self.output_file_path, bg="#000000", fg="#FFFFFF", font=("Courier", 12))
        self.lbl_status = Label(self.canvas, textvariable=self.status, bg="#000000", fg="#FFFFFF", font=("Courier", 10))

        self.btn_open = Label(self.canvas, image=self.btn_open_image, bg="#000000", cursor="hand2")
        self.btn_save = Label(self.canvas, image=self.btn_save_image, bg="#000000", cursor="hand2")
        self.btn_convert = Label(self.canvas, image=self.btn_convert_image, bg="#000000", cursor="hand2")
        self.btn_quit = Label(self.canvas, image=self.btn_quit_image, bg="#000000", cursor="hand2")

        # Bind click events
        self.btn_open.bind("<Button-1>", self.get_input_file)
        self.btn_save.bind("<Button-1>", self.save_as_file)
        self.btn_convert.bind("<Button-1>", self.convert_file)
        self.btn_quit.bind("<Button-1>", self.quit_app)

        # Bind hover events

        self.bind_hover_animation(self.btn_open, self.btn_open_animation, lambda: self.btn_open_image)
        self.bind_hover_animation(self.btn_quit, self.btn_quit_hover_animation, lambda: self.btn_quit_image)

    def layout_widgets(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.canvas.grid(sticky="nsew")

        # Placing widgets using coordinates calculated dynamically from screen size.
        # This ensures they scale gracefully whether on a laptop or an ultra-wide monitor or at least i hope it does.

        col_1_width = self.get_dynamic_width(5)
        col_2_width = self.get_dynamic_width(28)
        col_3_width = self.get_dynamic_width(60)
        row_1_height = self.get_dynamic_height(10)
        row_btn_height = self.get_dynamic_height(65)
        row_3_height = self.get_dynamic_height(65)

        self.btn_open.place(x=col_1_width, y=row_btn_height)
        self.lbl_input.place(x=col_2_width, y=row_1_height)

        self.btn_convert.place(x=col_2_width, y=row_btn_height)
        self.lbl_output.place(x=col_2_width, y=self.get_dynamic_height(40))

        self.btn_save.place(x=col_3_width, y=row_btn_height)
        self.lbl_status.place(x=col_2_width, y=row_3_height)

        self.btn_quit.place(x=self.get_dynamic_width(80), y=row_3_height)

    def load_image(self, filename):
        file_path = os.path.join(self.asset_path, filename)
        return PhotoImage(file=file_path).zoom(self.scale)

    def load_images(self):
        self.btn_open_image = self.load_image("OPEN_IDLE.png")
        self.btn_open_animation = Animation([self.load_image(f"OPEN_HOVER_FRAME_{frame}.png") for frame in range(1,5)], time_per_frame=150)
        self.btn_save_hover_animation = Animation([self.load_image(f"SAVE_HOVER_FRAME_{frame}.png") for frame in range(1,9)])
        self.btn_save_image = self.load_image("SAVE_NOT_AVAILABLE.png")
        self.btn_convert_image = self.load_image("CONVERT_NOT_AVAILABLE.png")
        self.btn_convert_hover_animation = Animation([self.load_image(f"CONVERT_HOVER_FRAME_{frame}.png") for frame in range(1,17)])
        self.btn_quit_image = self.load_image("QUIT_IDLE.png")
        self.btn_quit_hover_animation = Animation([self.load_image(f"QUIT_HOVER_FRAME_{frame}.png") for frame in range(1,5)])



    def get_dynamic_height(self, percentage: int):
        return round(self.window_height / 100 * percentage)

    def get_dynamic_width(self, percentage: int):
        return round(self.screen_width / 100 * percentage)

    def style_widgets(self):
        self.canvas.configure(background="#000000")

    def bind_hover_animation(self, button: Label, animation: Animation, idle_image):
        button.bind("<Enter>", lambda e: animation.start_hover(button, self.root))
        button.bind("<Leave>", lambda e: animation.stop_hover(button, idle_image()))

    def make_convert_available(self):
        self.btn_convert_image = self.load_image("CONVERT_IDLE.png")
        self.btn_convert.config(image=self.btn_convert_image)
        self.bind_hover_animation(self.btn_convert, self.btn_convert_hover_animation, lambda: self.btn_convert_image)

    def make_save_available(self):
        self.btn_save_image = self.load_image("SAVE_IDLE.png")
        self.btn_save.config(image=self.btn_save_image)
        self.bind_hover_animation(self.btn_save, self.btn_save_hover_animation, lambda: self.btn_save_image)

if __name__ == "__main__":
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_height = screen_height // 3

    root.geometry(f"{screen_width}x{window_height}+0+{screen_height - window_height}")
    root.wm_resizable(width=False, height=False)
    root.overrideredirect(True)
    root.wm_attributes(topmost=True)
    root.iconbitmap(os.path.join(os.path.dirname(__file__), "gui/assets/HTMD_LOGO1.ico"))
    gui = GUI(root, screen_width, screen_height , window_height)
    gui.start()

    root.mainloop()