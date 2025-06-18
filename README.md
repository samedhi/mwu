# mwu
A pure Python implementation of the Multiplicative Weights Update Algorithm.

The core implementation lives in `mwu.py` and exposes a single function
`mwu` which runs the algorithm for a fixed number of rounds.

```python
from mwu import mwu

# Define event and reward functions
...
final_weights = mwu(objects, event, reward, rounds=100)
```
