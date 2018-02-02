#!/usr/bin/env pythonw
# Purpose: Demonstrates different plots from the matplotlib examples collection
# Author: Ken McIvor <mcivor@iit.edu>, deriving from the matplotlib examples
# collection

# Updated for newer matplotlib by Chris Barker (PythonCHB@gmail.com)
#    2/1/2018
#
# Copyright 2002-2004 John D. Hunter, 2005 Illinois Institute of Technology
#
# Distributed under the license agreement for matplotlib 0.72.
#
# For information on the usage and redistribution of this file, and for a
# DISCLAIMER OF ALL WARRANTIES, see the file "LICENSE" that ships with the
# matplotlib 0.72 or http://matplotlib.sourceforge.net/license.html


__version__ = '2.1'


import wx
import wxmpl
import matplotlib
import matplotlib.cm as cm
import numpy as np

from pylab import normpdf


def plot_simple(fig):
    t = np.arange(0.0, 2.0, 0.01)
    s = np.sin(2 * np.pi * t)
    c = np.cos(2 * np.pi * t)

    axes = fig.gca()
    axes.plot(t, s, linewidth=1.0)
    axes.plot(t, c, linewidth=1.0)

    axes.set_xlabel('time (s)')
    axes.set_ylabel('voltage (mV)')
    axes.set_title('About as simple as it gets, folks')
    axes.grid(True)


def plot_subplot(fig):
    def f(t):
        return np.cos(2 * np.pi * t) * np.exp(-t)
    t1 = np.arange(0.0, 5.0, 0.10)
    t2 = np.arange(0.0, 5.0, 0.02)

    a1 = fig.add_subplot(2, 1, 1)
    a1.plot(t1, f(t1), 'bo')
    a1.plot(t2, f(t2), 'k')
    a1.grid(True)
    a1.set_title('A Tale of 2 Subplots')
    a1.set_ylabel('Damped oscillation')

    a2 = fig.add_subplot(2, 1, 2)
    a2.plot(t2, np.cos(2 * np.pi * t2), 'r>')
    a2.grid(True)
    a2.set_xlabel('time (s)')
    a2.set_ylabel('Undamped')


def plot_subplot_sharex(fig):
    def f(t):
        return np.cos(2 * np.pi * t) * np.exp(-t)
    t1 = np.arange(0.0, 5.0, 0.10)
    t2 = np.arange(0.0, 5.0, 0.02)

    a1 = fig.add_subplot(2, 1, 1)
    a1.plot(t1, f(t1), 'bo')
    a1.plot(t2, f(t2), 'k')
    a1.grid(True)
    a1.set_title('Two Subplots Sharing an Axis')
    a1.set_ylabel('Damped oscillation')
    for ticklabel in a1.get_xticklabels():
        ticklabel.set_visible(False)

    a2 = fig.add_subplot(2, 1, 2, sharex=a1)
    a2.plot(t2, np.cos(2 * np.pi * t2), 'r>')
    a2.grid(True)
    a2.set_xlabel('time (s)')
    a2.set_ylabel('Undamped')


def plot_histogram(fig):
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    axes = fig.gca()
    # the histogram of the data
    n, bins, patches = axes.hist(x, 100, normed=1)

    # add a 'best fit' line
    y = normpdf(bins, mu, sigma)
    l = axes.plot(bins, y, 'r--', linewidth=2)

    axes.set_xlim((40, 160))
    axes.set_xlabel('Smarts')
    axes.set_ylabel('P')
    axes.set_title('IQ: mu=100, sigma=15')
#    axes.set_title(r'$\rm{IQ:}\/ \mu=100,\/ \sigma=15$')


def plot_fill(fig):
    t = np.arange(0.0, 1.01, 0.01)
    s = np.sin(2 * 2 * np.pi * t)

    axes = fig.gca()
    axes.fill(t, s * np.exp(-5 * t), 'r')
    axes.grid(True)


def plot_log(fig):
    dt = 0.01
    t = np.arange(dt, 20.0, dt)

    a1 = fig.add_subplot(2, 1, 1)
    a1.semilogx(t, np.sin(2 * np.pi * t))
    a1.set_ylabel('semilogx')
    a1.grid(True)

    a2 = fig.add_subplot(2, 1, 2)
    a2.loglog(t, 20 * np.exp(-t / 10.0), basey=4)
    a2.xaxis.grid(True, which='minor')  # minor grid on too
    a2.set_xlabel('time (s)')
    a2.set_ylabel('loglog')
    a2.grid(True)


def plot_polar(fig):
    import pylab

    r = np.arange(0, 1, 0.001)
    theta = 2 * 2 * np.pi * r

    # radar green, solid grid lines
    matplotlib.rc('grid', color='#316931', linewidth=1, linestyle='-')

    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True, facecolor='#d5de9c')
    ax.plot(theta, r, color='#ee8d18', lw=3)

    ax.set_title("And there was much rejoicing!", fontsize=14)
    matplotlib.rcdefaults()


def plot_polar_subplot(fig):
    #
    # Polar demo
    #
    import pylab

    r = np.arange(0, 1, 0.001)
    theta = 2 * 2 * np.pi * r

    # radar green, solid grid lines
    matplotlib.rc('grid', color='#316931', linewidth=1, linestyle='-')

    ax = fig.add_subplot(1, 2, 1, polar=True, facecolor='#d5de9c')
    ax.plot(theta, r, color='#ee8d18', lw=3)

    ax.set_title("And there was much rejoicing!", fontsize=14)
    matplotlib.rcdefaults()

    #
    # First part of the subplot demo
    #
    def f(t):
        return np.cos(2 * np.pi * t) * np.exp(-t)

    t1 = np.arange(0.0, 5.0, 0.10)
    t2 = np.arange(0.0, 5.0, 0.02)

    A1 = fig.add_subplot(1, 2, 2)
    A1.plot(t1, f(t1), 'bo')
    A1.plot(t2, f(t2), 'k')
    A1.grid(True)

    A1.set_title('A tale of one subplot')
    A1.set_ylabel('Damped oscillation', fontsize=10)
    A1.set_xlabel('time (s)', fontsize=10)


