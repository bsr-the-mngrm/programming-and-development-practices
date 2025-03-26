class Person:
    """A simple class to represent a person.
    
    Demonstrates usage of many special methods such as __new__, __init__, __getattribute__,
    __setattr__, __delattr__, __str__, __repr__, comparison methods, pickling methods,
    and others.
    """
    
    def __new__(cls, name, age):
        # Called before __init__ to create a new instance.
        print(f"Creating instance for {name}")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age):
        # Initialize instance attributes.
        self.name = name
        self.age = age

    def __init_subclass__(cls, **kwargs):
        # Called automatically when a subclass of Person is created.
        super().__init_subclass__(**kwargs)
        print(f"New subclass of Person created: {cls.__name__}")

    def __getattribute__(self, name):
        # Intercepts all attribute access.
        value = super().__getattribute__(name)
        print(f"Accessed attribute '{name}': {value}")
        return value

    def __setattr__(self, name, value):
        # Intercepts setting an attribute.
        print(f"Setting attribute {name} to {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        # Intercepts deletion of an attribute.
        print(f"Deleting attribute {name}")
        super().__delattr__(name)

    def __str__(self):
        # Returns a user-friendly string representation.
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        # Returns an unambiguous string representation.
        return f"Person(name='{self.name}', age={self.age})"

    def __eq__(self, other):
        # Defines equality based on name and age.
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return NotImplemented

    def __ne__(self, other):
        # Defines inequality as the inverse of equality.
        eq_result = self.__eq__(other)
        if eq_result is NotImplemented:
            return NotImplemented
        return not eq_result

    def __hash__(self):
        # Allows the object to be used in hashed collections.
        return hash((self.name, self.age))

    def __format__(self, format_spec):
        # Custom formatting: if format_spec is "short", return only the name.
        if format_spec == "short":
            return f"{self.name}"
        return str(self)

    def __ge__(self, other):
        # Greater than or equal comparison based on age.
        if isinstance(other, Person):
            return self.age >= other.age
        return NotImplemented

    def __gt__(self, other):
        # Greater than comparison based on age.
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __le__(self, other):
        # Less than or equal comparison based on age.
        if isinstance(other, Person):
            return self.age <= other.age
        return NotImplemented

    def __lt__(self, other):
        # Less than comparison based on age.
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __dir__(self):
        # Customizes the list of attributes shown by dir().
        return ['name', 'age', '__class__', '__doc__', '__eq__', '__hash__', '__format__',
                '__ge__', '__getattribute__', '__getstate__', '__gt__', '__init__', '__init_subclass__',
                '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
                '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

    def __getstate__(self):
        # Custom state for pickling.
        state = self.__dict__.copy()
        state['extra'] = 'extra state'
        return state

    def __reduce__(self):
        # Helps the pickling process by specifying how to reconstruct the object.
        return (self.__class__, (self.name, self.age))

    def __reduce_ex__(self, protocol):
        # For protocol-specific pickling, simply delegate to __reduce__.
        return self.__reduce__()

    def __sizeof__(self):
        # Returns a custom size (this example adds an arbitrary constant).
        size = super().__sizeof__()
        return size + 10

    @classmethod
    def __subclasshook__(cls, C):
        # Customizes isinstance() and issubclass() behavior.
        if cls is Person:
            if any("name" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented


# -------------------- Usage Examples --------------------
if __name__ == "__main__":
    p1 = Person("Alice", 30)
    p2 = Person("Bob", 25)

    # String representations
    print("str(p1):", str(p1))
    print("repr(p1):", repr(p1))

    # Custom format using __format__
    print("Formatted (short):", format(p1, "short"))

    # Comparison based on age
    print("Is p1 > p2?:", p1 > p2)
    print("Is p1 >= p2?:", p1 >= p2)
    print("Is p1 < p2?:", p1 < p2)
    print("Is p1 <= p2?:", p1 <= p2)
    print("Are p1 and p2 equal?:", p1 == p2)
    print("Are p1 and p2 not equal?:", p1 != p2)

    # Hash and directory listing
    print("Hash of p1:", hash(p1))
    print("Directory of p1:", dir(p1))

    # Demonstrate pickling-related methods
    print("State of p1 (__getstate__):", p1.__getstate__())
    print("Reduced p1 (__reduce__):", p1.__reduce__())

    # Object size
    print("Size of p1:", p1.__sizeof__())

    # Access built-in attributes
    print("Class of p1 (__class__):", p1.__class__)
    print("Dictionary of p1 (__dict__):", p1.__dict__)
    print("Documentation (__doc__):", Person.__doc__)
    print("Module of p1 (__module__):", p1.__module__)
    print("Weak reference attribute (__weakref__):", getattr(p1, '__weakref__', None))

    # Test attribute access interception (triggers __getattribute__)
    _ = p1.name

    # Test deleting an attribute (triggers __delattr__)
    del p1.age

    # Creating a subclass to trigger __init_subclass__
    class Employee(Person):
        def __init__(self, name, age, employee_id):
            super().__init__(name, age)
            self.employee_id = employee_id

        def __repr__(self):
            return f"Employee(name='{self.name}', age={self.age}, id={self.employee_id})"
    
    emp = Employee("Charlie", 28, "E123")
    print("Employee instance:", repr(emp))
