"""Multiplicative Weights Update Algorithm implementation.

This module implements a basic version of the MWU algorithm as
outlined in article-summary.txt. The algorithm maintains weights for a
collection of objects and repeatedly samples an object proportionally
to its weight, observes an event, and updates the weight depending on
the event outcome.

The update rule here is multiplicative: the chosen object's weight is
scaled by (1 + eta * reward), where ``reward`` may be positive or
negative depending on whether the outcome is good or bad. The
parameter ``eta`` should be small (e.g. < 1).
"""

from __future__ import annotations

import random
from typing import Callable, Iterable, List, Sequence, Tuple


RewardFn = Callable[[object], float]
EventFn = Callable[[object], object]


def mwu(
    objects: Sequence[object],
    event: EventFn,
    reward: RewardFn,
    rounds: int,
    eta: float = 0.1,
) -> List[float]:
    """Run the multiplicative weights update algorithm.

    Parameters
    ----------
    objects:
        A sequence of objects to choose from.
    event:
        Function taking an object and returning the outcome for that
        round. The outcome is fed to ``reward``.
    reward:
        Function taking the outcome of ``event`` and returning a reward
        value. Positive values increase the object's weight and negative
        values decrease it.
    rounds:
        Number of iterations to run the algorithm for.
    eta:
        Learning rate controlling how aggressively weights are updated.

    Returns
    -------
    List[float]
        The final list of weights corresponding to ``objects``.
    """

    if rounds <= 0:
        return [1.0 for _ in objects]

    weights = [1.0 for _ in objects]

    for _ in range(rounds):
        total = sum(weights)
        if total == 0:
            break
        probabilities = [w / total for w in weights]
        idx = random.choices(range(len(objects)), weights=probabilities, k=1)[0]
        obj = objects[idx]
        outcome = event(obj)
        r = reward(outcome)
        weights[idx] *= 1.0 + eta * r

    return weights


if __name__ == "__main__":
    # Simple example demonstrating usage. We have three objects and an
    # event that returns the object itself. The reward gives +1 if the
    # chosen object is 0, otherwise -1.
    objs = [0, 1, 2]

    def event(x: int) -> int:
        return x

    def reward_fn(x: int) -> float:
        return 1.0 if x == 0 else -1.0

    final_weights = mwu(objs, event, reward_fn, rounds=10, eta=0.2)
    print(final_weights)
