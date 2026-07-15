from abc import ABC, abstractmethod


class Element(ABC):

    @abstractmethod
    def parse(index: int, file) -> tuple[int, object]:
        pass

    @abstractmethod
    def render_html(self):
        pass
