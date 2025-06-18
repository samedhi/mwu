"""Multiplicative Weights Update Algorithm implementation.

This module implements a minimal version of the multiplicative weights
update (MWU) algorithm.  The algorithm maintains weights for a
collection of objects, randomly chooses one proportionally to its
weight, observes an event, and then updates the chosen object's weight
based on the outcome.

Unlike a full MWU implementation, this module provides a single round
update that can easily be called repeatedly by the user.  It takes a
dictionary mapping objects to their current weights and returns a new
dictionary with the updated weights.
"""

from __future__ import annotations

import random
from typing import Callable, Dict, Mapping


RewardFn = Callable[[object], float]
EventFn = Callable[[object], object]


def mwu(
    event: EventFn,
    reward: RewardFn,
    objects: Mapping[object, float],
) -> Dict[object, float]:
    """Run a single round of the multiplicative weights update algorithm.

    Parameters
    ----------
    event:
        Function taking an object and returning the outcome for that
        round. The outcome is fed to ``reward``.
    reward:
        Function taking the outcome of ``event`` and returning a reward
        value. Positive values increase the object's weight and negative
        values decrease it.  The reward should be scaled as desired
        since no learning rate parameter is used.
    objects:
        Mapping from objects to their current weights.

    Returns
    -------
    Dict[object, float]
        A new mapping of objects to their updated weights after one
        multiplicative update.
    """

    if not objects:
        return {}

    total = sum(objects.values())
    if total == 0:
        return dict(objects)

    choices, weights_list = zip(*objects.items())
    chosen = random.choices(choices, weights=weights_list, k=1)[0]
    outcome = event(chosen)
    r = reward(outcome)

    new_weights = dict(objects)
    new_weights[chosen] *= 1.0 + r

    return new_weights


