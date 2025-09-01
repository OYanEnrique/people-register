# People Register

A simple Python project for registering and managing people data using a text-based interface.

## Features

- Register new people with name and age
- List all registered people
- Data stored in a text file (archive)
- Input validation and error handling
- User-friendly command-line interface

## Requirements

- Python 3.x

## How to Use

1. **Clone the repository:**
   ```
   git clone https://github.com/OYanEnrique/people-register.git
   cd people-register
   ```

2. **Run the program:**
   ```
   python system.py
   ```

3. **Menu Options:**
   - Register a new person
   - List all people
   - Exit

## Project Structure

```
archive.py      # Handles file operations (create, read, check existence)
interface.py    # User interface functions (input, menu, formatting)
system.py       # Main program logic and menu loop
```

## Example Usage

When you run the program, you will see a menu like:

```
------------------------------------------
         PEOPLE REGISTER SYSTEM
------------------------------------------
1 - Register a new person
2 - List all people
3 - Exit
------------------------------------------
```

Follow the prompts to add or view people.

## Error Handling

- Invalid input (non-integer age) is handled gracefully.
- Keyboard interruptions are caught and reported.
- File errors are displayed with colored messages.

## License

This project is licensed under the MIT License.
