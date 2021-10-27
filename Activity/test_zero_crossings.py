import pytest

import numpy as np

from Activity.test2 import zero_crossings

def test_zero_crossings():
    
    assert len(zero_crossings(np.zeros(10))) is 1, \
        "Zero array does not return expected"
    non_zero_result = zero_crossings(np.array([-4, 0, 4, -1]))
    assert len(non_zero_result) is 1
    # Check index of crossing is correct
    assert non_zero_result[0][0] == 2