# -*- coding: utf-8 -*-
"""My PDS Module."""
import importlib


__version__ = importlib.resources.files(__name__).joinpath('VERSION.txt').read_text().strip()


# For future consideration:
#
# - Other metadata (__docformat__, __copyright__, etc.)
# - N̶a̶m̶e̶s̶p̶a̶c̶e̶ ̶p̶a̶c̶k̶a̶g̶e̶s̶ we got this
