"""
First exploration into LHCb data

Date created: 19/10/21
Author: Tom Cowperthwaite
"""
import pickle
import matplotlib.pyplot as plt
from os import listdir
import numpy as np
from iminuit import Minuit

plt.style.use('style.mplstyle')

#define functions
def load(inc_acceptance=False):
    global files, titles, variables
    if inc_acceptance:
        files = listdir('real_data')
    else:
        files = listdir('real_data')[:-1]
    titles = [i[:-4] for i in files]
    file_dict = {}
    for i in files:
        with open('real_data/'+i, 'rb') as f:
            file_dict[i[:-4]] = pickle.load(f)
    variables = list(file_dict['total_dataset'].columns)
    return file_dict
    
def plot_1hist(title, var, bins=20, save=False, density=True):
    fig = plt.figure(figsize=[15,10])
    plt.hist(dic[title][var], bins=bins, density=density)
    plt.xlabel(var)
    if density:
        plt.ylabel('Frequency Density')
    else:
        plt.ylabel('Frequency')
    plot_tit = var+' distribution for '+title
    plt.title(plot_tit)
    if save:
        plt.savefig('outputs/single_plots/'+plot_tit+'.png')
    return fig

def overlaid_hist(var, bins=20, save=False):
    fig = plt.figure(figsize=[15,10])
    for title in titles:
        plt.hist(dic[title][var], bins=bins, density=True, label=title)
    plt.xlabel(var)
    plt.ylabel('Frequency Density')
    plot_tit = var+'distribution for all datasets (overlaid)'
    plt.legend()
    plt.title(plot_tit)
    if save:
        plt.savefig('outputs/comparison_plots/'+plot_tit+'.png')
    return fig


#%%

#load data
dic = load()
data = dic['total_dataset']
top_row = dict(data.iloc[0])
subset_100 = data.iloc[range(100)]

#split data into bins
bin_0 = data[(data.q2>0.1) & (data.q2<0.98)]
bin_1 = data[(data.q2>1.1) & (data.q2<2.5)]
bin_2 = data[(data.q2>2.5) & (data.q2<4)]
bin_3 = data[(data.q2>4) & (data.q2<6)]
bin_4 = data[(data.q2>6) & (data.q2<8)]
bin_5 = data[(data.q2>15) & (data.q2<17)]
bin_6 = data[(data.q2>17) & (data.q2<19)]
bin_7 = data[(data.q2>11) & (data.q2<12.5)]
bin_8 = data[(data.q2>1) & (data.q2<6)]
bin_9 = data[(data.q2>15) & (data.q2<17.9)]
b = [bin_0, bin_1, bin_2, bin_3, bin_4, bin_5, bin_6, bin_7, bin_8, bin_9]

# options = [top_row, subset_100, data]
# sel = 2

#%%

#compare q2 between datasets (separate plots)
for i in titles:
    plot_1hist(i, 'q2', save=True)
    
#%%
#general meeting 3 bulletpoints criteria
filtered_1 = data[data.K_MC15TuneV1_ProbNNk*(1-data.K_MC15TuneV1_ProbNNp) > 0.05]
filtered_12 = filtered_1[data.Pi_MC15TuneV1_ProbNNpi*(1-data.Pi_MC15TuneV1_ProbNNk)*(1-data.Pi_MC15TuneV1_ProbNNp) > 0.1]
filtered_123 = filtered_12[(data.mu_plus_MC15TuneV1_ProbNNmu > 0.2) & (data.mu_minus_MC15TuneV1_ProbNNmu > 0.2)]

#%%
plt.figure(1)
plt.hist(data['q2'], bins=20)
plt.hist(filtered_123['q2'], bins=20)

#%%

# from skeleton code
def d2gamma_p_d2q2_dcostheta(fl, afb, cos_theta_l):
    """
    Returns the pdf defined above
    :param fl: f_l observable
    :param afb: a_fb observable
    :param cos_theta_l: cos(theta_l)
    :return:
    """
    ctl = cos_theta_l
    c2tl = 2 * ctl ** 2 - 1
    acceptance = 0.5  # acceptance "function"
    scalar_array = 3/8 * (3/2 - 1/2 * fl + 1/2 * c2tl * (1 - 3 * fl) + 8/3 * afb * ctl) * acceptance
    normalised_scalar_array = scalar_array * 2  # normalising scalar array to account for the non-unity acceptance function
    return normalised_scalar_array

def log_likelihood(fl, afb, _bin):
    """
    Returns the negative log-likelihood of the pdf defined above
    :param fl: f_l observable
    :param afb: a_fb observable
    :param _bin: number of the bin to fit
    :return:
    """
    _bin = b[int(_bin)]
    ctl = _bin['costhetal']
    normalised_scalar_array = d2gamma_p_d2q2_dcostheta(fl=fl, afb=afb, cos_theta_l=ctl)
    return - np.sum(np.log(normalised_scalar_array))

_test_bin = 1
_test_afb = 0.7
_test_fl = 0.0

x = np.linspace(-1, 1, 500)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
ax1.plot(x, [log_likelihood(fl=i, afb=_test_afb, _bin=_test_bin) for i in x])
ax1.set_title(r'$A_{FB}$ = ' + str(_test_afb))
ax1.set_xlabel(r'$F_L$')
ax1.set_ylabel(r'$-\mathcal{L}$')
ax1.grid()

ax2.plot(x, [log_likelihood(fl=_test_fl, afb=i, _bin=_test_bin) for i in x])
ax2.set_title(r'$F_{L}$ = ' + str(_test_fl))
ax2.set_xlabel(r'$A_{FB}$')
ax2.set_ylabel(r'$-\mathcal{L}$')
ax2.grid()
plt.tight_layout()
plt.show()

#%%
bin_number_to_check = 1  # bin that we want to check in more details in the next cell
bin_results_to_check = None

log_likelihood.errordef = Minuit.LIKELIHOOD
decimal_places = 3
starting_point = [-0.1,0.0]
fls, fl_errs = [], []
afbs, afb_errs = [], []
for i in range(len(b)):
    m = Minuit(log_likelihood, fl=starting_point[0], afb=starting_point[1], _bin=i)
    m.fixed['_bin'] = True  # fixing the bin number as we don't want to optimize it
    m.limits=((-1.0, 1.0), (-1.0, 1.0), None)
    m.migrad()
    m.hesse()
    if i == bin_number_to_check:
        bin_results_to_check = m
    fls.append(m.values[0])
    afbs.append(m.values[1])
    fl_errs.append(m.errors[0])
    afb_errs.append(m.errors[1])
    print(f"Bin {i}: {np.round(fls[i], decimal_places)} pm {np.round(fl_errs[i], decimal_places)},", f"{np.round(afbs[i], decimal_places)} pm {np.round(afb_errs[i], decimal_places)}. Function minimum considered valid: {m.fmin.is_valid}")
    
plt.figure(figsize=(8, 5))
plt.subplot(221)
bin_results_to_check.draw_mnprofile('afb', bound=3)
plt.subplot(222)
bin_results_to_check.draw_mnprofile('fl', bound=3)
plt.tight_layout()
plt.show()