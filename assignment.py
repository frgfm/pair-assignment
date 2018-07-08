#!/usr/bin/env python

'''
These functions were developped to provide optimisation solutions for assignment problems

'''

__author__ = 'François-Guillaume Fernandez'
__license__ = 'MIT License'
__version__ = '0.1'
__maintainer__ = 'François-Guillaume Fernandez'
__status__ = 'Development'

import numpy as np


def all_pairs(lst):
    if len(lst) < 2:
        yield lst
        return
    a = lst[0]
    for i in range(1, len(lst)):
        pair = (a, lst[i])
        for rest in all_pairs(lst[1:i] + lst[i + 1:]):
            yield [pair] + rest


def brute_force_even(cost_matrix, idx_list=None):

    best_score = None
    best_assignment = []
    if idx_list is None:
        idx_list = [idx for idx in range(cost_matrix.shape[0])]

    for assignment in all_pairs(idx_list):

        # Build score
        assign_mat = np.zeros(cost_matrix.shape)
        for pair in assignment:
            if not isinstance(pair, tuple):
                continue
            assign_mat[pair[0], pair[1]] = 1
            assign_mat[pair[1], pair[0]] = 1
        score = np.sum(np.multiply(assign_mat, cost_matrix))

        # Check if we got a better score
        if best_score is None or score < best_score:
            best_assignment = assignment
            best_score = score

    return best_assignment, best_score


def bf_assign(cost_matrix):

    best_score = None
    best_assignment = []

    if cost_matrix.shape[0] % 2 == 1:
        odd_cnt = 0
        best_score = None
        best_assignment = []
        for removed in range(cost_matrix.shape[0]):
            idx_list = [idx for idx in range(cost_matrix.shape[0]) if idx != removed]
            odd_cnt = odd_cnt + 1
            tmp_assign, tmp_score = brute_force_even(cost_matrix, idx_list)
            if best_score is None or tmp_score < best_score:
                best_assignment = tmp_assign
                best_score = tmp_score
        return best_assignment, best_score
    else:
        return brute_force_even(cost_matrix)


def compute_approx_mat(cost_matrix, method='median'):

    """Display a progress bar.
    Parameters
    ----------
    count : int
        Number of iterations already performed.
    total : int
        Total number of iterations.
    status : str
        Status information you want to print out.
    """

    if method == 'median':
        approx_mat = np.median(cost_matrix, axis=1)

    elif method == 'mean':
        approx_mat = np.mean(cost_matrix, axis=1)

    else:
        raise ValueError('Approximation method argument is expected to be in ("median", "mean")')

    return approx_mat


def compute_rank_score(val, rank, alpha=2):

    return rank * val ** alpha


def approx_assign(cost_matrix, method='median'):

    approx_mat = compute_approx_mat(cost_matrix, method)
    remaining = np.argsort(-approx_mat)
    assignments, full_assigned = [], []
    while len(remaining) > 1:

        a1 = remaining[0]
        # Compute optimum with agent 0
        sorted_costs = np.argsort(cost_matrix[a1])
        for agent_idx in sorted_costs:
            if agent_idx == a1 or agent_idx in full_assigned:
                continue
            a2 = agent_idx
            break

        # Update remaining & full_assigned
        assignments.append((a1, a2))
        full_assigned.extend([a1, a2])
        remaining = [idx for idx in remaining if idx not in full_assigned]

    return assignments
