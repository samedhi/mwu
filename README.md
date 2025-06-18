# mwu
A pure Python implementation of the Multiplicative Weights Update Algorithm.

The core implementation lives in `mwu.py` and exposes a single function
`mwu` which performs one multiplicative weights update on a mapping of
objects to weights.

```python
from mwu import mwu

# Define event and reward functions
...
weights = {"a": 1.0, "b": 1.0}
weights = mwu(event, reward, weights)
```
