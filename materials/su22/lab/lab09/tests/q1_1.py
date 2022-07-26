test = {   'name': 'q1_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib # This imports a hashing library for the autograder. \n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest() \n'
                                               '>>> \n'
                                               '>>> get_hash(set(np.array(nhs_true_statements).astype(int)))\n'
                                               "'8dd6d5594e1f0c323aff853c6de15c73'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
