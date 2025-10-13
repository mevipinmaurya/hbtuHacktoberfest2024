# Utility Classes

This document outlines a set of small, single-purpose utility classes designed to handle common styling patterns efficiently. They are built to be mobile-friendly and have low CSS specificity.

---

### `.sr-only`

**Purpose**: Hides an element visually while keeping it accessible to screen readers and other assistive technologies. This is crucial for providing context that is obvious visually but needs to be explicitly stated for non-visual users.

**Usage**: Apply this class to any element that should only be available to screen readers.

### `.stack`

**Purpose**: Provides consistent vertical spacing between sibling elements. It automatically adds a margin-top to every direct child element except for the first one, creating a clean vertical rhythm.

**Usage**: Apply this class to a container element. The spacing can be customized by setting the --stack-space CSS custom property. The default space is 1.5rem.

### `.grid-2`

**Purpose**: Creates a responsive two-column grid layout. It is mobile-first, displaying content in a single vertical column on small screens and automatically switching to a two-column grid on larger screens (≥768px).

**Usage**: Apply this class to a container element. The direct children of this container will become the grid items.

### `.btn-sm`

**Purpose**: A size modifier used to create a smaller, more compact version of a button. It is not intended to be used by itself.

**Usage**: Add the .btn-sm class to an element that already has the base .btn class. It works by reducing the padding and font size.
