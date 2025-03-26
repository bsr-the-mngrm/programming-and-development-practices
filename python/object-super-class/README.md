# Extended Person Class with Dunder Methods

## Overview
This Python script defines an extended `Person` class that overrides most of the built-in special methods (often called "dunder" methods). The purpose is to illustrate how you can customize object behavior for creation, initialization, attribute access, formatting, comparisons, pickling, and more.

## Key Methods Implemented
- **Creation & Initialization:**
  - `__new__`: Logs instance creation.
  - `__init__`: Sets up initial attributes.
- **Attribute Management:**
  - `__getattribute__`: Intercepts attribute access for debugging.
  - `__setattr__` and `__delattr__`: Log changes and deletions of attributes.
- **String Representations:**
  - `__str__`: Provides a human-friendly description.
  - `__repr__`: Offers an unambiguous representation for debugging.
- **Comparisons:**
  - `__eq__`, `__ne__`: Define equality and inequality based on name and age.
  - `__ge__`, `__gt__`, `__le__`, `__lt__`: Compare instances based on age.
- **Formatting:**
  - `__format__`: Supports custom formatting (e.g., "short" format).
- **Pickling Support:**
  - `__getstate__`, `__reduce__`, `__reduce_ex__`: Enable and customize pickling behavior.
- **Additional Methods:**
  - `__sizeof__`: Returns a custom size metric for the object.
  - `__dir__`: Customizes the attributes shown by `dir()`.
  - `__init_subclass__`: Notifies when a subclass is created.
  - `__subclasshook__`: Alters isinstance/issubclass behavior.
- **Built-In Attributes:**
  - Attributes like `__class__`, `__dict__`, `__doc__`, `__module__`, and `__weakref__` are also highlighted.

## Usage Examples
- **Creation and Representation:**  
  Instantiate objects and display both `str` and `repr` representations.
- **Comparison and Formatting:**  
  Compare two `Person` objects using custom comparison operators and custom formatting.
- **Pickling & Size:**  
  Demonstrates retrieving an object's state and custom size.
- **Attribute Operations:**  
  Shows logging for attribute access, setting, and deletion.
- **Subclassing:**  
  Creating an `Employee` subclass to trigger `__init_subclass__`.


This code serves as a comprehensive demonstration of how Python’s object model can be extended and customized using special methods.
