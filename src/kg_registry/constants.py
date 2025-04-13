"""Constants for the KG-Registry."""

import pathlib

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.parent.resolve()
RESOURCE_DIRECTORY = ROOT.joinpath("resource")
DATA_DIRECTORY = ROOT.joinpath("_data")
