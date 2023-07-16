from typing import Tuple

import csv
import numpy as np
import matplotlib.pyplot as plt


class StringEditDistance:

    def __init__(self, 
                 x: str, 
                 y: str, 
                 cost_indels: int,  
                 cost_synonymous_subst: int,
                 cost_nonsynonymous_subst: int) -> None:
        
        self.x = x
        self.y = y
        self.cost_indels = cost_indels
        self.cost_synonymous_subst = cost_synonymous_subst
        self.cost_nonsynonymous_subst = cost_nonsynonymous_subst

    def get_cost(self, x: chr, y: chr) -> int:
        """
        Computes the cost between two characters.
            It checks whether both characters are of the same case.
            If True, then it returns 0 if they are identical, otherwise it returns a given cost.
            If False, then it converts them into the same case and checks whether they are identical.
            non-synonymous substitution: completely different characters.
            synonymous substitution: same characters, but different case.
        """
        if (x.islower() and y.islower()) or (x.isupper() and y.isupper()):
            if x != y:
                return self.cost_nonsynonymous_subst
            else:
                return 0
        else:
            if x.lower() != y.lower():
                return self.cost_nonsynonymous_subst
            else:
                return self.cost_synonymous_subst

    def get_cost_matrix(self, x: str, y: str) -> np.ndarray:
        """
        Computes the cost matrix. 
        """
        x_size = len(x)
        y_size = len(y)
        D = np.zeros(shape=(x_size + 1, y_size + 1), dtype=np.uint8)
        for i in range(1, x_size + 1):
            D[i, 0] = D[i - 1, 0] + self.cost_indels
        for j in range(1, y_size + 1):
            D[0, j] = D[0, j - 1] + self.cost_indels
        return D

    def get_pointer_matrix(self, x: str, y: str) -> np.ndarray:
        """
        Creates pointer matrix to keep track of the best sequence
        """
        x_size = len(x)
        y_size = len(y)
        P = np.zeros(shape=(x_size + 1, y_size + 1), dtype=(int, 2))
        return P

    def fill_cost_table(self, x: str, y: str, D: np.ndarray, P: np.ndarray = None) -> Tuple[np.ndarray, int, np.ndarray]:
        """
        Computes SED using a dynamic programming approach.
        """

        for i in range(1, D.shape[0]):

            for j in range(1, D.shape[1]):
                
                # top left
                m1 = D[i - 1, j - 1] + self.get_cost(x[i-1], y[j-1])
                # top
                m2 = D[i - 1, j] + self.cost_indels
                # left
                m3 = D[i, j - 1] + self.cost_indels

                D[i, j] = min(m1, m2, m3)

                # fill pointer matrix -> store coordinates to which cell an entry is pointing to (3D array)
                if m1 == D[i, j]:
                    P[i, j] = (i-1, j-1)
                else:
                   if m2 == D[i, j]:
                       P[i, j] = (i-1, j)
                   else:
                       P[i, j] = i, j-1
        
        return D, D[D.shape[0]-1, D.shape[1]-1], P

def main():
    # Load list of words/texts to compare from 'data/texts.txt'
    with open('data/texts.txt', 'r') as f:
        strings = [string.strip().split(', ') for string in f.readlines()]

    # Compute the string edit distance between all pairs of loaded words
    res = {f'pair_{i}':0 for i in range(1, len(strings)+1)}
    for i in range(len(strings)):
        x, y = strings[i][0], strings[i][1]
        sed = StringEditDistance(x, y, 1, 1, 2)
        D = sed.get_cost_matrix(x, y)
        P = sed.get_pointer_matrix(x, y)
        cost_matrix, cost, P = sed.fill_cost_table(x, y, D, P)
        res[f'pair_{i+1}'] = cost 
    
    print(res)

if __name__ == '__main__':
    main()