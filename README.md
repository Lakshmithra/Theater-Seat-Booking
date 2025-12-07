# Cinema Seat Booking System

A Python console application for managing movie theater seat bookings with color-coded seating, persistent storage, and receipt generation.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Technology Stack](#technology-stack)  
4. [Installation & Setup](#installation--setup)  
5. [Usage Instructions](#usage-instructions)  
6. [File Structure](#file-structure)  
7. [How It Works](#how-it-works)  
8. [Seat Types & Pricing](#seat-types--pricing)  
9. [Author & Date](#author--date)  

---

## Project Overview

The Cinema Seat Booking System is a Python-based console application designed to simulate a real-world theater booking experience. Users can select movies and showtimes, book or cancel seats, and see a color-coded seating chart. The system ensures seat availability is tracked persistently, so bookings remain saved between sessions.

This project is ideal for beginners to understand **Python file handling, console input/output, and color-coded terminal output**.

---

## Features

- **Movie & Showtime Selection:** Choose from multiple movies and showtimes.  
- **Color-Coded Seat Layout:** Seats are displayed in different colors according to type.  
- **Seat Booking:** Book one or more seats with automatic receipt generation.  
- **Seat Cancellation:** Cancel booked seats and receive a 60% refund.  
- **Persistent Storage:** Seat layouts are saved in files for each movie-showtime combination.  
- **Error Handling:** Handles invalid inputs and prevents double booking.  

---

## Technology Stack

- **Python 3.x** – main programming language  
- **Colorama** – for terminal color output  
- **OS module** – for file handling to persist seat layouts  

---

## Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/CinemaSeatBooking.git

