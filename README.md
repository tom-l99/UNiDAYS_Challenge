# UNiDAYS Software Engineer Intern Discount Challenge

## Instructions
* Coded in Python 3
* Download file or copy all raw code (UniDays_main.py)
* Run with any Python IDE, it is simplest to view and run the code using [IDLE](https://www.python.org/downloads/) - (I coded the program with this).
* Test cases can be accessed at the bottom of the code in the __main__ section (add, edit or remove item dictionary keys)

## Approach 
I originally approached the program by splitting the rules from a dictionary to use the numerical values to perform calculations to work out the cost.
After re-reading the task, I decided that hardcoding pricing rules was not expandable should future rules be added, or existing rules edited.
Instead, I created a 3-dimensional dictionary to list the given pricing rules, formatting it so that the amount requirement and affected price values were able to be accessed.
This has allowed for my program to be expandable in regards to altering pricing rules as well as providing a reduced line count.
