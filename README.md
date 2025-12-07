# Cinema Seat Booking System

Author

R. Lakshmithra
This was my first Python project, completed as a part of my course to demonstrate practical understanding of Python programming concepts and console applications.
A Python console application for booking and managing movie theater seats with color-coded seating and persistent storage. 

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Technology Stack](#technology-stack)  
- [Installation & Setup](#installation--setup)   

---

## Project Overview

The Cinema Seat Booking System is a console-based Python application that allows users to:

- Select movies and showtimes.  
- View a color-coded seating layout based on seat types (Platinum, Gold, Silver).  
- Book and cancel seats with real-time updates.  
- Persist seat booking information in files for future sessions.  

This project demonstrates file handling, user input validation, use of libraries like `colorama` for console output, and fundamental Python programming concepts.

---

## Features

- **Movie and Showtime Selection:** Choose from multiple movies and showtimes.  
- **Color-coded Seat Layout:** Different seat types are displayed in distinct colors for better clarity:
  - Platinum: Magenta  
  - Gold: Yellow  
  - Silver: Cyan  
- **Booking and Cancellation:** Users can book multiple seats at once or cancel them with a partial refund policy.  
- **Persistent Storage:** Seat layouts are saved to files to retain booking information across sessions.  
- **Receipt Generation:** Displays a summary of booked seats and total price.  

---

## Technology Stack

- **Programming Language:** Python 3.x  
- **Libraries:**  
  - `colorama` for colored console output  
  - `os` for file handling and checking file existence  

---

## Installation & Setup

1. Make sure you have **Python 3.x** installed on your system.  
2. Clone this repository or download the `.py` file.  
3. Install the required library `colorama` if not already installed:  

```bash
pip install colorama
