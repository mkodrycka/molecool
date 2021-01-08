"""
molecool
A Python package for analyzing and visualizing xyz files.
"""

# Add imports here
from .functions import *
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram
from .center_of_mass import calculate_molecular_mass, calculate_center_of_mass 

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
