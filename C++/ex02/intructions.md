## Overview

For this exercise you will create a program that prints out all the numbers between 2 inputs inclusive.

**Some tests will not output anything**

## Input
You will be provided 2 integers through standard input. These integers can be user-inputted or redirected from a file using input redirection.

## Test your code
1. Compile the file with "make ex02" 
2. Run your executable with "./C++/ex02/ex02.exe"
3. Input 2 integers
4. To run a test case use "./C++/ex02/ex02.exe < testingFiles/C++/ex02/ex02.input1.txt"
    1. There are 2 different test cases for this problem 
    2. To run a different test case change what file is redirected
5. To compare your results with the correct results you will **either** need to push to your GitHub repository or run the tests locally
    1. using GitHub
        1. Run **git add .** to prepare **all** changes for commit
        2. Run **git commit -m "commit message"** to make changes permanent in the local repository
        3. Run **git push** to push your changes to your remote repository
        4. Look at results found in
            * the Actions window of GitHub
            * the GitHub Actions extension window for VSCode

    1. run each input redirection
        1. run "./C++/ex02/ex02.exe < testingFiles/C++/ex02/ex02.input1.txt > ./C++/ex02/ex02.output1.txt" to run the test and save its output to a .txt file
        2. compare results of the test to the actual resutls with "diff ./C++/ex02/ex02.output1.txt testingFiles/C++/ex02/CorrectOutput/ex02.correct.output1.txt"
            * **if nothing is printed, it means your output is the same**
        3. repeat steps 1 and 2 with the different input files. Make sure to change the name of the files in the input and output redirection