"""
Composite Pattern - File System Example
Real-world usage: File systems, GUI hierarchies, organization charts, DOM trees, menus
"""

from abc import ABC, abstractmethod
from typing import List


class FileSystemItem(ABC):
    """Component interface"""
    
    @abstractmethod
    def get_name(self) -> str:
        """Get item name"""
        pass
    
    @abstractmethod
    def get_size(self) -> int:
        """Get item size in bytes"""
        pass
    
    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display item structure"""
        pass


class File(FileSystemItem):
    """Leaf class - represents a file"""
    
    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size
    
    def get_name(self) -> str:
        return self._name
    
    def get_size(self) -> int:
        return self._size
    
    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        return f"{prefix}📄 {self._name} ({self._size} bytes)"


class Folder(FileSystemItem):
    """Composite class - represents a folder"""
    
    def __init__(self, name: str):
        self._name = name
        self._children: List[FileSystemItem] = []
    
    def get_name(self) -> str:
        return self._name
    
    def get_size(self) -> int:
        """Calculate total size of folder and all children"""
        total = 0
        for child in self._children:
            total += child.get_size()
        return total
    
    def add(self, item: FileSystemItem):
        """Add a child item"""
        self._children.append(item)
    
    def remove(self, item: FileSystemItem):
        """Remove a child item"""
        if item in self._children:
            self._children.remove(item)
    
    def get_children(self) -> List[FileSystemItem]:
        """Get all children"""
        return self._children
    
    def display(self, indent: int = 0) -> str:
        """Display folder structure recursively"""
        prefix = "  " * indent
        result = [f"{prefix}📁 {self._name}/ ({self.get_size()} bytes total)"]
        for child in self._children:
            result.append(child.display(indent + 1))
        return "\n".join(result)


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Composite Pattern - File System Example")
    print("=" * 60)
    print()
    
    # Create file system structure
    root = Folder("root")
    
    # Create documents folder
    documents = Folder("Documents")
    documents.add(File("resume.pdf", 245760))
    documents.add(File("cover_letter.docx", 15360))
    
    # Create projects folder
    projects = Folder("Projects")
    project1 = Folder("WebApp")
    project1.add(File("index.html", 2048))
    project1.add(File("style.css", 4096))
    project1.add(File("script.js", 8192))
    
    project2 = Folder("MobileApp")
    project2.add(File("MainActivity.java", 12288))
    project2.add(File("layout.xml", 3072))
    
    projects.add(project1)
    projects.add(project2)
    
    # Create images folder
    images = Folder("Images")
    images.add(File("photo1.jpg", 1048576))
    images.add(File("photo2.png", 2097152))
    
    # Add folders to root
    root.add(documents)
    root.add(projects)
    root.add(images)
    root.add(File("readme.txt", 512))
    
    # Display file system
    print("File System Structure:")
    print("-" * 60)
    print(root.display())
    print()
    
    # Calculate sizes
    print("Size Analysis:")
    print("-" * 60)
    print(f"Root folder size: {root.get_size()} bytes ({root.get_size() / 1024:.2f} KB)")
    print(f"Documents folder size: {documents.get_size()} bytes")
    print(f"Projects folder size: {projects.get_size()} bytes")
    print(f"WebApp folder size: {project1.get_size()} bytes")
    print(f"MobileApp folder size: {project2.get_size()} bytes")
    print(f"Images folder size: {images.get_size()} bytes")
    print()
    
    # Demonstrate uniform interface
    print("Uniform Interface Demo:")
    print("-" * 60)
    items = [root, documents, File("test.txt", 1024)]
    for item in items:
        print(f"{item.get_name()}: {item.get_size()} bytes")
    print()
    
    print("=" * 60)
    print("Key Benefit: Can treat files and folders uniformly!")
    print("Operations work the same way on both individual files and folders!")
    print("=" * 60)

