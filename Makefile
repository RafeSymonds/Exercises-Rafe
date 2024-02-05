# Compiler
CXX := g++
# Compiler flags
CXXFLAGS := -std=c++11 -Wall -Wextra -pedantic

# List of exercises (source files)
EXERCISES := $(shell find . -name '*.cpp')

# Map source files to executable files
EXECUTABLES := $(EXERCISES:%.cpp=%.exe)

# Default target
all: $(EXECUTABLES)

# Rule to create executables
%.exe: %.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

# Rule to create specific exercise
ex%: 
	$(CXX) $(CXXFLAGS) $(wildcard C++/ex$*/ex$*.cpp) -o $(patsubst %.cpp,%.exe,$(wildcard C++/ex$*/ex$*.cpp))


# Clean rule
clean:
	rm -f $(EXECUTABLES)

.PHONY: all clean
