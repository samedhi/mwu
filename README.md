# mwu
A pure Python implementation of the Multiplicative Weights Update Algorithm.

The core implementation lives in `mwu.py` and exposes a single function
`mwu` which performs one multiplicative weights update on a mapping of
objects to weights.

## Example

```python
import random
from mwu import mwu

# The outcome of a chosen object is just the object itself
def outcome(obj):
    return obj

# Reward the chosen object and penalize the rest
def reward(obj, result):
    return 0.1 if obj == result else -0.1

weights = {"a": 1.0, "b": 1.0}

random.seed(0)
new_weights = mwu(outcome, reward, weights)
print(new_weights)
```

Running this example prints:

```
{'a': 0.9, 'b': 1.1}
```

Here object `'b'` was chosen so it gained weight while `'a'` was penalized.
