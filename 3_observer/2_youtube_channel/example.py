"""
Observer Pattern - YouTube Channel Example
Real-world usage: Event handling systems, MVC architecture (Model notifying View), Pub-Sub systems
"""

from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """Observer interface"""

    @abstractmethod
    def update(self, channel_name: str, video_title: str):
        """Receive update from subject"""
        pass


class Subject(ABC):
    """Subject interface"""

    @abstractmethod
    def attach(self, observer: Observer):
        """Attach an observer"""
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        """Detach an observer"""
        pass

    @abstractmethod
    def notify(self, video_title: str):
        """Notify all observers"""
        pass


class YoutubeChannel(Subject):
    """Concrete Subject - The YouTube Channel"""

    def __init__(self, name: str):
        self._name = name
        self._subscribers: List[Observer] = []
        self._videos: List[str] = []

    def attach(self, observer: Observer):
        print(f"Channel '{self._name}': Attached a new subscriber.")
        self._subscribers.append(observer)

    def detach(self, observer: Observer):
        print(f"Channel '{self._name}': Detached a subscriber.")
        self._subscribers.remove(observer)

    def notify(self, video_title: str):
        print(f"Channel '{self._name}': Notifying {len(self._subscribers)} subscribers...")
        for subscriber in self._subscribers:
            subscriber.update(self._name, video_title)

    def upload_video(self, title: str):
        print(f"\nChannel '{self._name}' is uploading video: '{title}'")
        self._videos.append(title)
        self.notify(title)


class Subscriber(Observer):
    """Concrete Observer - The Subscriber"""

    def __init__(self, name: str):
        self._name = name

    def update(self, channel_name: str, video_title: str):
        print(f"  [Notification] Hey {self._name}, {channel_name} just uploaded '{video_title}'!")


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Observer Pattern - YouTube Channel Example")
    print("=" * 60)
    print()

    # Create a channel
    channel = YoutubeChannel("TechDaily")

    # Create subscribers
    alice = Subscriber("Alice")
    bob = Subscriber("Bob")
    charlie = Subscriber("Charlie")

    # Users subscribe
    channel.attach(alice)
    channel.attach(bob)

    # Upload a video
    channel.upload_video("Observer Pattern Explained")

    # Charlie subscribes, Bob unsubscribes
    print()
    channel.attach(charlie)
    channel.detach(bob)

    # Upload another video
    channel.upload_video("Python Design Patterns Tutorial")

    print()
    print("=" * 60)
    print("Key Benefit: The channel doesn't need to know WHO subscribers are,")
    print("just that they implement the Observer interface!")
    print("=" * 60)
