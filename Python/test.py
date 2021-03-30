import pandas as pd
import collections
a = {"a":[1,2,3], "b":[11,22,33]}
a = pd.DataFrame(a)
for row in a.itertuples():
    print(pd.DataFrame(row))
    exit(0)