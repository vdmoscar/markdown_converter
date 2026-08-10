class Animation:
    def __init__(self, frames: list[object], current_frame_count=0, time_per_frame=100):
        self.frames = frames
        self.current_frame_count = current_frame_count
        self.after_id = None
        self.speed = time_per_frame

    def get_current_frame(self):
        return self.frames[self.current_frame_count]

    def progress_one_frame(self):
        self.current_frame_count = (self.current_frame_count + 1) % len(self.frames)
        return self.get_current_frame()

    def start_hover(self, widget, root):
        """Play the animation frames sequentially on hover."""
        widget.config(image=self.progress_one_frame())
        # Schedule the next frame update every 100ms
        self.after_id = root.after(self.speed, lambda: self.start_hover(widget, root))

    def stop_hover(self, widget, idle_image):
        """Stop the loop and revert back to the static idle image."""
        if self.after_id:
            widget.after_cancel(self.after_id)
            self.after_id = None
        self.current_frame_count = 0  # Reset frames for next time
        widget.config(image=idle_image)