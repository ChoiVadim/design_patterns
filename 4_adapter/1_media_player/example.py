"""
Adapter Pattern - Media Player Example
Real-world usage: API integrations, legacy systems, third-party libraries, payment gateways
"""

from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    """Target interface that client expects"""
    
    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        """Play media file"""
        pass


# Adaptee classes (existing incompatible interfaces)
class Mp3Player:
    """Existing MP3 player - doesn't implement MediaPlayer"""
    
    def play_mp3(self, file_name: str):
        print(f"🎵 Playing MP3 file: {file_name}")
        return f"MP3: {file_name}"


class Mp4Player:
    """Existing MP4 player - different interface"""
    
    def play_mp4(self, file_name: str):
        print(f"🎬 Playing MP4 file: {file_name}")
        return f"MP4: {file_name}"


class VlcPlayer:
    """Existing VLC player - different interface"""
    
    def play_vlc(self, file_name: str):
        print(f"🎥 Playing VLC file: {file_name}")
        return f"VLC: {file_name}"


# Adapter classes
class Mp3Adapter(MediaPlayer):
    """Adapter for MP3 player"""
    
    def __init__(self):
        self._mp3_player = Mp3Player()
    
    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "mp3":
            return self._mp3_player.play_mp3(file_name)
        else:
            raise ValueError(f"MP3 adapter cannot play {audio_type} files")


class Mp4Adapter(MediaPlayer):
    """Adapter for MP4 player"""
    
    def __init__(self):
        self._mp4_player = Mp4Player()
    
    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "mp4":
            return self._mp4_player.play_mp4(file_name)
        else:
            raise ValueError(f"MP4 adapter cannot play {audio_type} files")


class VlcAdapter(MediaPlayer):
    """Adapter for VLC player"""
    
    def __init__(self):
        self._vlc_player = VlcPlayer()
    
    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "vlc":
            return self._vlc_player.play_vlc(file_name)
        else:
            raise ValueError(f"VLC adapter cannot play {audio_type} files")


class AudioPlayer(MediaPlayer):
    """Main audio player that uses adapters"""
    
    def __init__(self):
        self._mp3_adapter = Mp3Adapter()
        self._mp4_adapter = Mp4Adapter()
        self._vlc_adapter = VlcAdapter()
    
    def play(self, audio_type: str, file_name: str):
        audio_type_lower = audio_type.lower()
        
        if audio_type_lower == "mp3":
            return self._mp3_adapter.play(audio_type, file_name)
        elif audio_type_lower == "mp4":
            return self._mp4_adapter.play(audio_type, file_name)
        elif audio_type_lower == "vlc":
            return self._vlc_adapter.play(audio_type, file_name)
        else:
            raise ValueError(f"Invalid media type: {audio_type}")


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Adapter Pattern - Media Player Example")
    print("=" * 60)
    print()
    
    player = AudioPlayer()
    
    # Play different formats using the same interface
    print("Playing different media formats:")
    print("-" * 60)
    
    try:
        player.play("mp3", "song.mp3")
        print()
        
        player.play("mp4", "movie.mp4")
        print()
        
        player.play("vlc", "video.vlc")
        print()
        
        # Try unsupported format
        print("Attempting to play unsupported format:")
        print("-" * 60)
        player.play("avi", "video.avi")
    except ValueError as e:
        print(f"❌ Error: {e}")
    print()
    
    print("=" * 60)
    print("Key Benefit: Can use incompatible interfaces (Mp3Player,")
    print("Mp4Player, VlcPlayer) through a unified MediaPlayer interface!")
    print("=" * 60)

