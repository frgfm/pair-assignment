# Pair assignment
This repository was made for pair assignments in constrained environments. 
Input is mostly considered as a symmetric cost matrix of shape N x N where N is the number of agents.



## Installation

This module was developed using only Python and numpy

```bash
git clone https://github.com/frgfm/pair-assignment.git
cd pair-assignment
pip install requirements.txt
```



## Usage

If you prefer running the simulation directly without entering a shell:

```bash
python main.py
```

If you favor using objects in Python, you can use the classes and functions from the game.py file

```python
# Generate random cost matrix
nb_agents = 13
cost_matrix = np.random.rand(nb_agents, nb_agents)
for row_idx in range(cost_matrix.shape[0]):
    for col_idx in range(row_idx, cost_matrix.shape[1]):
        if row_idx == col_idx:
            cost_matrix[row_idx, col_idx] = 0
        else:
            cost_matrix[col_idx, row_idx] = cost_matrix[row_idx, col_idx]

# Brute Force
start_time = datetime.now()
bf_assignment, bf_score = bf_assign(cost_matrix)
print('Brute force score: %s (computed in %s)' % (np.sum([cost_matrix[couple] for couple in bf_assignment]), datetime.now() - start_time))

# Approx method
start_time = datetime.now()
ap_assignment = approx_assign(cost_matrix)
print('Approx method score: %s (computed in %s)' % (np.sum([cost_matrix[couple] for couple in ap_assignment]), datetime.now() - start_time))

```

Either way, it should simulate a game with an output similar to:
```bash
Brute force score: 1.2715180930424301 (computed in 0:00:01.583963)
Approx method score: 1.9992776643053922 (computed in 0:00:00)
```


## TODO
- [x] Build a baseline exact assignment method (brute force most likely)
- [x] Draft a first approximation method to boost computation speed
- [ ] Explore other solutions

