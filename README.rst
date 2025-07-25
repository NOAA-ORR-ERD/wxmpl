
Fork of Ken McIvors wxMPL project
=================================

Formerly at: http://agni.phys.iit.edu/~kmcivor/wxmpl/

Ken has not maintained this for a while, and is no longer at IIT.

**NOTE:** Perhaps maintaining this doesn't make sense.
Rather, anyone using it should port their code to wxmplot:
https://pypi.org/project/wxmplot/

IIRC, wxmplot is heavier weight, but should support everything
that wxmpl does -- and is is still maintained

Status
------

This package has seen little maintenance for years.

However, it has been minimally updated to run with recent versions of
Python, wxPython, and Matplotlib. It was most recently tested with:

- Python 3.13
- wxPython 4.2.3
- matplotlib 3.10.3

Demo status:

``plotting.py``: runs fine

``picking_points.py``: no errors, but the point picking isn't working

``stripcharting.py``: crashes out at startup

**NOTE:** Picking functionality is disabled / broken -- it needs to be updated for modern wxPython (and maybe MPL, too)

PRs accepted!

-Chris Barker

WxMpl - Painless matplotlib embedding for wxPython
--------------------------------------------------

The `wxmpl' module provides an matplotlib `FigureCanvas' with user-interaction
features like point-under-cursor and zooming in on a selected area.
Support for creating stripcharts, plots that update as their data changes, is
also included.

Documentation of the module itself is available in the`reference/'
subdirectory.  An introduction to using matplotlib with WxMpl is available in
the `tutorial/' subdirectory.  Scripts demonstrating some of matplotlib's
examples with WxMpl and plotting stripcharts data are in the `demos/'
subdirectory.


REQUIREMENTS
------------

* Python 3.8 or greater: http://www.python.org

* wxPython 4.0 or later: http://www.wxpython.org

(It may work with earlier versions, but this is what it was tested on)

* matplotlib 3.0 or later: https://matplotlib.org/

(Also may work for eariler versions, but >= 0.9.8 anyway)

PLATFORMS
---------

WxMpl has been tested under Windows 10 and Mac OS 11 [wxPython > 4.0.0]. It has also reported to work on Linux -- anywhere wxPython and matplotlib work should be fine.


INSTALLATION
------------

The Python setuptools and pip system provides packaging, compilation, and installation
for wxmpl.

To install, execute the following command as superuser::

  $ python setup.py install [OPTIONS]

Or:

  $ pip install ./

For more information about installation options, execute the following
command:
  > python setup.py install --help

For information about other setuptools commands, execute the following command:
  > python setup.py install --help-commands

**NOTE** The packaging system has not been updated for modern standards -- PRs accepted!

AVAILABILITY
------------

Project curently being manged on gitHub here:

https://github.com/NOAA-ORR-ERD/wxmpl

AUTHOR
------

WxMpl was written by: Ken McIvor <mcivor@iit.edu>

Contributions from: Carlo Segre <segre@iit.edu>

Currently maintained by: Chris Barker <Chris.Barker@noaa.gov>


COPYRIGHT & LICENSE
-------------------

  Copyright 2005-2009 Illinois Institute of Technology

  Permission is hereby granted, free of charge, to any person obtaining
  a copy of this software and associated documentation files (the
  "Software"), to deal in the Software without restriction, including
  without limitation the rights to use, copy, modify, merge, publish,
  distribute, sublicense, and/or sell copies of the Software, and to
  permit persons to whom the Software is furnished to do so, subject to
  the following conditions:

  The above copyright notice and this permission notice shall be
  included in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
  IN NO EVENT SHALL ILLINOIS INSTITUTE OF TECHNOLOGY BE LIABLE FOR ANY
  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

  Except as contained in this notice, the name of Illinois Institute
  of Technology shall not be used in advertising or otherwise to promote
  the sale, use or other dealings in this Software without prior written
  authorization from Illinois Institute of Technology.

