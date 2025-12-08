#!/usr/bin/env python3
"""
Combine all Organization YAML frontmatter files into a single YAML file.

This script is a thin wrapper around organizations.py.
For the full implementation, see organizations.combine_organizations().
"""

from organizations import main_combine

if __name__ == "__main__":
    main_combine()
