#!/usr/bin/env python

'''
These functions were developped to provide optimisation solutions for assignment problems
'''

__author__ = 'François-Guillaume Fernandez'
__license__ = 'MIT License'
__version__ = '0.1'
__maintainer__ = 'François-Guillaume Fernandez'
__status__ = 'Development'

from assignment import bf_assign, approx_assign
import numpy as np
from datetime import datetime


def main():
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



if __name__ == "__main__":
    main()
