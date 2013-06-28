.. pypps_reader documentation master file, created by
   sphinx-quickstart on Fri Jun 28 15:23:28 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pypps_reader's documentation!
========================================

pypps_reader is a small application for the reading of NWCSAF-PPS generated
data, both final products and those files that PPS spits out on it's way during
processing.

The source code of the module can be found on the github_ page.

.. _github: http://github.com/adybbroe/pypps_reader


Contents:

.. toctree::
   :maxdepth: 2


Installation
------------

You can download the source code from github_::

  $> git clone git://github.com/adybbroe/pypps_reader.git

and then run::

  $> python setup.py install

or, if you want to hack the package::

  $> python setup.py develop


Usage
-----

A simple usage:

 >>> from pypps_reader import NwcSafPpsData
 >>> ctype = NwcSafPpsData("/local_disk/data/pps/export/noaa18_20120803_1144_37124_satproj_00000_05500_cloudtype.h5")
 >>> avhrr = NwcSafPpsData("/local_disk/data/pps/import/PPS_data/remapped/noaa18_20120803_1144_37124_satproj_00000_05500_avhrr.h5")
 >>> print ctype.cloudtype.data
 [[ 1  1  1 ...,  1  6  6]
  [ 1  1  1 ...,  1  6  6]
  [ 1  1  1 ...,  1  6  6]
  ...,
  [ 0  0  0 ...,  0  0  0]
  [10 10 10 ..., 14 14 14]
  [10 10 10 ..., 14 14 14]]

 >>> print avhrr.area.lons
 [[  56.50100268   56.44800268   56.39600268 ...,   24.59000117
     24.54600117   24.50100116]
  [  56.50000268   56.44800268   56.39500268 ...,   24.58600117
     24.54100117   24.49600116]
  [  56.49900268   56.44700268   56.39400268 ...,   24.58100117
     24.53700117   24.49200116]
  ...,
  [ 129.35300614  129.32700614  129.30000614 ...,  -47.08100224
    -47.08200224  -47.08300224]
  [ 129.46600615  129.44000615  129.41500615 ...,  -47.10700224
    -47.10800224  -47.10900224]
  [ 129.57800615  129.55400615  129.52900615 ...,  -47.13200224
    -47.13300224  -47.13500224]] 



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

