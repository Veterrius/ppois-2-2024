from abc import ABC

from src.main.view.abstract.window import Window


class Subwindow(Window, ABC):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.lift()