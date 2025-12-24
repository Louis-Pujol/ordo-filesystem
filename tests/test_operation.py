"""Unit tests for the Operation abstract base class."""

import pytest

from ordo.ops.operation import Operation


class ConcreteOperation(Operation):
    """Concrete implementation of Operation for testing."""

    def __init__(self, source: str, target: str):
        """Initialize with source and target paths.

        Args:
            source: Source path (must be relative)
            target: Target path (must be relative)
        """
        super().__init__()
        self.source = self.validate_path(source)
        self.target = self.validate_path(target)
        self.applied = False

    def apply(self) -> None:
        """Apply the operation."""
        self.applied = True

    def undo(self) -> None:
        """Undo the operation."""
        self.applied = False

    def to_dict(self) -> dict:
        """Serialize to dictionary."""
        return {
            "type": "ConcreteOperation",
            "source": self.source,
            "target": self.target,
            "applied": self.applied,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ConcreteOperation":
        """Deserialize from dictionary."""
        op = cls(data["source"], data["target"])
        op.applied = data.get("applied", False)
        return op


class TestOperationPathValidation:
    """Tests for path validation."""

    def test_valid_relative_path(self):
        """Test that valid relative paths are accepted."""
        op = ConcreteOperation("file.txt", "dest/file.txt")
        assert op.source == "file.txt"
        assert op.target == "dest/file.txt"

    def test_valid_nested_relative_path(self):
        """Test that nested relative paths are accepted."""
        op = ConcreteOperation("dir1/dir2/file.txt", "dir3/dir4/file.txt")
        assert op.source == "dir1/dir2/file.txt"
        assert op.target == "dir3/dir4/file.txt"

    def test_reject_absolute_posix_path(self):
        """Test that absolute POSIX paths are rejected."""
        with pytest.raises(ValueError, match="Absolute paths are not allowed"):
            ConcreteOperation("/absolute/path.txt", "relative.txt")

    def test_reject_parent_directory_reference(self):
        """Test that paths with '..' are rejected."""
        with pytest.raises(ValueError, match="Paths containing '..' are not allowed"):
            ConcreteOperation("../parent/file.txt", "relative.txt")

    def test_reject_parent_in_middle_of_path(self):
        """Test that '..' in the middle of a path is rejected."""
        with pytest.raises(ValueError, match="Paths containing '..' are not allowed"):
            ConcreteOperation("dir/../file.txt", "relative.txt")

    def test_reject_parent_in_target_path(self):
        """Test that '..' in target path is rejected."""
        with pytest.raises(ValueError, match="Paths containing '..' are not allowed"):
            ConcreteOperation("source.txt", "../target.txt")

    def test_validate_path_static_method(self):
        """Test the validate_path static method directly."""
        # Valid paths
        assert Operation.validate_path("file.txt") == "file.txt"
        assert Operation.validate_path("dir/file.txt") == "dir/file.txt"

        # Invalid paths
        with pytest.raises(ValueError):
            Operation.validate_path("/absolute/path.txt")

        with pytest.raises(ValueError):
            Operation.validate_path("../parent.txt")


class TestOperationSerialization:
    """Tests for operation serialization."""

    def test_to_dict(self):
        """Test serialization to dictionary."""
        op = ConcreteOperation("source.txt", "target.txt")
        data = op.to_dict()

        assert data["type"] == "ConcreteOperation"
        assert data["source"] == "source.txt"
        assert data["target"] == "target.txt"
        assert data["applied"] is False

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        data = {
            "type": "ConcreteOperation",
            "source": "source.txt",
            "target": "target.txt",
            "applied": False,
        }
        op = ConcreteOperation.from_dict(data)

        assert op.source == "source.txt"
        assert op.target == "target.txt"
        assert op.applied is False

    def test_serialization_roundtrip(self):
        """Test that serialization and deserialization preserve data."""
        original = ConcreteOperation("dir/source.txt", "other/target.txt")
        original.apply()

        # Serialize
        data = original.to_dict()

        # Deserialize
        restored = ConcreteOperation.from_dict(data)

        # Verify all data is preserved
        assert restored.source == original.source
        assert restored.target == original.target
        assert restored.applied == original.applied

    def test_serialization_rejects_unsafe_paths(self):
        """Test that deserialization validates paths."""
        # Try to deserialize data with absolute path
        data = {
            "type": "ConcreteOperation",
            "source": "/absolute/source.txt",
            "target": "target.txt",
            "applied": False,
        }

        with pytest.raises(ValueError, match="Absolute paths are not allowed"):
            ConcreteOperation.from_dict(data)

        # Try to deserialize data with '..' path
        data = {
            "type": "ConcreteOperation",
            "source": "source.txt",
            "target": "../target.txt",
            "applied": False,
        }

        with pytest.raises(ValueError, match="Paths containing '..' are not allowed"):
            ConcreteOperation.from_dict(data)


class TestOperationAbstractMethods:
    """Tests for abstract method implementation."""

    def test_cannot_instantiate_abstract_class(self):
        """Test that Operation cannot be instantiated directly."""
        with pytest.raises(TypeError):
            Operation()  # type: ignore

    def test_concrete_implementation_has_all_methods(self):
        """Test that concrete implementation has all required methods."""
        op = ConcreteOperation("source.txt", "target.txt")

        # Check all methods exist and are callable
        assert callable(op.apply)
        assert callable(op.undo)
        assert callable(op.to_dict)
        assert callable(op.from_dict)

    def test_apply_and_undo(self):
        """Test that apply and undo work correctly."""
        op = ConcreteOperation("source.txt", "target.txt")

        # Initially not applied
        assert op.applied is False

        # Apply
        op.apply()
        assert op.applied is True

        # Undo
        op.undo()
        assert op.applied is False
