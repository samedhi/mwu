import random
from mwu import mwu


def outcome(obj):
    return obj


def reward(obj, result):
    return 0.1 if obj == result else -0.1


def test_basic_update_seed0():
    random.seed(0)
    weights = {"a": 1.0, "b": 1.0}
    assert mwu(outcome, reward, weights) == {"a": 0.9, "b": 1.1}


def test_empty_mapping():
    assert mwu(outcome, reward, {}) == {}


def test_zero_weights():
    weights = {"a": 0.0, "b": 0.0}
    assert mwu(outcome, reward, weights) == weights
