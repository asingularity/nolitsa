# -*- coding: utf-8 -*-

from __future__ import division

import numpy as np

from nolitsa import surrogates, noise, utils
from numpy.testing import assert_allclose, run_module_suite


def test_ft():
    # Test surrogates.ft()
    # Always test for both odd and even number of points.
    for n in (1021, 1024):
        # NOTE that zero mean series almost always causes an assertion
        # error since the relative tolerance between different "zeros"
        # can be quite large.  This is not a bug!
        x = 1.0 + np.random.random(n)
        y = surrogates.ft(x)

        assert_allclose(utils.spectrum(x)[1], utils.spectrum(y)[1])


def test_aaft():
    # Test surrogates.aaft()
    # Always test for both odd and even number of points.
    for n in (2 ** 16 - 1, 2 ** 16):
        # Correlated Gaussian numbers transformed using f(x) = tanh(x)
        x = noise.sma(np.random.normal(size=n), hwin=5)
        x = np.tanh(x)
        y = surrogates.aaft(x)

        assert_allclose(utils.spectrum(x)[1], utils.spectrum(y)[1], atol=1e-3)


def test_iaaft():
    # Test surrogates.aaft()
    # Always test for both odd and even number of points.
    for n in (2 ** 14, 2 ** 14 + 1):
        # Correlated Gaussian numbers transformed using f(x) = tanh(x)
        x = noise.sma(np.random.normal(size=n), hwin=5)
        x = np.tanh(x)
        y, i, e = surrogates.iaaft(x)

        assert_allclose(utils.spectrum(x)[1], utils.spectrum(y)[1], atol=1e-6)

if __name__ == '__main__':
    run_module_suite()
