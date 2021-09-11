import time
import random
from toolz.itertoolz import partition_all, concat, partition
import numpy as np
import pandas as pd

chunk_size = 4
# data = []
# for i in range(100):
#     x = []
#     for j in range(random.randrange(10) + 5):
#         x.append(random.randrange(10000))
#     data.append(x)
#
# print(data)

data_array = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

data_np_array = np.array(data_array)

data_dp = pd.DataFrame(data_array)

print(list(partition(2, [1, 2, 3, 4, 5])))

print(list(partition_all(2, data_array)))

print(list(partition_all(2, data_np_array)))

print(list(partition_all(2, data_dp.values.tolist())))

data1 = pd.DataFrame(data=([1, 2, 3, 4], [1, 2, 3, 4]), columns=['a', 'b', 'c', 'd'])

print(data1)

# maps = (print(x) for x in partition_all(chunk_size, data_array))

# print(maps)
#
#
# # break up our data into chunks and create a dynamic list of workers
# maps = (print(x) for x in partition_all(chunk_size, data))
