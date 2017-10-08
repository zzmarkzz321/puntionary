# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

import os
from client import client


#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
	client.run(host='0.0.0.0', port=3000)