# Decorator Pattern - Example 2: Text Formatting

## Problem Description

A text editor needs to apply multiple formatting options (bold, italic, underline, strikethrough) to text. Users should be able to combine these formats in any way. The Decorator pattern allows stacking formatting decorators on a base text component.

**Real-world usage**: Used in rich text editors (Word, Google Docs), markdown processors, HTML rendering engines, and text styling libraries.

## Class Diagram

```
                    ┌─────────────────────┐
                    │    TextComponent    │
                    │  (Component)        │
                    ├─────────────────────┤
                    │ + render()          │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │                              │
    ┌───────────▼──────┐          ┌───────────▼──────────┐
    │   PlainText      │          │  TextDecorator       │
    │  (Concrete)      │          │   (Decorator)        │
    ├──────────────────┤          ├──────────────────────┤
    │ + render()       │          │ - component          │
    └──────────────────┘          │ + render()           │
                                   └──────────┬───────────┘
                                              │
                    ┌─────────────────────────┼─────────────────────────┐
                    │                         │                         │
        ┌───────────▼──────┐    ┌─────────────▼──────┐    ┌─────────────▼──────┐
        │  BoldDecorator   │    │ ItalicDecorator    │    │ UnderlineDecorator │
        ├──────────────────┤    ├────────────────────┤    ├────────────────────┤
        │ + render()       │    │ + render()         │    │ + render()         │
        └──────────────────┘    └────────────────────┘    └────────────────────┘
```

