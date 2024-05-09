

# File Structure

- `problem1.py`: Implementation of the solution to Problem 1.
- `problem2.py`: Implementation of the solution to Problem 2.
- `calendar.py`: Implementation of the solution to Problem 3.

# Problem Descriptions

### Problem 1: Data Stream Ingestion
In this problem, I implemented a system that processes a data stream of strings along with timestamps. The system ensures that each unique string is printed at most every 5 seconds.

### Problem 2: Fuel Station Design
For Problem 2, I designed a fuel station capable of handling three types of vehicles: diesel, petrol, and electric. The station has a fixed number of slots for each type of vehicle, and it provides methods for fueling vehicles and opening fuel slots.

### Problem 3: Calendar Design
Problem 3 involved implementing a calendar program that allows users to add events without causing double bookings. I created a `Calendar` class along with a `Node` class to manage event intervals and prevent overlapping bookings.

# Debugging the Calendar Design

## Issue Identification
The original implementation of the calendar program did not correctly handle double bookings. Events were being inserted into the calendar without properly checking for overlaps with existing events.

## Debugging Steps
1. **Understanding the Original Implementation**:
   - I carefully reviewed the code provided to understand its structure and logic flow.
   - Identified the `Node` class responsible for representing event intervals and the `Calendar` class for managing these intervals.

2. **Identifying the Problem**:
   - Observed that the `insert` method in the `Node` class did not correctly check for overlapping intervals.
   - Realized that the conditionals in the `insert` method needed to be adjusted to properly handle different scenarios of overlap.

3. **Adjusting the Conditionals**:
   - Modified the conditionals in the `insert` method to correctly handle cases where the new event overlaps with existing events.
   - Implemented conditionals to check if the new event starts after the end of the current event or ends before the start of the current event, indicating no overlap.
   - Added a conditional to handle cases where the new event overlaps with the current event, preventing insertion and returning False.

4. **Testing the Fixed Implementation**:
   - Created instances of the `Calendar` class and tested the `book` method with various input intervals to verify that double bookings were properly prevented.
   - Ensured that the method returned True for valid bookings and False for double bookings.


## Instructions for Running the Code

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the Python scripts.
4. Execute each script using the Python interpreter. For example:

$ python problem1.py
