# coding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals

from .smbfs import SMBFS

__all__ = ['SMBFS']

__license__ = "MIT"
__copyright__ = "Copyright (c) 2017 Martin Larralde"
__author__ = "Martin Larralde <martin.larralde@ens-cachan.fr>"
__version__ = 'dev'

# Dynamically get the version of the installed module
try:
    import pkg_resources
    __version__ = pkg_resources.get_distribution(__name__).version
except Exception:
    pkg_resources = None
finally:
    del pkg_resources