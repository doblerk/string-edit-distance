# String Edit Distance

This repository contains an implementation of the string edit distance algorithm to compute the minimum sequence of cost edit operations between two strings.

## Installation

#### Prerequisites
- Python >= 3.10

#### Install
```bash
# Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install the Python package
python3 -m pip install -e .
```

## Example usage
```python
from sed.string_edit_distance import StringEditDistance


string1 = 'ABABBB'
string2 = 'BABAAA'

sed = StringEditDistance(string1, string2)

D = sed.init_cost_matrix()
P = sed.init_pointer_matrix()

sed.calc_sed(D, P)

print('Cost Matrix D: ')
print(D)
print('\nPointer Matrix P: ')
for row in P:
    print(" ".join(row))
```

#### Cost Matrix D

According to the cost matrix $D$, the string edit distance is $6$ (lower right value).

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | 2 | 1 | 2 | 3 | 4 | 5 |
| 2 | 1 | 2 | 1 | 2 | 3 | 4 |
| 3 | 2 | 1 | 2 | 1 | 2 | 3 |
| 4 | 3 | 2 | 1 | 2 | 3 | 4 |
| 5 | 4 | 3 | 2 | 3 | 4 | 5 |
| 6 | 5 | 4 | 3 | 4 | 5 | 6 |

#### Pointer Matrix P

According to the pointer matrix $P$, these pointers can be used to reconstruct the edit operations by following the trajectory from the lower right position.

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   | ← | ← | ← | ← | ← | ← |
| ↑ | ↖ | ↖ | ← | ↖ | ↖ | ↖ |
| ↑ | ↖ | ↑ | ↖ | ← | ← | ← |
| ↑ | ↑ | ↖ | ↑ | ↖ | ↖ | ↖ |
| ↑ | ↖ | ↑ | ↖ | ↑ | ↖ | ↖ |
| ↑ | ↖ | ↑ | ↖ | ↖ | ↖ | ↖ |
| ↑ | ↖ | ↑ | ↖ | ↖ | ↖ | ↖ |

## Further information

The current implementation is restricted to lowercase and uppercase Roman letters, represented by the set $\{a, b, c, \ldots, z, A, B, C, \ldots, Z\}$, with cost of edit operations defined as:

$$
c(l \xrightarrow{} \epsilon) = c(\epsilon \xrightarrow{} l') = 1
$$
$$
c(l \xrightarrow{} l') = \begin{cases}
    0 \ \text{if 'A'=='A' or 'v'=='v'} \\
    1 \ \text{if 'a'=='A' or 'V'=='v'} \\
    2 \ \text{if 'a'=='b' or 'v'=='B'}
    \end{cases}
$$