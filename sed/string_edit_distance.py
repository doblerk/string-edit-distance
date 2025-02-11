import numpy as np
from typing import Tuple


class StringEditDistance:

    def __init__(self, 
                 x: str, 
                 y: str) -> None:
        self.x = x
        self.y = y

    def cost_del(self, letter: str) -> int:
        return 1

    def cost_ins(self, letter: str) -> int:
        return 1
    
    def cost_sub(self,
                 letter1: str,
                 letter2: str) -> int:
        c_sub = 1 if letter1.lower() == letter2.lower() else 2
        return (letter1 != letter2) * c_sub
    
    def init_cost_matrix(self) -> np.ndarray:
        n, m = len(self.x), len(self.y)
        D = np.zeros((n + 1, m + 1))

        # Assign cost for deleted elements
        for i in range(1, n + 1):
            D[i, 0] = D[i - 1, 0] + self.cost_del(self.x[i - 1])

        # Assign cost for inserted elements
        for j in range(1, m + 1):
            D[0, j] = D[0, j - 1] + self.cost_ins(self.y[j - 1])
        
        return D
    
    def init_pointer_matrix(self) -> np.ndarray:
        n, m = len(self.x), len(self.y)
        P = np.full((n + 1, m + 1), "", dtype=str)

        # Assign cost for deleted elements
        for i in range(1, n + 1):
            P[i, 0] = "↑"

        # Assign cost for inserted elements
        for j in range(1, m + 1):
            P[0, j] = "←"
        
        return P

    def calc_sed(self,
                 D: np.ndarray,
                 P: np.ndarray) -> None:
        n, m = len(self.x), len(self.y)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                
                m_1 = D[i - 1, j - 1] + self.cost_sub(self.x[i - 1], self.y[j - 1])
                m_2 = D[i - 1, j] + self.cost_del(self.x[i - 1])
                m_3 = D[i, j - 1] + self.cost_ins(self.y[j - 1])

                # Select the operation that minimizes the partial edit distance
                D[i, j] = min([m_1, m_2, m_3])

                # Update pointers
                if D[i, j] == m_1:
                    P[i, j] = "↖"
                elif D[i, j] == m_2:
                    P[i, j] = "↑"
                elif D[i, j] == m_3:
                    P[i, j] = "←"