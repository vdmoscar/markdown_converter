from tkinter import *
from tkinter import filedialog
import os
import sys
from converter import convert_to_html
from gui.animation import Animation

class GUI:
    def __init__(self, root, screen_width, window_height):
        self.input_file_path = StringVar()
        self.output_file_path = StringVar()
        self.status = StringVar()
        self.root = root
        self.screen_width = screen_width

        self.window_height = window_height
        self.animation_list = []
        self.asset_path = "gui/assets/"

        # Image placeholders (for your future PNG sprites)
        self.border_image = None
        self.btn_open_image = PhotoImage(file=f"{self.asset_path}OPEN_IDLE.png")
        self.btn_open_animation = Animation([PhotoImage(file=f"{self.asset_path}OPEN_HOVER_FRAME_{frame}.png") for frame in range(1,5)], time_per_frame=150)
        self.btn_save_hover_animation = Animation([PhotoImage(file=f"{self.asset_path}SAVE_HOVER_FRAME_{frame}.png") for frame in range(1,9)])
        self.btn_save_image = PhotoImage(file=f"{self.asset_path}SAVE_IDLE.png")
        self.btn_convert_image = PhotoImage(file=f"{self.asset_path}CONVERT_IDLE.png")
        self.btn_convert_hover_animation = Animation([PhotoImage(file=f"{self.asset_path}CONVERT_HOVER_FRAME_{frame}.png") for frame in range(1,17)])
        self.btn_quit_image = PhotoImage(file=f"{self.asset_path}QUIT_IDLE.png")
        self.btn_quit_hover_animation = Animation([PhotoImage(file=f"{self.asset_path}QUIT_HOVER_FRAME_{frame}.png") for frame in range(1,5)])


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
            self.btn_open_image = PhotoImage(file=f"{self.asset_path}OPEN_USED.png")
            self.btn_open.config(image=self.btn_open_image)

    def get_output_file(self, widget=None):
        self.output_file_path.set(filedialog.asksaveasfilename(
            initialdir=os.path.dirname(self.input_file_path.get()),
            defaultextension=".html"))
        if self.output_file_path.get():
            self.btn_save_image = PhotoImage(file=f"{self.asset_path}SAVE_USED.png")
            self.btn_save.config(image=self.btn_save_image)

    def convert_file(self, event=None):
        if not self.output_file_path.get() or not self.input_file_path.get():
            self.status.set("Please give both an input file and an output file path.")
        else:
            try:
                with open(self.input_file_path.get(), "r") as input_file:
                    with open(self.output_file_path.get(), "w") as output_file:
                        output_file.write(convert_to_html(input_file.readlines()))
                        self.status.set("conversion completed")
                        self.btn_convert_image = PhotoImage(file=f"{self.asset_path}CONVERT_SUCCES.png")
                        self.btn_convert.config(image=self.btn_convert_image)
            except Exception:
                self.status.set("conversion failed :(")

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
        self.btn_save.bind("<Button-1>", self.get_output_file)
        self.btn_convert.bind("<Button-1>", self.convert_file)
        self.btn_quit.bind("<Button-1>", self.quit_app)

        # Bind hover events for the save button

        self.bind_hover_animation(self.btn_open, self.btn_open_animation, lambda: self.btn_open_image)
        self.bind_hover_animation(self.btn_save, self.btn_save_hover_animation, lambda: self.btn_save_image)
        self.bind_hover_animation(self.btn_convert, self.btn_convert_hover_animation, lambda: self.btn_convert_image)
        self.bind_hover_animation(self.btn_quit, self.btn_quit_hover_animation, lambda: self.btn_quit_image)

    def layout_widgets(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.canvas.grid(sticky="nsew")

        # Placing widgets using coordinates calculated dynamically from screen size.
        # This ensures they scale gracefully whether on a laptop or an ultra-wide monitor or at least i hope it does.

        col_1_width = self.get_dynamic_width(2)
        col_2_width = self.get_dynamic_width(20)
        col_3_width = self.get_dynamic_width(40)
        row_1_height = self.get_dynamic_height(10)
        row_btn_height = self.get_dynamic_height(65)
        row_3_height = self.get_dynamic_height(65)

        self.btn_open.place(x=col_1_width, y=row_btn_height)
        self.lbl_input.place(x=col_2_width, y=row_1_height)

        self.btn_save.place(x=col_2_width, y=row_btn_height)
        self.lbl_output.place(x=col_2_width, y=self.get_dynamic_height(40))

        self.btn_convert.place(x=col_3_width, y=row_btn_height)
        self.lbl_status.place(x=col_2_width, y=row_3_height)

        self.btn_quit.place(x=self.get_dynamic_width(70), y=row_3_height)


    def get_dynamic_height(self, percentage: int):
        return round(self.window_height / 100 * percentage)

    def get_dynamic_width(self, percentage: int):
        return round(self.screen_width / 100 * percentage)


    def style_widgets(self):
        self.canvas.configure(background="#000000")

    def bind_hover_animation(self, button: Label, animation: Animation, idle_image):
        button.bind("<Enter>", lambda e: animation.start_hover(button, self.root))
        button.bind("<Leave>", lambda e: animation.stop_hover(button, idle_image()))


if __name__ == "__main__":
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_height = screen_height // 5 * 2

    root.geometry(f"{screen_width}x{window_height}+0+{screen_height - window_height}")
    root.wm_resizable(width=False, height=False)
    root.overrideredirect(True)
    root.wm_attributes(topmost=True)

    gui = GUI(root, screen_width, window_height)
    gui.start()

    root.mainloop()