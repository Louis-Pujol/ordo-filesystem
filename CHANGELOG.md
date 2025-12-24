# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Abstract `Operation` base class in `ordo.ops.operation` module with:
  - `apply()` method for executing operations
  - `undo()` method for reversing operations
  - `to_dict()` method for serializing operations
  - `from_dict()` class method for deserializing operations
  - `validate_path()` static method for path validation
- Path safety enforcement: all operations must use relative paths only
- Automatic rejection of absolute paths and paths containing `..`
- Comprehensive unit tests for operation serialization and path validation

## [0.1.0] - 2025-12-24

### Added

PR [#1](https://github.com/Louis-Pujol/ordo-filesystem/pull/1) package structure:

- Initial package structure with src-layout, PEP 621 compliant with hatchling build backend and dynamic versioning, MIT License
- Pre-commit hooks with ruff linter/formatter with renovate bot
- GitHub Actions workflows: build, tests, docs deployment, PyPI/GHCR publishing
- Dockerfile (Python 3.12-slim)
- MkDocs documentation with Material theme



[Unreleased]: https://github.com/Louis-Pujol/ordo-filesystem/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Louis-Pujol/ordo-filesystem/releases/tag/v0.1.0
