"""
State Pattern - Music Player Example
Real-world usage: TCP Connection states (Established, Closed, Listening), Order processing (New, Paid, Shipped), Game character states
"""

from abc import ABC, abstractmethod


class State(ABC):
    """State interface"""

    @abstractmethod
    def click_play(self, player):
        pass

    @abstractmethod
    def click_lock(self, player):
        pass

    @abstractmethod
    def click_next(self, player):
        pass

    @abstractmethod
    def click_previous(self, player):
        pass


class MusicPlayer:
    """Context - The Music Player"""

    def __init__(self):
        self._state = StoppedState()
        self._playing = False
        self._playlist = ["Track 1", "Track 2", "Track 3"]
        self._current_track = 0

    def change_state(self, state: State):
        self._state = state

    def click_play(self):
        self._state.click_play(self)

    def click_lock(self):
        self._state.click_lock(self)

    def click_next(self):
        self._state.click_next(self)

    def click_previous(self):
        self._state.click_previous(self)

    def start_playback(self):
        self._playing = True
        print(f"Playing: {self._playlist[self._current_track]}")

    def stop_playback(self):
        self._playing = False
        print("Playback stopped.")

    def next_track(self):
        self._current_track = (self._current_track + 1) % len(self._playlist)
        print(f"Next track: {self._playlist[self._current_track]}")

    def previous_track(self):
        self._current_track = (self._current_track - 1) % len(self._playlist)
        print(f"Previous track: {self._playlist[self._current_track]}")


class LockedState(State):
    """Concrete State - Locked"""

    def click_play(self, player):
        print("Locked... Do nothing.")

    def click_lock(self, player):
        if player._playing:
            player.change_state(PlayingState())
            print("Unlocked -> Playing")
        else:
            player.change_state(StoppedState())
            print("Unlocked -> Stopped")

    def click_next(self, player):
        print("Locked... Do nothing.")

    def click_previous(self, player):
        print("Locked... Do nothing.")


class PlayingState(State):
    """Concrete State - Playing"""

    def click_play(self, player):
        player.stop_playback()
        player.change_state(StoppedState())
        print("Paused.")

    def click_lock(self, player):
        player.change_state(LockedState())
        print("Locked (while playing)")

    def click_next(self, player):
        player.next_track()

    def click_previous(self, player):
        player.previous_track()


class StoppedState(State):
    """Concrete State - Stopped"""

    def click_play(self, player):
        player.start_playback()
        player.change_state(PlayingState())

    def click_lock(self, player):
        player.change_state(LockedState())
        print("Locked (while stopped)")

    def click_next(self, player):
        print("Locked... Do nothing.")

    def click_previous(self, player):
        print("Locked... Do nothing.")


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("State Pattern - Music Player Example")
    print("=" * 60)
    print()

    player = MusicPlayer()

    # Initial state is Stopped
    print("1. Click Play (Stopped -> Playing)")
    player.click_play()
    print()

    print("2. Click Next (Playing -> Next Track)")
    player.click_next()
    print()

    print("3. Click Lock (Playing -> Locked)")
    player.click_lock()
    print()

    print("4. Click Play (Locked -> Do nothing)")
    player.click_play()
    print()

    print("5. Click Lock (Locked -> Playing)")
    player.click_lock()
    print()

    print("6. Click Play (Playing -> Stopped)")
    player.click_play()
    print()

    print("=" * 60)
    print("Key Benefit: Object behavior changes based on its internal state,")
    print("avoiding massive if-else statements!")
    print("=" * 60)
