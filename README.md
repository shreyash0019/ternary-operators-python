
# Ternary Operators in Python

This repository demonstrates the usage of ternary operators in Python for concise conditional expressions. The project includes examples of using ternary operators to simplify conditional logic and make the code more readable.

## Features

- **Basic Syntax**: Use of Python's ternary operator for simple conditions.
- **Conditional Assignment**: Assign values based on a condition.
- **Nested Ternary Operators**: Use ternary operators within other ternary operators.
- **Multiple Examples**: Various examples to demonstrate different use cases of ternary operators.

## Example Usage

### Basic Syntax

```python
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)  # Output: Odd
```

### Nested Ternary Operator

```python
x = 10
result = "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(result)  # Output: Positive
```

### Conditional Assignment

```python
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shreyash0019/ternary-operators-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ternary-operators-python
   ```

### Usage

1. Run the main script:
   ```bash
   python ternary_example.py
   ```

2. You can modify and experiment with ternary operator examples within the `ternary_example.py` file.

### Example Output

#### Case 1: Simple Conditional Check
```text
Odd
```

#### Case 2: Nested Ternary Operator
```text
Positive
```

#### Case 3: Conditional Assignment
```text
Adult
```

## Project Structure

```
Ternary Operators in Python
├── ternary_example.py     # Contains examples of ternary operators usage
├── README.md              # Project documentation
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out:

- **Name**: Shreyash Ingle
- **Email**: ingleshreyas01@gmail.com
