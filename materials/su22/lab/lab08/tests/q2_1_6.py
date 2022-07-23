test = {   'name': 'q2_1_6',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib # This imports a hashing library for the autograder. \n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest() \n'
                                               '>>> \n'
                                               '>>> get_hash(set(np.array(framingham_explanations).astype(int)))\n'
                                               "'89f36ca994427830ee4d7f42bc8d88db'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
