# Lab 5: Static Code Analysis
## Blood Donation Management System

### 1. Issues Identified

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Hardcoded password | Security - Low | 5 | Password stored in source code | Read from an environment variable |
| Use of assert | Security - Low | 18 | Assertion used for input validation | Raise ValueError for invalid input |
| Mutable default argument | Bug | 17 | Default list may be shared across calls | Use None and initialize a new list |
| Broad exception handling | Code quality | 45 | Catches unexpected errors | Validate input and handle specific errors |
| Unsafe temporary file | Security - Medium | 60 | Uses insecure mktemp() | Use NamedTemporaryFile |
| Shell command execution | Security - High | 65 | Uses os.system() | Use subprocess.run() with shell=False |
| Missing module docstring | Code quality | 1 | Module purpose is undocumented | Add a module docstring |
| Missing function docstrings | Code quality | Multiple | Functions lack descriptions | Add function docstrings |
| Naming violations | Code quality | Multiple | Uses camelCase names | Use snake_case |
| Long line | Style | 7 | Line exceeds 79 characters | Split the line |
| Excess blank lines | Style | 58 | Too many blank lines | Remove extra blank lines |
| Inline comment spacing | Style | 80 | Incorrect comment spacing | Add two spaces before comment |
| Missing operator spacing | Style | 81 | Missing spaces around assignment | Add spaces around the operator |

### 2. Tools Used

- Pylint: Checks code quality and programming practices.
- Bandit: Checks potential security vulnerabilities.
- Flake8: Checks formatting and Python style.

### 3. Verification

After fixing the code:

- Achieve a Pylint score above 9.5/10.
- Address the Bandit findings.
- Fix Flake8 formatting violations.
- Run the program to verify its functionality.

### 4. Conclusion

Static code analysis helped identify security issues, potential bugs,
naming violations, and formatting problems. Fixing these issues improves
code readability, security, and maintainability.