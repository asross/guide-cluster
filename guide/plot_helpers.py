import matplotlib.pyplot as plt
import numpy
import re
from .datapoint import feature_units

def activity_color(plx):
    return (0.5, 1, 0.5, 0.5) if plx == 'plx' else (0.5, 0.5, 1, 0.5)

def feature_label(feature):
    return '{} ({})'.format(feature, feature_units[feature])

def feature_values(feature, points):
    return [getattr(p, feature)() for p in points]

def plot_activity(d1, d2, plx, points):
    key = 'd{}_d{}_{}_activity'.format(d1, d2, plx)
    color = activity_color(plx)
    activity = lambda p: getattr(p, key)()
    activities = numpy.array([activity(p) for p in points])
    plt.xlabel('activity')
    plt.ylabel('number of points')
    plt.title(key)
    plt.hist(activities, 100, range=(-4, 4), color=color, label=key)

def compare_activities(d1, d2, points, ylim=10000):
    plot_activity(d1, d2, 'base', points)
    plot_activity(d1, d2, 'plx', points)
    plt.legend()
    plt.ylim(0, ylim)
    plt.axvline(color='red')
    plt.title('D{} vs D{}'.format(d1, d2))

def compare_point_groups_by(feature, active, inactive, bins=20, xrng=None, show=False, axis1=None):
    if axis1 is None: _fig, axis1 = plt.subplots()
    axis2 = axis1.twinx()
    axis1.set_xlabel(feature_label(feature))
    active_values = feature_values(feature, active)
    inactive_values = feature_values(feature, inactive)

    if xrng is None:
        xmin = min(min(active_values), min(inactive_values))
        xmax = max(max(active_values), max(inactive_values))
        xrng = (xmin, xmax)

    active_color = 'b'
    inactive_color = (1, 1, 0.5, 0.5)

    axis1.set_ylabel('number of active points')
    axis1.hist(active_values, bins, range=xrng, color=active_color, label='active')
    axis2.set_ylabel('number of inactive points')
    axis2.hist(inactive_values, bins, range=xrng, color=inactive_color, label='inactive')

    line1, label1 = axis1.get_legend_handles_labels()
    line2, label2 = axis2.get_legend_handles_labels()
    plt.legend(line1 + line2, label1 + label2)

    active_avg = numpy.mean(active_values)
    inactive_avg = numpy.mean(inactive_values)

    plt.axvline(active_avg, color=active_color, ls='dashed', lw=4)
    plt.axvline(inactive_avg, color=inactive_color, ls='dashed', lw=4)

    active_sym = '$\mathregular{\overline{active}}$'
    inactive_sym = '$\mathregular{\overline{inactive}}$'
    title = '{}, {}={}, {}={}'.format(feature, active_sym, round(active_avg, 2), inactive_sym, round(inactive_avg, 2))
    plt.title(title)

    if show:
        plt.show()

class figure_grid():
    def __init__(self, rows, cols, title):
        self.rows = rows
        self.cols = cols
        self.title = title
        self.fig = plt.figure(figsize=(13, 3.333*self.rows))
        
    def __enter__(self):
        return self.fig

    def __exit__(self, type, value, traceback):
        self.fig.suptitle(self.title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        self.fig.subplots_adjust(top=0.80 + 0.0625*(self.rows-1))
        plt.show()
