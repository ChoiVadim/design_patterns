# Adapter Pattern - Example 1: Media Player

## Problem Description

A media player application needs to play different audio/video formats (MP3, MP4, VLC). The existing player only supports MP3, but we need to integrate support for MP4 and VLC formats without modifying the existing code. The Adapter pattern allows incompatible interfaces to work together.

**Real-world usage**: Used in API integrations, legacy system integration, third-party library wrappers, payment gateway integrations, and database adapters (ORM).

## Class Diagram

```
                    ┌─────────────────────┐
                    │   MediaPlayer       │
                    │  (Target)           │
                    ├─────────────────────┤
                    │ + play(audioType,   │
                    │        fileName)    │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   AudioPlayer      │
                    │  (Adapter)         │
                    ├────────────────────┤
                    │ - mp3Player        │
                    │ - mp4Adapter       │
                    │ - vlcAdapter       │
                    │ + play()           │
                    └────────────────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
    ┌───────────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
    │   Mp3Player     │ │ Mp4Player  │ │ VlcPlayer  │
    │  (Adaptee)      │ │ (Adaptee)  │ │ (Adaptee)  │
    ├──────────────────┤ ├────────────┤ ├────────────┤
    │ + playMp3()     │ │ + playMp4() │ │ + playVlc()│
    └──────────────────┘ └────────────┘ └────────────┘
```

