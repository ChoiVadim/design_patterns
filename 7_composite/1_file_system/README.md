# Composite Pattern - Example 1: File System

## Problem Description

A file system contains files and folders. Folders can contain files and other folders. We need to perform operations (like calculating total size, listing contents) on both files and folders uniformly. The Composite pattern treats individual objects and compositions uniformly.

**Real-world usage**: Used in file systems, GUI component hierarchies (windows containing panels containing buttons), organization charts, XML/HTML DOM trees, and menu systems.

## Class Diagram

```
                    ┌─────────────────────┐
                    │   FileSystemItem    │
                    │  (Component)        │
                    ├─────────────────────┤
                    │ + getName()         │
                    │ + getSize()         │
                    │ + display()         │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │                              │
    ┌───────────▼──────┐          ┌───────────▼──────────┐
    │      File       │          │      Folder          │
    │  (Leaf)         │          │  (Composite)        │
    ├─────────────────┤          ├──────────────────────┤
    │ - name          │          │ - name               │
    │ - size          │          │ - children[]         │
    │ + getName()     │          │ + getName()          │
    │ + getSize()     │          │ + getSize()          │
    │ + display()     │          │ + display()          │
    └─────────────────┘          │ + add(item)          │
                                  │ + remove(item)       │
                                  └──────────────────────┘
```

