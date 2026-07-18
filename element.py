from abc import ABC, abstractmethod


class Element(ABC):
    
    @abstractmethod
    def parse(context: object) -> tuple[int, object]:
        pass

    @abstractmethod
    def render_html(self):
        pass
