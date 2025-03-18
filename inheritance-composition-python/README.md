# Inheritance and Composition in Python – Code Samples

This repository contains sample code snippets extracted and adapted from the Real Python article "[Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/)" by Isaac Rodriguez (Jan 11, 2025).

## Overview

The article explains two major object-oriented programming concepts in Python:

- **Inheritance** – modeling an *"is a"* relationship where a derived class reuses and extends the functionality of a base class.
- **Composition** – modeling a *"has a"* relationship where a class contains objects of other classes to build complex structures.

This sample demonstrates a payroll system where different types of employees (salary, hourly, and commission) are modeled using inheritance. The abstract base class `Employee` defines the common interface, and specialized employee classes provide their own implementations of the payroll calculation.

## Repository Structure

- **hr.py**  
  Contains the definitions of:
  - `PayrollSystem`: processes a collection of employees.
  - `Employee`: an abstract base class that defines the required interface.
  - `SalaryEmployee`, `HourlyEmployee`, and `CommissionEmployee`: concrete subclasses that implement the payroll calculation differently.

- **program.py**  
  A small driver program that creates several employee objects and calls the payroll system to calculate and print each employee’s paycheck.

## How to Run

Make sure you have Python 3 installed. From the repository’s root directory, run:

```bash
python program.py
