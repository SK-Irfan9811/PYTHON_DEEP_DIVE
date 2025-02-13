import importlib.util
import sys

print(importlib.util.find_spec("module"))
sys.path.append('C:/Users/Irfan_Shaik/IRFAN/PYTHON/PYTHON_DEEP_DIVE/deep_dive-1/modules/example2')
print(importlib.util.find_spec("module"))
# print("module_3" in globals())
# import module_3
#
# print("module_3" in globals())
