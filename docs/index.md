# Ordo

Reversible filesystem operations for Python.

## Overview

**Ordo** is a Python package designed to provide reversible, non-destructive filesystem operations with built-in undo capabilities.

### Project Goals

**Short-term goal:** Implement reversible, non-destructive filesystem operations that can be safely undone.

**Long-term goal:** Connect with an LLM agent to enable intelligent, safe filesystem management.

## Features (Planned)

- ✨ Reversible file operations (move, copy, delete, modify)
- 📜 Operation history and undo capabilities
- 🛡️ Non-destructive by default
- 🔒 Safe filesystem management
- 🤖 LLM agent integration (future)

## Installation

Install from PyPI:

```bash
pip install ordo
```

Or install from source:

```bash
git clone https://github.com/Louis-Pujol/ordo-filesystem.git
cd ordo-filesystem
pip install -e .
```

## Quick Start

```python
import ordo

# More examples coming soon as features are implemented
```

## Module Structure

The package is organized into several modules:

- **`ordo.core`**: Core functionality and base classes
- **`ordo.fs`**: Filesystem operations interface
- **`ordo.ops`**: Specific operation implementations
- **`ordo.undo`**: Undo/redo functionality

## Development

This package is in early development. Contributions are welcome!

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/Louis-Pujol/ordo-filesystem.git
cd ordo-filesystem

# Install in editable mode
pip install -e .

# Install development dependencies
pip install -e .[dev,docs]

# Setup pre-commit hooks
pre-commit install
```

### Running tests

```bash
# Run tests (when available)
pytest
```

### Building documentation

```bash
# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## License

MIT License - see [LICENSE](https://github.com/Louis-Pujol/ordo-filesystem/blob/main/LICENSE) file for details.

## Links

- [GitHub Repository](https://github.com/Louis-Pujol/ordo-filesystem)
- [Issue Tracker](https://github.com/Louis-Pujol/ordo-filesystem/issues)
- [API Reference](api/ordo.md)
