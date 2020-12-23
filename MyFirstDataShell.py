from BobRoss import BobRoss
from BillWatterson import BillWatterson
import pandas as pd

inventory_management = pd.read_csv('inventory.csv')

class MyDataShell:
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.data_as_csv = pd.read_csv('inventory.csv')

    def get_stats(self):
        return self.data_as_csv.describe()

inventory_management_stats = MyDataShell('inventory.csv')

print(inventory_management)
print(inventory_management_stats.get_stats())

BillWatterson
BobRoss