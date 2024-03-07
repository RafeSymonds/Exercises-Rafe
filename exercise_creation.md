# Exercise Creation Guide
In order to create an exercise there are 4 major parts.

## Instruction Creation
Create a new folder in either the C++ or Python exercise folder.   
Create an instruction file called `ex??.instructions.md`  
Create a C++ or Python file called `ex??.cpp` or `ex??.py` and fill in any needed starter code.

## Test Case Creation
Create a new folder `ex??` in either the C++ or Python testing folder.

### C++ Test Cases
C++ testing utilizes file redirection for input and output. Therefore, correct output files should be prepared in advance. C++ exercises execute via a main function, processing data derived from the input files.

### Python Test Cases
Python tests are established using the PyTest framework. The verification process involves ensuring the output from specific functions is accurate through the use of `assert` commands.

### GitHub Workflow File
To set up the automated grading on GitHub, duplicate the preceding auto-grader configuration and replace the exercise identifiers with those relevant to the new exercise. It’s advisable to retain similarity in file naming to the ones before, enabling straightforward updates by just altering the exercise name. Should the C++ exercises require a varying number of test cases, additional run instructions can be scripted.