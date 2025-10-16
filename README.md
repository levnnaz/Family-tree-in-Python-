# Family Tree Handling System

This project is a Python-based Family Tree Handling System developed by students at the University of Greenwich. 
The system allows users to explore a family tree by viewing relationships such as parents, children, siblings, cousins, spouses, and extended family. 
It also includes features for calculating birthdays, average age at death, number of children, and generating birthday calendars.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [System Requirements](#system-requirements)
4. [Repository Structure](#repository-structure)
5. [How to Run](#how-to-run)
6. [Example Usage](#example-usage)
7. [Object-Oriented Design Overview](#object-oriented-design-overview)
8. [Summary](#summary)
   
---

## Project Overview

The Family Tree Handling System is designed to manage and explore family relationships in an organized way. 
Users can retrieve information about parents, children, siblings, cousins, and spouses, as well as calculate important family statistics such as average age at death and average number of children. 
The system uses Object-Oriented Programming principles to maintain a modular, extensible, and reusable codebase. 
It also includes a user-friendly console interface where users can select options to view or calculate specific family data.

---

## Features

| **No.** | **Feature Description** |
|----------|--------------------------|
| **1** | Display parents of a selected family member. |
| **2** | Display children of a selected family member. |
| **3** | Display the spouse(s) of a selected family member. |
| **4** | Display siblings of a selected family member. |
| **5** | Display cousins of a selected family member. |
| **6** | Display birthdays of all members in the family tree. |
| **7** | Display a sorted birthday calendar (ignoring birth year). |
| **8** | Display grandchildren of a selected family member. |
| **9** | Display immediate family (parents, siblings, spouse, children). |
| **10** | Display extended family (living blood relatives including aunts, uncles, and cousins). |
| **11** | Calculate the average age at death in the family tree. |
| **12** | Display the number of children for a selected member. |
| **13** | Calculate the average number of children per person in the family tree. |
   
---

## System Requirements

- Python 3.8 or higher
- No additional libraries are required; the project uses only built-in Python modules.
- Compatible with Windows, macOS, and Linux.

---

## Repository Structure

- `main.py` – Entry point of the program.
- `member_class.py` – Defines the `Member` class with attributes and methods for a family member.
- `familytree_class.py` – Contains the `FamilyTree` class with methods to find relationships.
- `immediate_family_class.py` – Contains the `ImmediateFamily` class to display immediate and extended family.
- `birthdays_class.py` – Contains the `Birthdays` class for handling birthdays and creating a birthday calendar.
- `calculations_class.py` – Contains the `Calculations` class for average age and children calculations.
- `familytree_database.py` – Holds the family tree data and relationships.
- `Coursework_1_full_code.py` – Full combined code of all classes and features.
- `README.md` – This file.

---

## How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/family-tree-system.git
2. Navigate to the project directory:

   ```bash
   cd family-tree-system
3. Run the main program:

   ```bash
   python main.py
4. Follow the console prompts to choose an option (1-13) and enter the name of a family member as required.

---

## Example Usage

- To find the parents of "Otto Emmersohn":
  1. Choose option 1 from the menu.
  2. Enter `Otto Emmersohn`.
  3. The program will display Otto’s parents.

- To display the sorted birthday calendar:
  1. Choose option 7 from the menu.
  2. The program will display all birthdays sorted by day and month.

---

## Object-Oriented Design Overview

The system uses object-oriented programming with the following key classes:

- `Member`: Encapsulates information about each family member (name, birth date, death year, parents, spouse(s)).
- `FamilyTree`: Inherits from `Member` and includes methods for retrieving parents, children, siblings, cousins, and grandchildren.
- `ImmediateFamily`: Inherits from `FamilyTree` and provides methods to get immediate and extended family.
- `Birthdays`: Inherits from `FamilyTree` and handles birthdays and sorting birthday calendars.
- `Calculations`: Inherits from `FamilyTree` and calculates average age at death, number of children, and average children per person.

---

## Summary

The Family Tree Handling System provides a complete solution for exploring and analyzing family relationships using Python and Object-Oriented Programming principles. 
It allows users to view immediate and extended family, calculate important statistics like average age at death and number of children, and manage birthdays efficiently. 
This project demonstrates clean design, modular code, and a user-friendly console interface, making it a valuable educational tool and a strong addition to a programming portfolio.



  

