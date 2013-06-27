#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Adam.Dybbroe

# Author(s):

#   Adam.Dybbroe <a000680@c14526.ad.smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Example showing how to read some PPS data
"""

import logging

from pypps_reader import NwcSafPpsData

#: Default time format
_DEFAULT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

#: Default log format
_DEFAULT_LOG_FORMAT = '[%(levelname)s: %(asctime)s : %(name)s] %(message)s'

if __name__ == "__main__":

    from logging import handlers
    import sys

    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt=_DEFAULT_LOG_FORMAT,
                                  datefmt=_DEFAULT_TIME_FORMAT)
    handler.setFormatter(formatter)
    logging.getLogger('').addHandler(handler)
    logging.getLogger('').setLevel(logging.INFO)

    LOG = logging.getLogger('example')

    SUNSATANGLES = "/local_disk/data/pps/import/ANC_data/remapped/noaa18_20120803_1144_37124_satproj_00000_05500_sunsatangles.h5"
    AVHRR = "/local_disk/data/pps/import/PPS_data/remapped/noaa18_20120803_1144_37124_satproj_00000_05500_avhrr.h5"
    EMISSIVITY = "/local_disk/data/pps/import/EMISS_data/remapped/noaa18_20120803_1144_37124_satproj_00000_05500_emissivity.h5"
    CLOUDTYPE = "/local_disk/data/pps/export/noaa18_20120803_1144_37124_satproj_00000_05500_cloudtype.h5"

    ctype = NwcSafPpsData(CLOUDTYPE)
    #avhrr = NwcSafPpsData(AVHRR)
    #emiss = NwcSafPpsData(EMISSIVITY)
    
