# Cinema Seat Booking System

A Python console application to manage movie theater seat bookings with color-coded seating, booking, cancellation, and persistent storage.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [Author](#author)  

---

## Overview

The Cinema Seat Booking System allows users to:

- Select from multiple movies and showtimes.  
- View a 10x10 color-coded seating layout by seat type: Platinum, Gold, Silver.  
- Book seats and generate a receipt with the total price.  
- Cancel booked seats with a partial refund (60% policy).  
- Save and load seat layouts for each movie and showtime, so bookings persist across sessions.  

---

## Features

- **Color-coded seat display**:  
  - Platinum (A-C) – Magenta  
  - Gold (D-F) – Yellow  
  - Silver (G-J) – Cyan  

- **Persistent seat storage**: Bookings are saved to a file for each movie and showtime.  
- **Booking and cancellation** with receipt generation.  
- **Error handling** for invalid seat entries and duplicate bookings.  

---

## Technologies Used

- **Python 3.x**  
- **Colorama** for colored console output  
- **OS module** for file handling  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/CinemaSeatBooking.git
