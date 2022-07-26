test = {   'name': 'q1_6',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib # This imports a hashing library for the autograder. \n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest() \n'
                                               '>>> \n'
                                               '>>> get_hash(set(np.array(ci_statements).astype(int)))\n'
                                               "'5ad06bc3b78920bcf496ed9a814cf4db'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
