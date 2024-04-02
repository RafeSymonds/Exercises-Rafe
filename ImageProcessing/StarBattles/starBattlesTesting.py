import starBattles
import numpy as np


test1Regions = np.array([
    [1, 1, 1, 1, 1, 6, 6, 8, 8, 8],
    [1, 1, 1, 1, 1, 6, 8, 8, 8, 8],
    [1, 1, 1, 1, 6, 6, 6, 8, 8, 30],
    [31, 31, 1, 1, 6, 6, 6, 6, 30, 30],
    [31, 31, 1, 1, 1, 1, 6, 48, 48, 30],
    [31, 31, 31, 1, 1, 1, 48, 48, 48, 30],
    [31, 62, 31, 64, 64, 66, 66, 48, 48, 48],
    [31, 62, 64, 64, 64, 64, 66, 66, 66, 48],
    [62, 62, 62, 84, 84, 64, 64, 64, 64, 64],
    [62, 62, 62, 84, 64, 64, 64, 64, 64, 64]])

test1CorrectSolution = np.array([
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]])

test1IncorrectSolution = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]])

test2Regions = np.array([
    [ 1,  1,  1,  1,  1,  1,  7,  7,  7, 10],
    [ 1,  1,  1,  1,  1,  7,  7,  7,  7, 10],
    [ 1,  1,  1,  1,  1,  1,  1, 28, 10, 10],
    [ 1,  1, 33,  1,  1,  1, 28, 28, 10, 10],
    [ 1,  1, 33, 44, 44, 44, 28, 28, 28, 28],
    [ 1, 33, 33, 44, 44, 44, 28, 58, 58, 58],
    [ 1, 62, 62, 44, 44, 44, 44, 58, 58, 58],
    [62, 62, 62, 62, 44, 76, 76, 76, 76, 76],
    [84, 84, 62, 84, 84, 76, 76, 76, 76, 76],
    [84, 84, 84, 84, 84, 76, 76, 76, 76, 76]])

test2CorrectSolution = np.array([
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]])

test2IncorrectSolution = np.array([
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1]])

test3Regions = np.array([
    [1, 1, 1, 1, 5, 5, 5, 5, 9, 9],
    [1, 1, 1, 1, 15, 5, 5, 9, 9, 9],
    [1, 1, 1, 15, 15, 15, 15, 9, 9, 9],
    [1, 1, 1, 15, 15, 15, 15, 9, 9, 9],
    [1, 42, 42, 15, 15, 15, 15, 9, 9, 50],
    [1, 42, 42, 42, 55, 15, 50, 50, 50, 50],
    [61, 61, 42, 55, 55, 55, 50, 50, 50, 50],
    [61, 61, 42, 42, 42, 79, 79, 50, 79, 79],
    [61, 61, 83, 83, 42, 79, 79, 79, 79, 79],
    [61, 61, 83, 83, 42, 42, 42, 42, 42, 42]])

test3CorrectSolution = np.array([
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]])

test3IncorrectSolution = np.array([
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]])

test4Regions = np.array([
    [ 1,  1,  1,  1,  1,  1,  1,  8,  8,  8],
    [ 1,  1,  1, 14,  1,  1,  1,  8,  8,  8],
    [ 1,  1, 14, 14, 14,  1,  1,  8,  8, 30],
    [31, 32, 32, 32, 32,  1,  8,  8,  8, 30],
    [31, 31, 31, 31, 31, 31, 31,  8,  8, 30],
    [31, 31, 31, 31,  8,  8,  8,  8,  8, 30],
    [31, 31, 31, 31,  8,  8, 67, 67,  8,  8],
    [31, 31, 31, 74,  8,  8, 67, 67, 79, 79],
    [74, 74, 74, 74, 74, 86, 67, 67, 79, 79],
    [74, 74, 74, 74, 86, 86, 86, 86, 86, 86]])

test4CorrectSolution = np.array([
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]])

test4IncorrectSolution = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]])

def test_validate():
    assert starBattles.validateSolution(test1Regions, test1CorrectSolution) == True
    assert starBattles.validateSolution(test1Regions, test1IncorrectSolution) == False
    assert starBattles.validateSolution(test2Regions, test2CorrectSolution) == True
    assert starBattles.validateSolution(test2Regions, test2IncorrectSolution) == False
    assert starBattles.validateSolution(test3Regions, test3CorrectSolution) == True
    assert starBattles.validateSolution(test3Regions, test3IncorrectSolution) == False
    assert starBattles.validateSolution(test4Regions, test4CorrectSolution) == True
    assert starBattles.validateSolution(test4Regions, test4IncorrectSolution) == False

def test_solve():
    test1Solution = starBattles.generateSolution(test1Regions)
    assert starBattles.validateSolution(test1Regions, test1Solution) == True

    test2Solution = starBattles.generateSolution(test2Regions)
    assert starBattles.validateSolution(test2Regions, test2Solution) == True 

    test3Solution = starBattles.generateSolution(test3Regions)
    assert starBattles.validateSolution(test3Regions, test3Solution) == True 

    test4Solution = starBattles.generateSolution(test4Regions)
    assert starBattles.validateSolution(test4Regions, test4Solution) == True 


def test_generate_images():
    test1Img = starBattles.returnImage('ImageProcessing/StarBattles/TestCases/test1_input.png')
    test1GeneratedRegions = starBattles.generateRegionsFromImage(test1Img)
    assert starBattles.validateSolution(test1GeneratedRegions, test1CorrectSolution)

    test2Img = starBattles.returnImage('ImageProcessing/StarBattles/TestCases/test2_input.png')
    test2GeneratedRegions = starBattles.generateRegionsFromImage(test2Img)
    assert starBattles.validateSolution(test2GeneratedRegions, test2CorrectSolution)

    test3Img = starBattles.returnImage('ImageProcessing/StarBattles/TestCases/test3_input.png')
    test3GeneratedRegions = starBattles.generateRegionsFromImage(test3Img)
    assert starBattles.validateSolution(test3GeneratedRegions, test3CorrectSolution)

    test4Img = starBattles.returnImage('ImageProcessing/StarBattles/TestCases/test4_input.png')
    test4GeneratedRegions = starBattles.generateRegionsFromImage(test4Img)
    assert starBattles.validateSolution(test4GeneratedRegions, test4CorrectSolution)


