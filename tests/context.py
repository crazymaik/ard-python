# Header that must be included in all test modules.
import os
import sys

# Prepend the parent directory of this module to the path array used for
# module lookup. This way the tests will use the source project instead
# of the installed project/package.
module_path = os.path.abspath(__file__)
parent_path = os.path.dirname(os.path.dirname(module_path))
sys.path.insert(0, parent_path)
