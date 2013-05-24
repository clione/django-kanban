# Copyright 2013 Clione Software
# Licensed under MIT license. See LICENSE for details.

import defaults

DEBUG = True
TEMPLATE_DEBUG = DEBUG

__version__ = defaults.__version__

if DEBUG:
    from development import *
else:
    from production import *