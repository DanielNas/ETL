import logging
import os
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root = file.parents[1]
sys.path.append(str(root))