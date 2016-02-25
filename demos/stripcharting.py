#!/usr/bin/env python
# Purpose: Demonstrates stripcharting using wxmpl
# Author: Ken McIvor <mcivor@iit.edu>
#
# Copyright 2005 Illinois Institute of Technology
#
# See the file "LICENSE" for information on usage and redistribution
# of this file, and for a DISCLAIMER OF ALL WARRANTIES.

import wx
import time
import wxmpl
from numpy import arange, cos, sin, pi, exp


class StripchartApp(wx.App):
    def OnInit(self):
        self.timer = wx.PyTimer(self.OnTimer)
        self.numPoints = 0

        self.frame = wxmpl.PlotFrame(None, -1, 'WxMpl Stripchart Demo')
        self.frame.Show(True)

        # The data to plot
        x =  arange(0.0, 200, 0.1)
        y1 = 4*cos(2*pi*(x-1)/5.7)/(6+x) + 2*sin(2*pi*(x-1)/2.2)/(10)
        y2 = y1 + .5
        y3 = y2 + .5
        y4 = y3 + .5

        # Fetch and setup the axes
        axes = self.frame.get_figure().gca()
        axes.set_title('Stripchart Test')
        axes.set_xlabel('t')
        axes.set_ylabel('f(t)')

        # Attach the StripCharter and define its channels
        self.charter = wxmpl.StripCharter(axes)
        self.charter.setChannels([
            TestChannel('ch1', x, y1),
            TestChannel('ch2', x, y2),
            TestChannel('ch3', x, y3),
            TestChannel('ch4', x, y4)
        ])

        # Prime the pump and start the timer
        self.charter.update()
        self.timer.Start(100)
        return True

    def OnTimer(self):
        # avoid wxPyDeadObject errors
        if not isinstance(self.frame, wxmpl.PlotFrame):
            self.timer.Stop()
            return

        if self.numPoints == self.charter.channels[0].x.shape[0]:
            self.timer.Stop()

        for channel in self.charter.channels:
            channel.tick()

        self.charter.update()


class TestChannel(wxmpl.Channel):
    """
    A data-provider that reveals another point every time its C{tick()} method
    is called.
    """
    def __init__(self, name, x, y):
        """
        Creates a new C{TestChannel} with the matplotlib label C{name} and X
        and Y vectors.
        """
        wxmpl.Channel.__init__(self, name)
        self.x = x
        self.y = y
        self.idx = 0

    def getX(self):
        """
        Returns the current X vector.
        """
        return self.x[0:self.idx]

    def getY(self):
        """
        Returns the current Y vector.
        """
        return self.y[0:self.idx]

    def tick(self):
        """
        Reveals another point from the source X and Y vectors.
        """
        if self.idx < self.x.shape[0]:
            self.setChanged(True)
            self.idx += 1


def main():
    app = StripchartApp()
    app.MainLoop()


if __name__ == '__main__':
    main()
