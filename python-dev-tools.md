# Python Development Tools

This document covers essential libraries and extensions used in professional Python development. These tools help with package management, code formatting, linting, testing, and type checking.

## 1. Dependency Management

### **Poetry**
- A modern tool for dependency management and packaging in Python.
- Creates and manages virtual environments automatically.
- Uses a `pyproject.toml` file to specify dependencies.
- Command examples:
  ```sh
  poetry new my_project  # Create a new project
  poetry add requests  # Add a dependency
  poetry install  # Install dependencies
  ```

### **pip-tools**
- Provides `pip-compile` to create a `requirements.txt` file with pinned dependencies.
- Helps keep dependencies deterministic and reproducible.
- Command examples:
  ```sh
  pip-compile requirements.in  # Generate requirements.txt
  pip-sync  # Sync dependencies
  ```

### **virtualenv** / **venv**
- Used to create isolated Python environments.
- `venv` is built into Python 3.
- Command examples:
  ```sh
  python -m venv env  # Create a virtual environment
  source env/bin/activate  # Activate (Linux/macOS)
  env\Scripts\activate  # Activate (Windows)
  ```

## 2. Code Formatting

### **Black**
- Opinionated code formatter that enforces consistency.
- Command examples:
  ```sh
  black my_project/  # Format all Python files
  ```

### **isort**
- Automatically sorts and organizes imports.
- Command examples:
  ```sh
  isort my_project/  # Sort imports in all files
  ```

## 3. Linting

### **Flake8**
- A tool to check code against style and programming errors.
- Can be combined with plugins for additional checks.
- Command example:
  ```sh
  flake8 my_project/  # Run linting
  ```

### **Pylint**
- More configurable than Flake8, provides a score for code quality.
- Command example:
  ```sh
  pylint my_project/  # Run static analysis
  ```

## 4. Type Checking

### **Mypy**
- A static type checker for Python that enforces type hints.
- Helps catch potential errors before runtime.
- Command example:
  ```sh
  mypy my_project/  # Run type checking
  ```

## 5. Pre-commit Hooks

### **Pre-commit**
- Runs checks like linting and formatting before code is committed.
- Uses a `.pre-commit-config.yaml` file for configuration.
- Command examples:
  ```sh
  pre-commit install  # Set up pre-commit hooks
  pre-commit run --all-files  # Run checks manually
  ```

## 6. Testing

### **pytest**
- A powerful testing framework for Python.
- Supports fixtures, mocking, and parallel test execution.
- Command examples:
  ```sh
  pytest tests/  # Run all tests
  pytest -v -s  # Run with verbose output
  ```

### **unittest**
- Built-in Python testing framework.
- Command example:
  ```sh
  python -m unittest discover tests/  # Run all tests
  ```

## 7. Pretty Error Display

### **pretty_errors**
- Enhances Python tracebacks to make them more readable and visually appealing.
- Useful for debugging by providing color-coded and structured error messages.
- Command examples:
  ```sh
  pip install pretty-errors  # Install the package
  ```
- Usage example:
  ```python
  import pretty_errors
  ```
  Simply importing `pretty_errors` will modify the traceback formatting globally.

## Conclusion
Using these tools ensures a consistent, maintainable, and efficient Python development workflow. Each tool plays a specific role in improving code quality, reliability, and ease of collaboration.
