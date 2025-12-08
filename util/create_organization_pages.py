#!/usr/bin/env python3
"""
Create Organization pages for all Organizations used as Contacts in Resource pages.

This script is a thin wrapper around organizations.py.
For the full implementation, see organizations.process_resource_organizations().
"""

from organizations import main_create

if __name__ == "__main__":
    main_create()
