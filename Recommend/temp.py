import pandas as pd
import numpy as np
import random
data = pd.read_csv(r'E:\DoAnPTIT\Data\final_rating_not_spare.csv')
user_id =  np.unique(data['customer_id'])
print(random.choice(user_id))