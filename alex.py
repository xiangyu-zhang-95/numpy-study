import numpy as np

print(np.__file__)

# __git_revision__ not in __all__
print(np.__git_revision__)

# __version__ is in __all__
print(np.__version__)

print("np.__all__:")
print(np.__all__)

print("np.core.__all__:")
print(np.core.__all__)

print("np._mat.__all__:")
print(np._mat.__all__)

print("np.lib.__all__:")
print(np.lib.__all__)

import sys
print("sys.version_info")
print(sys.version_info[:2])

np.testing
try:
    np.x
except Exception as e:
    print(e)

my_dir = dir(np)
print("dir(np): ")
print(my_dir)

for name in np.__all__:
    if name not in my_dir:
        print(f"{name} in np.__all__ but not in dir(np)")

