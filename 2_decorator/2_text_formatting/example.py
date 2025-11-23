"""
Decorator Pattern - Text Formatting Example
Real-world usage: Rich text editors, markdown processors, HTML rendering
"""

from abc import ABC, abstractmethod


class TextComponent(ABC):
    """Component interface for text"""
    
    @abstractmethod
    def render(self) -> str:
        """Return formatted text"""
        pass


class PlainText(TextComponent):
    """Concrete component - plain text"""
    
    def __init__(self, text: str):
        self._text = text
    
    def render(self) -> str:
        return self._text


class TextDecorator(TextComponent):
    """Base decorator class"""
    
    def __init__(self, component: TextComponent):
        self._component = component
    
    @abstractmethod
    def render(self) -> str:
        pass


class BoldDecorator(TextDecorator):
    """Decorator for bold text"""
    
    def render(self) -> str:
        return f"**{self._component.render()}**"


class ItalicDecorator(TextDecorator):
    """Decorator for italic text"""
    
    def render(self) -> str:
        return f"*{self._component.render()}*"


class UnderlineDecorator(TextDecorator):
    """Decorator for underlined text"""
    
    def render(self) -> str:
        return f"__{self._component.render()}__"


class StrikethroughDecorator(TextDecorator):
    """Decorator for strikethrough text"""
    
    def render(self) -> str:
        return f"~~{self._component.render()}~~"


class CodeDecorator(TextDecorator):
    """Decorator for code text"""
    
    def render(self) -> str:
        return f"`{self._component.render()}`"


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Decorator Pattern - Text Formatting Example")
    print("=" * 60)
    print()
    
    # Plain text
    print("1. Plain Text:")
    print("-" * 60)
    text1 = PlainText("Hello, World!")
    print(f"Output: {text1.render()}")
    print()
    
    # Bold text
    print("2. Bold Text:")
    print("-" * 60)
    text2 = BoldDecorator(PlainText("Hello, World!"))
    print(f"Output: {text2.render()}")
    print()
    
    # Bold and italic
    print("3. Bold and Italic:")
    print("-" * 60)
    text3 = ItalicDecorator(BoldDecorator(PlainText("Hello, World!")))
    print(f"Output: {text3.render()}")
    print()
    
    # Bold, italic, and underline
    print("4. Bold, Italic, and Underline:")
    print("-" * 60)
    text4 = UnderlineDecorator(
        ItalicDecorator(
            BoldDecorator(PlainText("Hello, World!"))
        )
    )
    print(f"Output: {text4.render()}")
    print()
    
    # Strikethrough
    print("5. Strikethrough:")
    print("-" * 60)
    text5 = StrikethroughDecorator(PlainText("Old Price: $100"))
    print(f"Output: {text5.render()}")
    print()
    
    # Code formatting
    print("6. Code Formatting:")
    print("-" * 60)
    text6 = CodeDecorator(PlainText("print('Hello')"))
    print(f"Output: {text6.render()}")
    print()
    
    # Complex combination
    print("7. Complex Combination (Bold + Italic + Code):")
    print("-" * 60)
    text7 = CodeDecorator(
        ItalicDecorator(
            BoldDecorator(PlainText("function_name"))
        )
    )
    print(f"Output: {text7.render()}")
    print()
    
    print("=" * 60)
    print("Key Benefit: Can stack multiple formatters dynamically")
    print("without creating classes for every combination!")
    print("=" * 60)

