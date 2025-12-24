"""Abstract base class for filesystem operations."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Operation(ABC):
    """Abstract base class for reversible filesystem operations.

    All operations must work with relative paths only. Absolute paths
    and paths containing '..' are not allowed for security reasons.
    """

    @staticmethod
    def validate_path(path: str | Path) -> str:
        """Validate that a path is relative and safe.

        Args:
            path: The path to validate

        Returns:
            The validated path as a string

        Raises:
            ValueError: If the path is absolute or contains '..'
        """
        path_obj = Path(path)

        # Check if path is absolute
        if path_obj.is_absolute():
            raise ValueError(f"Absolute paths are not allowed: {path}")

        # Check for '..' in path parts
        if ".." in path_obj.parts:
            raise ValueError(f"Paths containing '..' are not allowed: {path}")

        return str(path_obj)

    @abstractmethod
    def apply(self) -> None:
        """Apply the operation.

        This method performs the filesystem operation.
        """
        pass

    @abstractmethod
    def undo(self) -> None:
        """Undo the operation.

        This method reverses the filesystem operation.
        """
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        """Serialize the operation to a dictionary.

        Returns:
            A dictionary representation of the operation that can be
            used to reconstruct it via from_dict().
        """
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict[str, Any]) -> "Operation":
        """Deserialize an operation from a dictionary.

        Args:
            data: Dictionary representation of the operation

        Returns:
            A new Operation instance
        """
        pass