def plot_legend(fig):
    a = np.arange(0, 3, .02)
    c = np.exp(a)
    d = np.fromiter(reversed(c), dtype=c.dtype)

    axes = fig.gca()
    lines = axes.plot(a, c, 'k--', a, d, 'k:', a, c + d, 'k')
    names = ('Model length', 'Data length', 'Total message length')
    axes.legend(lines, names, loc='upper center', shadow=True)
    axes.set_ylim([-1, 20])
    axes.grid(False)
    axes.set_xlabel('Model complexity --->')
    axes.set_ylabel('Message length --->')
    axes.set_title('Minimum Message Length')
    axes.set_xticklabels([])
    axes.set_yticklabels([])


def plot_image(fig):
    def func3(x, y):
        return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)

    dx, dy = 0.025, 0.025
    x = np.arange(-3.0, 3.0, dx)
    y = np.arange(-3.0, 3.0, dy)
    X, Y = np.meshgrid(x, y)
    Z = func3(X, Y)

    axes = fig.gca()
    axes.imshow(Z, cmap=cm.jet, extent=(-3, 3, -3, 3))


def plot_layered_images(fig):
    def func3(x, y):
        return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)

    # make these smaller to increase the resolution
    dx, dy = 0.05, 0.05

    x = np.arange(-3.0, 3.0, dx)
    y = np.arange(-3.0, 3.0, dy)
    X, Y = np.meshgrid(x, y)

    # when layering multiple images, the images need to have the same
    # extent.  This does not mean they need to have the same shape, but
    # they both need to render to the same coordinate system determined by
    # xmin, xmax, ymin, ymax

    xmin, xmax, ymin, ymax = min(x), max(x), min(y), max(y)
    extent = xmin, xmax, ymin, ymax
    Z1 = np.array(([0, 1] * 4 + [1, 0] * 4) * 4)
    Z1.shape = 8, 8  # chessboard
    Z2 = func3(X, Y)

    axes = fig.gca()
    axes.imshow(Z1, cmap=cm.gray, interpolation='nearest', extent=extent)
    axes.imshow(Z2, cmap=cm.jet, alpha=.9,
                interpolation='bilinear', extent=extent)


def plot_axes(fig):
    # create some data to use for the plot
    dt = 0.001
    t = np.arange(0.0, 10.0, dt)
    r = np.exp(-t[:1000] / 0.05)               # impulse response
    x = np.random.randn(len(t))
    s = np.convolve(x, r, mode=2)[:len(x)] * dt  # colored noise

    # the main axes is subplot(111) by default
    axes = fig.gca()
    axes.plot(t, s)
    axes.set_xlim((0, 1))
    axes.set_ylim((1.1 * min(s), 2 * max(s)))
    axes.set_xlabel('time (s)')
    axes.set_ylabel('current (nA)')
    axes.set_title('Gaussian colored noise')

    # this is an inset axes over the main axes
    a = fig.add_axes([.65, .6, .2, .2], facecolor='y')
    n, bins, patches = a.hist(s, 400, normed=1)
    a.set_title('Probability')
    a.set_xticks([])
    a.set_yticks([])

    # this is another inset axes over the main axes
    a = fig.add_axes([.2, .6, .2, .2], facecolor='y')
    a.plot(t[:len(r)], r)
    a.set_title('Impulse response')
    a.set_xlim((0, 0.2))
    a.set_xticks([])
    a.set_yticks([])


#
# Demo Infrastructure
#

class Demo:

    def __init__(self, title, plotFunction, size=(6.0, 3.7), dpi=96):
        self.title = title
        self.plotFunction = plotFunction
        self.size = size
        self.dpi = dpi

    def run(self):
        frame = wxmpl.PlotFrame(None,
                                -1,
                                self.title,
                                size=self.size,
                                dpi=self.dpi)
        self.plotFunction(frame.get_figure())
        frame.draw()
        frame.Show()

    def makeButton(self, parent):
        btn = wx.Button(parent, -1, self.title)
        btn.Bind(wx.EVT_BUTTON, self.OnButton)
        return btn

    def OnButton(self, evt):
        self.run()


DEMONSTRATIONS = [
    Demo('Simple Plot', plot_simple),
    Demo('Subplots', plot_subplot),
    Demo('Shared X Axes', plot_subplot_sharex),
    Demo('Histogram Plot', plot_histogram),
    Demo('Filled Polygons', plot_fill),
    Demo('Logarithmic Scaling', plot_log),
    Demo('Polar Plot', plot_polar, (6.0, 6.0)),
    Demo('Polar and Linear Subplots', plot_polar_subplot, (8.0, 4.0)),
    Demo('Linear Plot with a Legend', plot_legend),
    Demo('Pseudocolor Image', plot_image),
    Demo('Layered Images', plot_layered_images),
    Demo('Overlapping Axes', plot_axes)
]


class TestFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        buttons = [demo.makeButton(self) for demo in DEMONSTRATIONS]

        sizer = wx.BoxSizer(wx.VERTICAL)
        for btn in buttons:
            sizer.Add(btn, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizer)
        self.Fit()

        self.Bind(wx.EVT_WINDOW_DESTROY, self.OnWindowDestroy)

    def OnWindowDestroy(self, evt):
        wx.GetApp().ExitMainLoop()


def main():
    app = wx.App()
    frame = TestFrame(None, title='WxMpl Demos')
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()
