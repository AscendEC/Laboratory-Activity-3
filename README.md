# Laboratory-Activity-3
Python OOP Structure

# Library Book Management System

A simple console-based **Library Book Management System** built using **Object-Oriented Programming (OOP)** in Python.

This program was created as a practice activity / laboratory requirement to demonstrate core OOP concepts.

## Disclaimer
This repository is created solely for educational purposes. The code, documentation, and all contents are submitted as a requirement for Laboratory Activity 2 of the CS15L course. This project is not intended for production use, commercial purposes, distribution as exemplary code, or as a reference for best practices in professional software development. No warranty of any kind is provided — express or implied. Use at your own risk.

© Ascend Earn Cañete / 553867

## Features
- Add book details (title, author, publication year) using user input
- Borrow a book (mark as unavailable)
- Return a book (mark as available again)
- Display complete book information and current availability status
- Simple menu-driven interface
- Basic input validation and error handling

## OOP Requirements Met
- **One class only**: `Book`
- **Attributes** (4):
  - `title` (string)
  - `author` (string)
  - `year` (integer)
  - `available` (boolean)
- **Methods** (5):
  - `set_book_info()`
  - `borrow_book()`
  - `return_book()`
  - `display_info()`
  - `is_available()`
- All data entry uses `input()`
- All output uses `print()`
- Runs entirely in the terminal/console

## How to Run 

1. **Clone this repository** to your computer  
   Open a terminal (Command Prompt, PowerShell, Terminal, Git Bash, etc.) and run:

   ```bash
   git clone https://github.com/AscendEC/Laboratory-Activity-3.git
