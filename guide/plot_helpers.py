import matplotlib.pyplot as plt
import numpy
import re

def activity_color(plx):
    return (1, 1, 0.5, 0.5) if plx == 'plx' else None

def plot_activity(d1, d2, plx, points):
    key = 'd{}_d{}_{}_activity'.format(d1, d2, plx)
    color = activity_color(plx)
    activity = lambda p: getattr(p, key)()
    activities = numpy.array([activity(p) for p in points])
    plt.hist(activities, 100, range=(-4, 4), color=color, label=key)

def compare_activities(d1, d2, points, ylim=10000):
    plot_activity(d1, d2, 'base', points)
    plot_activity(d1, d2, 'plx', points)
    plt.legend()
    plt.ylim(0, ylim)
    plt.axvline(color='red')
    plt.title('D{} vs D{}'.format(d1, d2))
    plt.show()

# def opacify(color):
    # opaque_color = list(color)
    # opaque_color[3] = 1
    # return tuple(opaque_color)
def compare_point_groups_by(feature, point_groups, buckets=20, xrng=None):
    fig, axis1 = plt.subplots()        
    all_labels = []
    all_values = []
    min_values = []
    max_values = []
    title_parts = []
    for label, points in point_groups:
        values = [getattr(p, feature)() for p in points]
        all_labels.append(label)
        all_values.append(values)
        min_values.append(min(values))
        max_values.append(max(values))

    if xrng is None:
        xrng = (min(min_values), max(max_values))
    colors = [None, (1, 1, 0.5, 0.5)]
    i = 0
    legend_line = None
    legend_label = None
    avgs = []
    axes = []
    for label, values in zip(all_labels, all_values):
        axis = axis1 if i == 0 else axis1.twinx()
        axis.hist(values, buckets, range=xrng, color=colors[i], label=label)
        avg = numpy.mean(values)
        plt.axvline(avg, color=colors[i], ls='dashed', lw=4)
        # axes.append(axis)
        title_parts.append('{} (avg={})'.format(label, str(round(avg, 2))))
        plot_line, plot_label = axis.get_legend_handles_labels()
        if legend_line is None:
            legend_line = plot_line
            legend_label = plot_label
        else:
            legend_line += plot_line
            legend_label += plot_label
        i += 1

    plt.title('{} for {} points'.format(feature, ' vs. '.join(title_parts)), fontsize=16, y=1.08)
    plt.legend(legend_line, legend_label)
    plt.show()

gRNA_features = {
    'molecular_mass': None,
    'gc_content': None,
    'dna_starts_with_g': 2,
    'dna_starts_with_gg': 2,
    'dna_starts_with_atg': 2,
    'dna_contains_gg': 2,
    'dna_contains_atg': 2,
    'nearest_neighbor_dS': None,
    'nearest_neighbor_dH': None,
    'nearest_neighbor_Tm': None,
    'mfold_dS': None,
    'mfold_dH': None,
    'mfold_dG': None,
    'mfold_Tm': None,
    'hairpin_stem_length': 10,
    'hairpin_loop_length': 10,
    'hairpin_count': 10,
    'num_1_mm_bowtie_hits': 10,
    'num_1_mm_bowtie_hits_same_chromosome': 10,
    'num_1_or_2_mm_bowtie_hits': 10,
    'num_1_or_2_mm_bowtie_hits_same_chromosome': 10
}
