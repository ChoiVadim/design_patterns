"""
Factory Pattern - UI Components Example
Real-world usage: GUI frameworks, game engines, database connections, DI frameworks
"""

from abc import ABC, abstractmethod
from enum import Enum


class OS(Enum):
    """Operating system types"""
    WINDOWS = "windows"
    MACOS = "macos"
    LINUX = "linux"


# Product interfaces
class Button(ABC):
    """Product interface for buttons"""
    
    @abstractmethod
    def render(self) -> str:
        """Render the button"""
        pass
    
    @abstractmethod
    def onClick(self) -> str:
        """Handle button click"""
        pass


class Dialog(ABC):
    """Product interface for dialogs"""
    
    @abstractmethod
    def render(self) -> str:
        """Render the dialog"""
        pass
    
    @abstractmethod
    def show(self) -> str:
        """Show the dialog"""
        pass


class Menu(ABC):
    """Product interface for menus"""
    
    @abstractmethod
    def render(self) -> str:
        """Render the menu"""
        pass


# Concrete products for Windows
class WindowsButton(Button):
    """Windows-style button"""
    
    def render(self) -> str:
        return "🪟 [Windows Button]"
    
    def onClick(self) -> str:
        return "Windows button clicked - using Win32 API"


class WindowsDialog(Dialog):
    """Windows-style dialog"""
    
    def render(self) -> str:
        return "🪟 Windows Dialog Window"
    
    def show(self) -> str:
        return "Showing Windows native dialog (Win32)"


class WindowsMenu(Menu):
    """Windows-style menu"""
    
    def render(self) -> str:
        return "🪟 Windows Menu Bar"


# Concrete products for macOS
class MacOSButton(Button):
    """macOS-style button"""
    
    def render(self) -> str:
        return "🍎 [macOS Button]"
    
    def onClick(self) -> str:
        return "macOS button clicked - using Cocoa framework"


class MacOSDialog(Dialog):
    """macOS-style dialog"""
    
    def render(self) -> str:
        return "🍎 macOS Dialog Window"
    
    def show(self) -> str:
        return "Showing macOS native dialog (Cocoa/AppKit)"


class MacOSMenu(Menu):
    """macOS-style menu"""
    
    def render(self) -> str:
        return "🍎 macOS Menu Bar"


# Concrete products for Linux
class LinuxButton(Button):
    """Linux-style button"""
    
    def render(self) -> str:
        return "🐧 [Linux Button]"
    
    def onClick(self) -> str:
        return "Linux button clicked - using GTK/Qt"


class LinuxDialog(Dialog):
    """Linux-style dialog"""
    
    def render(self) -> str:
        return "🐧 Linux Dialog Window"
    
    def show(self) -> str:
        return "Showing Linux native dialog (GTK/Qt)"


class LinuxMenu(Menu):
    """Linux-style menu"""
    
    def render(self) -> str:
        return "🐧 Linux Menu Bar"


# Factory interface
class UIFactory(ABC):
    """Abstract factory for UI components"""
    
    @abstractmethod
    def create_button(self) -> Button:
        """Create a button"""
        pass
    
    @abstractmethod
    def create_dialog(self) -> Dialog:
        """Create a dialog"""
        pass
    
    @abstractmethod
    def create_menu(self) -> Menu:
        """Create a menu"""
        pass


# Concrete factories
class WindowsFactory(UIFactory):
    """Factory for Windows UI components"""
    
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_dialog(self) -> Dialog:
        return WindowsDialog()
    
    def create_menu(self) -> Menu:
        return WindowsMenu()


class MacOSFactory(UIFactory):
    """Factory for macOS UI components"""
    
    def create_button(self) -> Button:
        return MacOSButton()
    
    def create_dialog(self) -> Dialog:
        return MacOSDialog()
    
    def create_menu(self) -> Menu:
        return MacOSMenu()


class LinuxFactory(UIFactory):
    """Factory for Linux UI components"""
    
    def create_button(self) -> Button:
        return LinuxButton()
    
    def create_dialog(self) -> Dialog:
        return LinuxDialog()
    
    def create_menu(self) -> Menu:
        return LinuxMenu()


# Factory creator
def get_ui_factory(os_type: OS) -> UIFactory:
    """Factory method to get appropriate UI factory"""
    factories = {
        OS.WINDOWS: WindowsFactory,
        OS.MACOS: MacOSFactory,
        OS.LINUX: LinuxFactory
    }
    factory_class = factories.get(os_type)
    if factory_class:
        return factory_class()
    raise ValueError(f"Unsupported OS: {os_type}")


# Application class
class Application:
    """Application that uses UI factory"""
    
    def __init__(self, os_type: OS):
        self._factory = get_ui_factory(os_type)
        self._button = None
        self._dialog = None
        self._menu = None
    
    def create_ui(self):
        """Create UI components"""
        self._button = self._factory.create_button()
        self._dialog = self._factory.create_dialog()
        self._menu = self._factory.create_menu()
    
    def render_ui(self):
        """Render all UI components"""
        print(f"  {self._menu.render()}")
        print(f"  {self._button.render()}")
        print(f"  {self._dialog.render()}")
    
    def interact(self):
        """Simulate user interaction"""
        print(f"  {self._button.onClick()}")
        print(f"  {self._dialog.show()}")


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Factory Pattern - UI Components Example")
    print("=" * 60)
    print()
    
    # Create application for Windows
    print("1. Windows Application:")
    print("-" * 60)
    windows_app = Application(OS.WINDOWS)
    windows_app.create_ui()
    windows_app.render_ui()
    windows_app.interact()
    print()
    
    # Create application for macOS
    print("2. macOS Application:")
    print("-" * 60)
    macos_app = Application(OS.MACOS)
    macos_app.create_ui()
    macos_app.render_ui()
    macos_app.interact()
    print()
    
    # Create application for Linux
    print("3. Linux Application:")
    print("-" * 60)
    linux_app = Application(OS.LINUX)
    linux_app.create_ui()
    linux_app.render_ui()
    linux_app.interact()
    print()
    
    print("=" * 60)
    print("Key Benefit: Application doesn't need to know which")
    print("concrete UI classes to create - factory handles it!")
    print("=" * 60)

