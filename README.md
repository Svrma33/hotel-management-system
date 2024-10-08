# Hotel Booking System

## Project Overview

The Hotel Booking System is a comprehensive application designed to manage hotel reservations efficiently. This system allows users to register, log in, and book rooms while managing customer details, room types, and pricing structures. It uses a MySQL database to store and retrieve data.

## Features

- **User Registration**: New users can register by providing necessary details.
- **User Login**: Registered users can log in to access their booking functionalities.
- **Room Booking**: Users can check room availability, book rooms, and calculate total costs including taxes.
- **Customer Management**: Manage customer details like name, contact number, email, nationality, and address.
- **Search Functionality**: Search for rooms based on specific criteria.
- **Price Calculation**: Calculate total room costs based on room type and meal preferences.

## Technology Stack

- **Frontend**: Tkinter (for GUI)
- **Backend**: Python
- **Database**: MySQL

## Installation

### Prerequisites

- Python 3.x
- MySQL Server
- Required Python libraries (e.g., mysql-connector-python, Tkinter)

### Setup Instructions

### 1. Download or CLone this repository
### 2. Install the required Python packages:
```bash
pip install mysql-connector-python
```
### 3. Set up the MySQL database:
- Create a database named `hotel_db`,`login`,`users_db`
- Create necessary tables for:<pre>
  hotel_db - (`customer`, `details`, `room`)
  login    - (`registernow`)
  users_db - (`users`)
  </pre>

### File Structure and Functionality
<pre>hotel-booking-system/
│
├── customer.py      # Handles customer-related functionalities
├── details.py       # Manages detailed views and information display
├── hotel.py         # Core hotel functionalities and room management
├── login.py         # User login functionality
├── register.py      # User registration process
└── room.py          # Room booking and management interface
</pre>
### 1. customer.py
Purpose: This file manages all functionalities related to customer details.
Key Features:
Add Customer: Function to add new customer details to the database.
View Customer: Functionality to retrieve and display customer information.
Update Customer: Function to modify existing customer details based on user input.
Delete Customer: Ability to remove customer records from the system.
### 2. details.py
Purpose: Manages the detailed views and information display in the application.
Key Features:
Display Room Details: Functionality to present detailed information about available rooms.
Show Customer Information: Method to present specific customer data after login or during searches.
Booking Summary: Generate and display a summary of bookings made by the customer.
### 3. hotel.py
**Purpose:** Contains core functionalities related to hotel management.
Key Features:
**Room Availability:** Function to check available rooms based on user-defined criteria.
**Booking Management:** Manage bookings by adding, updating, or deleting reservations.
**Price Calculation:** Calculate room prices based on room type, number of guests, and additional services.
### 4. login.py
**Purpose:** Handles user authentication processes.
**Key Features:**
**Login Functionality:** Validate user credentials against stored data.
**Session Management:** Maintain user session states after successful login.
**Error Handling:** Provide feedback for unsuccessful login attempts.
### 5. register.py
**Purpose:** Manages the user registration process.
**Key Features:**
**Registration Form:** Present a form for new users to fill in their details.
**Validation:** Check for duplicate usernames or emails and validate input data.
**Database Interaction:** Add new user details to the database upon successful registration.
### 6. room.py
**Purpose:** Acts as the main interface for room booking and management.
**Key Features:**
**User Interface:** Provides a GUI for users to interact with the booking system.
**Booking Process:** Integrates functions from hotel.py and customer.py to facilitate room bookings.
### Usage
After launching the `login.py`, users can register or log in.
Navigate through the options to book a room, view customer details, or calculate pricing based on selected options.
Follow on-screen instructions to complete bookings.
