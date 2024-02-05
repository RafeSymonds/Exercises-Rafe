# Exercises
This is a repository for programing exercises in C++ and Python to give students practice in developing code.

# How the Exercises Work
* There are multiple exercises for both C++ and Python that can be completed one by one. Each exercise gets harder and bulids on the last. 

* Code can be tested by pushing to GitHub and reading the output of the GitHub actions. Code can also be tested locally by following the commands in each exercise.

* **If you plan on testing using GitHub**, we highly recommend the GitHub Actions extension for VSCode because it allows you to easily see your scores for each test in VSCode. To see specific error messages look at GitHub.


# Setup Guide
1. First you will need to fork the repository on GitHub (just click Fork in the upper right and follow the steps)
2. Once you have your own repository, you need to clone it to your local machine. Use "git clone [your SSH clone link]"
3. Now you are ready to setup C++ and Python

There are exercises for both C++ and Python.

## Using the g++ comiplier for C++
1. To locally compile and run the C++ code you will need the g++ compiler
2. To install g++ use "**sudo apt-get install g++**"
3. C++ code should be written in **.cpp** files
4. Each exercise has specific instructions to compile and run

## Using Pytest for Python
1. Tests are written using Pytest
2. To install Pytest use “**python3 -m pip install pytest**”
3. Python code should be written in **.py** files
4. Each exercise has specific instructions to compile and run
5. To run **every test** for **every exercise** run "python3 -m pytest"

# Testing Guide
1. Fork the GitHub to your own repository
2. Clone your new GitHub repository to your local machine by using “git clone”
3. Complete an exercise
4. Once ready to check an exercise either
    1. Push to GitHub
    2. Locally check Python
        1. Run “python3 -m pip install pytest” to install pytest 
        2. Run “python3 -m pytest” to test the python exercises
    3. Locally check C++
        1. Run “make” to compile all exercises (g++ compiler)
        2. Run exe file with input redirection 
        3. Example: ./ex01a.exe < ex01.input.txt
