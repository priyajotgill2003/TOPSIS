# -*- coding: utf-8 -*-
"""102003293

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ui4F76jPGOAum1STvZAHvC2LId1CtyrO
"""

import pandas as pd
import numpy as np
import sys

#Exception handling 
def check_data(input_file, weights, impacts):

    try:                         # Read the input file
        matrix = pd.read_csv(input_file)
    except:
        print("Error: Invalid input file")
        sys.exit(1)

    if matrix.shape[1] < 3:      # at least 3 columns
        print("Error: Invalid input file, must have at least 3 columns")
        sys.exit(1)

    try:                         # Correct number of parameters (weights and impacts)
        weights = np.array(weights, dtype=float)
        impacts = np.array(impacts)
    except Exception as e:
        print(e)
        print("Error: Invalid weights or impacts")
        sys.exit(1)

    try:
        if len(weights) != matrix.shape[1] - 1 or len(impacts) != matrix.shape[1] - 1:
            print("Error: Invalid number of weights or impacts")
            sys.exit(1)
    except:
        print("Error: Invalid weights or impacts, must be separated by commas")
        sys.exit(1)
 
    for col in matrix.columns[1:]:      # from 2nd column to last column only numeric values are valid
        if not pd.api.types.is_numeric_dtype(matrix[col]):
            print("Error: Invalid input file, all columns must be numeric")
            sys.exit(1)

    if not all([impact in ["+", "-"] for impact in impacts]):  # Impacts must be either + or -
        print("Error: Invalid impacts, must be either + or -")
        sys.exit(1)

    if not all([weight > 0 for weight in weights]):   #weights>0 only
        print("Error: Invalid weights, must be positive")
        sys.exit(1)

    return matrix, weights, impacts

#Implemention of the TOPSIS method for multi-criteria decision making.
def topsis(matrix, weights, impact):   

    raw_matrix = matrix.drop(matrix.columns[0], axis=1)
    impact = np.where(impact == "+", 1, -1)

    # Normalize the decision matrix
    raw_matrix = raw_matrix / np.sqrt(np.sum(raw_matrix**2, axis=0))
    weighted_matrix = raw_matrix * weights

    #Calculating ideal best and ideal worst
    ideal_best = np.amax(weighted_matrix * impact, axis=0).abs()
    ideal_worst = np.amin(weighted_matrix * impact, axis=0).abs()

    # Calculating euclidean distance 
    Si_best = np.sqrt(np.sum((weighted_matrix - ideal_best) ** 2, axis=1))
    Si_worst = np.sqrt(np.sum((weighted_matrix - ideal_worst) ** 2, axis=1))

    # Calculate performance score
    performance_score = Si_worst / (Si_best + Si_worst)

    # Calculating rank in the descending order
    rank = performance_score.rank(ascending=False).astype(int)

    # Add performance score and rank to the decision matrix
    matrix["Performance Score"] = performance_score
    matrix["Rank"] = rank

    return matrix

def start():
    
    if len(sys.argv) != 5:
        print("Error: Invalid number of arguments")
        sys.exit(1)

    # Get the input file path, weights and impacts from the command line
    input_file = sys.argv[1]
    weights = sys.argv[2].split(",")
    impacts = sys.argv[3].split(",")
    output_file = sys.argv[4]

    # Exception handling on input data
    matrix, weights, impacts = check_data(input_file, weights, impacts)
    print(matrix)
    # Implementation part
    final = topsis(matrix, weights, impacts)
    print(final)
    # Save the result to the output file
    final.to_csv(output_file, index=False)
    
    print("Output saved to", output_file)
def main():
    start()
