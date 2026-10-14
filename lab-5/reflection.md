# Lab 5: Static Code Analysis
## Reflection

### 1. What is static code analysis?

Static code analysis is the process of checking source code without executing it.
It helps identify programming mistakes, security vulnerabilities, and formatting
problems before the software is deployed.

### 2. What is the purpose of Pylint, Bandit, and Flake8?

- Pylint checks code quality, naming conventions, missing docstrings, and
  potential programming problems.
- Bandit checks Python code for potential security vulnerabilities.
- Flake8 checks Python formatting and style violations.

### 3. What issues did you identify and fix?

The analysis identified a hardcoded password, use of assert for validation,
a mutable default argument, broad exception handling, unsafe temporary-file
creation, shell command execution, naming violations, missing docstrings,
and formatting problems.

These issues were addressed by improving input validation, using safer
file and process handling, following Python naming conventions, adding
documentation, and correcting formatting.

### 4. How does static code analysis improve software quality?

Static code analysis helps developers identify problems early, improve security,
maintain consistent coding standards, and make programs easier to read and
maintain. Running the tools again after fixing the code helps verify the
improvements.