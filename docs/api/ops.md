# ordo.ops

::: ordo.ops

## Overview

The `ordo.ops` module provides the abstract `Operation` base class for implementing reversible filesystem operations. All operations must work with relative paths only for security reasons.

## Operation Class

The `Operation` class is an abstract base class that defines the interface for all filesystem operations in ordo. Each operation must implement:

- `apply()`: Execute the operation
- `undo()`: Reverse the operation
- `to_dict()`: Serialize the operation to a dictionary
- `from_dict()`: Deserialize an operation from a dictionary

## Path Safety

All operations enforce strict path safety rules:

- **Relative paths only**: Absolute paths are not allowed
- **No parent directory traversal**: Paths containing `..` are rejected
- **Validation on creation and deserialization**: All paths are validated when creating operations and when deserializing from dictionaries

Use the `validate_path()` static method to validate paths before using them in operations.

## Example Usage

```python
from ordo.ops import Operation

class MyOperation(Operation):
    def __init__(self, source: str, target: str):
        self.source = self.validate_path(source)
        self.target = self.validate_path(target)

    def apply(self):
        # Implement the operation
        pass

    def undo(self):
        # Reverse the operation
        pass

    def to_dict(self):
        return {
            "type": "MyOperation",
            "source": self.source,
            "target": self.target
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["source"], data["target"])
```
