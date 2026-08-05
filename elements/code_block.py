from element import Element


class CodeBlock(Element):
    regex = r"^```"

    def __init__(self, content, language):
        self.content = content
        self.language = language

    @staticmethod
    def parse(context):
        content = ""
        line = context.get_current_line()
        language = line[3:].strip()
        while context.has_next_line() and context.identify_next_line() != CodeBlock:
            content += context.get_next_line()
            context.current_index += 1

        context.current_index += 2
        return CodeBlock(content, language)

    def render_html(self):
        if self.language:
            return f"<pre><code class='language-{self.language}'>{self.content}</code></pre>"
        return f"<pre><code>{self.content}</code></pre>"
