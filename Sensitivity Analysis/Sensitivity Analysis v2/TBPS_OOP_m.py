# -*- coding: utf-8 -*-
# Made by NathanvEs - 15/10/2021

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from iminuit import Minuit
from scipy.optimize import curve_fit

class LHCb:
    def __init__(self, df = None):
        """
        Loads in data 
        
        if df == None:
            # Change this path to whatever it is on your personal computer
            folder_path = "data/csv"
            file_name = "/total_dataset.csv"
            file_path = folder_path + file_name
            self.dF = pd.read_csv(file_path)
        else:
            
        """
        self.dF_unfiltered = pd.read_pickle("data/total_dataset.pkl")
        self.dF = df
        self.dF_filtered_out = None
        
    def Mass(self, PE, P):
        """
        Returns the mass in units of MeV/c^2
        """
        return (PE**2 - P**2)**0.5

    def apply_selection_threshold(self, dataF, column, threshold, opposite=False):
        """
        Generic function for applying a selection criteria
        """
        mask = (dataF[column] >= threshold)
        if opposite == True:
            dataF = dataF[~mask]
        else:
            dataF = dataF[mask]
        return dataF

    def probability_assignment(self):
        """
        Assigning probability variables
        """
        mu_plus_ProbNNmu = self.dF['mu_plus_MC15TuneV1_ProbNNmu']
        mu_minus_ProbNNmu = self.dF['mu_minus_MC15TuneV1_ProbNNmu']
        mu_plus_ProbNNp = self.dF["mu_plus_MC15TuneV1_ProbNNp"]
        mu_plus_probNNk = self.dF["mu_plus_MC15TuneV1_ProbNNk"]
        mu_plus_ProbNNpi = self.dF["mu_plus_MC15TuneV1_ProbNNpi"]
        K_ProbNNp = self.dF["K_MC15TuneV1_ProbNNp"]
        K_probNNk = self.dF["K_MC15TuneV1_ProbNNk"]
        Pi_ProbNNp = self.dF["Pi_MC15TuneV1_ProbNNp"]
        Pi_probNNk = self.dF["Pi_MC15TuneV1_ProbNNk"]
        Pi_ProbNNpi = self.dF["Pi_MC15TuneV1_ProbNNpi"]

        """
        Some selection criteria
        P(kaon): ProbNNK · (1 − ProbNNp) > 0.05 
        P(pion): ProbNNπ · (1 − ProbNNK) · (1 − ProbNNp) > 0.1
        """
        
        self.dF['accept_kaon'] = K_probNNk * (1 - K_ProbNNp)
        self.dF['accept_pion'] = Pi_ProbNNpi * (1 - Pi_probNNk) * (1 - Pi_ProbNNp)
        self.dF['accept_muon'] = self.dF[['mu_plus_MC15TuneV1_ProbNNmu', 'mu_plus_MC15TuneV1_ProbNNmu']].max(axis=1)
        self.dF['dilepton_mass'] = self.Mass(self.dF['mu_minus_PE'],self.dF['mu_minus_P']) + self.Mass(self.dF['mu_plus_PE'],self.dF['mu_plus_P'])
        
    def probability_filter(self, order):
        """
        Filtering the data based on the probabilities
        """
        
        if order == 0:
            self.dF_unfiltered = self.dF
    
            # Probability selections (based on CERN paper)
            self.dF = self.apply_selection_threshold(self.dF_unfiltered, 'accept_kaon', 0.05)
            self.dF = self.apply_selection_threshold(self.dF, 'accept_pion', 0.1)
            self.dF = self.apply_selection_threshold(self.dF, 'accept_muon', 0.2)
            self.dF_filtered_out = self.apply_selection_threshold(self.dF_unfiltered, 'accept_kaon', 0.05, opposite=True)
            self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'accept_pion', 0.1, opposite=True)], ignore_index=True).drop_duplicates()
            self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'accept_muon', 0.2, opposite=True)], ignore_index=True).drop_duplicates()
        else:
            self.dF = self.apply_selection_threshold(self.dF, 'accept_kaon', 0.05)
            self.dF = self.apply_selection_threshold(self.dF, 'accept_pion', 0.1)
            self.dF = self.apply_selection_threshold(self.dF, 'accept_muon', 0.2)
            self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'accept_kaon', 0.05, opposite=True)], ignore_index = True).drop_duplicates()
            self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'accept_pion', 0.1, opposite=True)], ignore_index=True).drop_duplicates()
            self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'accept_muon', 0.2, opposite=True)], ignore_index=True).drop_duplicates()
             
            print(len(self.dF),len(self.dF_unfiltered),len(self.dF_filtered_out)) 
            
    def trasv_mom_filter(self, order):
        
        if order == 0:
           self.dF_unfiltered = self.dF
           
           # Transverse momenta selections (based on CERN paper)
           self.dF = self.apply_selection_threshold(self.dF_unfiltered, 'mu_plus_PT', 800)
           self.dF = self.apply_selection_threshold(self.dF, 'mu_minus_PT', 800)
           self.dF = self.apply_selection_threshold(self.dF, 'K_PT', 250)
           self.dF = self.apply_selection_threshold(self.dF, 'Pi_PT', 250)
           self.dF_filtered_out = self.apply_selection_threshold(self.dF_unfiltered, 'mu_plus_PT', 800, opposite=True)
           self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'mu_minus_PT', 800, opposite=True)], ignore_index=True).drop_duplicates()
           self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'K_PT', 250, opposite=True)], ignore_index=True).drop_duplicates()
           self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'Pi_PT', 250, opposite=True)], ignore_index=True).drop_duplicates()
                       
        else:
            # Transverse momenta selections (based on CERN paper)
            self.dF = self.apply_selection_threshold(self.dF, 'mu_plus_PT', 800)
            self.dF = self.apply_selection_threshold(self.dF, 'mu_minus_PT', 800)
            self.dF = self.apply_selection_threshold(self.dF, 'K_PT', 250)
            self.dF = self.apply_selection_threshold(self.dF, 'Pi_PT', 250)
            self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'mu_plus_PT', 800, opposite=True)], ignore_index=True).drop_duplicates()
            self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'mu_minus_PT', 800, opposite=True)], ignore_index=True).drop_duplicates()
            self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'K_PT', 250, opposite=True)], ignore_index=True).drop_duplicates()
            self.dF_filtered_out = pd.concat([self.dF_filtered_out, self.apply_selection_threshold(self.dF_unfiltered, 'Pi_PT', 250, opposite=True)], ignore_index=True).drop_duplicates()
            
            print(len(self.dF),len(self.dF_unfiltered),len(self.dF_filtered_out))
    
            # Masses selection (based on CERN paper)
            # Seems already included unless I am mistaken
            
            # K, Pi, mu: chi_IP^2 > 9 definitely already included in the data not needed to select on it
            # Bo: DIRA > 0.9995 already included in the data
            # Bo: chi_IP^2 < 25 already included in the data (actually < 16)

    def intermediary_plotting(self):
        # Some plotting
        n1, bin1, patches1 = plt.hist(self.dF_unfiltered['B0_MM'], range=[5170, 5600], bins=300, zorder=1)
        n2, bin2, patches2 = plt.hist(self.dF['B0_MM'], range=[5170, 5600], bins=300, zorder=3)
        # n3, bin3, patches3 = plt.hist(self.dF_filtered_out['B0_MM'], range=[5170, 5600], bins=300, zorder=2)
        plt.title('Invariant Mass of $B_0$ with & without background')
        plt.xlabel('MM($B_0$)(MeV/$c^2$)')
        plt.ylabel('Number of Candidates')
        plt.legend(['unfiltered','filtered','filtered out'])
        
        # Fitting to the invariant mass plot
        def gauss_exp(x, a, b, c, e, f):
            return a * np.exp(-((x-b)**2)/2/c**2) + np.exp(e*x +f)
        
        def gauss(x, a, b, c):
            return a * np.exp(-((x-b)**2)/2/c**2)
        
        def exp_tail(x, b, c):
            return np.exp(b*x +c)
        
        
        bin1_alt = []
        for i in range(len(n1)):
            bin1_alt.append((bin1[i]+bin1[i+1])/2)
        
        bin2_alt = []
        for i in range(len(n1)):
            bin2_alt.append((bin2[i]+bin2[i+1])/2)
            
        bin3_alt = []
        for i in range(len(n1)):
            bin3_alt.append((bin3[i]+bin3[i+1])/2)
        
        guess2 = [7000, 5270, 20]
        params2, cov2 = curve_fit(gauss, bin2_alt, n2, p0=guess2)
        
        guess3 = [-0.0007, 9.5]
        params3, cov3 = curve_fit(exp_tail, bin3_alt, n3, p0 = guess3)
        
        guess1 = params2.tolist() + params3.tolist()
        
        params1, cov1 = curve_fit(gauss_exp, bin1_alt, n1, p0 = guess1)
        
        
        x_fit = np.linspace(5170, 5600, 500)
        fit1 = gauss_exp(x_fit, *params1)
        fit2 = gauss(x_fit, *params2)
        fit3 = exp_tail(x_fit, *params3)
        
        plt.plot(x_fit, fit1, color = "skyblue", zorder=4)
        plt.plot(x_fit, fit2, color = "pink", zorder=5)
        plt.plot(x_fit, fit3, color = "black", zorder=6)
        plt.show()

    # """
    # First thing to do is to split up total data in bins based on q^2 range. 
    # Then for each bin get the values of fl, afb, at, aim and compare to sm values.
    # """

    def q_separate(self):
        """
        SEPARATING DATA INTO q^2 BINS
        """
        self.bins = []
        q_ranges = [[0.01,0.98],[1.1,2.5],[2.5,4.0],[4.0,6.0],[6.0,8.0],
                    [15.0,17.0],[17.0,19.0],[11.0,12.5],[1.0,6.0],[15.0,17.9]]
        q_ranges_paper = [[0.01,2.0],[2.0,4.0],[4.0,8.5],[10.0,13.0],[14.5,16.0],[16.0,23.0]]
        
        for q_range in q_ranges_paper:
            mask = (self.dF['q2'] > q_range[0]) & (self.dF['q2'] < q_range[1])
            bin = self.dF[mask]
            self.bins.append(bin)

    """
    _test_bin = 3
    _test_afb = 0.7
    _test_fl = 0.0
    
    x = np.linspace(-1, 1, 500)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
    ax1.plot(x, [ll_dG_dctl(fl=i, afb=_test_afb, _bin=_test_bin) for i in x])
    ax1.set_title(r'$A_{FB}$ = ' + str(_test_afb))
    ax1.set_xlabel(r'$F_L$')
    ax1.set_ylabel(r'$-\mathcal{L}$')
    ax1.grid()
    ax2.plot(x, [ll_dG_dctl(fl=_test_fl, afb=i, _bin=_test_bin) for i in x])
    ax2.set_title(r'$F_{L}$ = ' + str(_test_fl))
    ax2.set_xlabel(r'$A_{FB}$')
    ax2.set_ylabel(r'$-\mathcal{L}$')
    ax2.grid()
    plt.tight_layout()
    plt.show()
    """

    def fit_observable(self):
        """
        FITTING FOR THE OBSERVABLES PER q^2 BIN
        """
        
        def dgamma_dcosthetak(fl, cos_theta_k):
            """
            Returns the pdf defined above
            :param fl: F_L observable
            :param cos_theta_k: cos(theta_k)
            :return:
            """
            ctk = cos_theta_k
            acceptance = 0.5  # acceptance "function"
            scalar_array = ((3/2)*fl*ctk**2 + (3/4)*(1-fl)*(1-ctk**2)) * acceptance
            normalised_scalar_array = scalar_array * 2  # normalising scalar array to account for the non-unity acceptance function
            return normalised_scalar_array


        def ll_dG_dctk(fl, _bin):
            """
            Returns the negative log-likelihood of the pdf defined above
            :param fl: f_l observable
            :param afb: a_fb observable
            :param _bin: number of the bin to fit
            :return:
            """
            _bin = int(_bin)
            data = self.bins[_bin]
            ctk = data['costhetak']
            normalised_scalar_array = dgamma_dcosthetak(fl=fl, cos_theta_k=ctk)
            return - np.sum(np.log(normalised_scalar_array))
        
        
        def dgamma_dcosthetal(fl, afb, cos_theta_l):
            """
            Returns the pdf defined above
            :param fl: f_l observable
            :param afb: a_fb observable
            :param cos_theta_l: cos(theta_l)
            :return:
            """
            ctl = cos_theta_l
            acceptance = 0.5  # acceptance "function"
            scalar_array = ((3/4)*fl*(1-ctl**2) + (3/8)*(1-fl)*(1+ctl**2) + afb*ctl) * acceptance
            normalised_scalar_array = scalar_array * 2  # normalising scalar array to account for the non-unity acceptance function
            return normalised_scalar_array
        
        
        def ll_dG_dctl(fl, afb, _bin):
            """
            Returns the negative log-likelihood of the pdf defined above
            :param fl: f_l observable
            :param afb: a_fb observable
            :param _bin: number of the bin to fit
            :return:
            """
            _bin = int(_bin)
            data = self.bins[_bin]
            ctl = data['costhetal']
            normalised_scalar_array = dgamma_dcosthetal(fl=fl, afb=afb, cos_theta_l=ctl)
            return - np.sum(np.log(normalised_scalar_array))
        
        
        def dgamma_dphi(fl, at, aim, phi):
            """
            Returns the pdf defined above
            :param fl: f_l observable
            :param at: a_t observable
            :param aim: a_im observable
            :param cos_theta_l: cos(theta_l)
            :return:
            """
            acceptance = 0.5  # acceptance "function"
            scalar_array = (1/(2*np.pi)) * (1 + (1/2)*(1-fl)*at*np.cos(2*phi) + aim*np.sin(2*phi)) * acceptance
            normalised_scalar_array = scalar_array * 2  # normalising scalar array to account for the non-unity acceptance function
            return normalised_scalar_array
        
        
        def ll_dG_dphi(fl, at, aim, _bin):
            """
            Returns the negative log-likelihood of the pdf defined above
            :param fl: f_l observable
            :param afb: a_fb observable
            :param _bin: number of the bin to fit
            :return:
            """
            _bin = int(_bin)
            data = self.bins[_bin]
            phi = data['phi']
            normalised_scalar_array = dgamma_dphi(fl=fl, at=at, aim=aim, phi=phi)
            return - np.sum(np.log(normalised_scalar_array))
        
        
        ll_dG_dctl.errordef = Minuit.LIKELIHOOD
        ll_dG_dctk.errordef = Minuit.LIKELIHOOD
        ll_dG_dphi.errordef = Minuit.LIKELIHOOD
        decimal_places = 3
        starting_point = [-0.1,0.0]
        
        self.fls_l, self.fl_errs_l, self.fls_k, self.fl_errs_k, self.fls_p, self.fl_errs_p = [], [], [], [], [], []
        self.afbs, self.afb_errs = [], []
        self.ats, self.at_errs = [], []
        self.aims, self.aim_errs = [], []
        
        for i in range(len(self.bins)):
            l = Minuit(ll_dG_dctl, fl=starting_point[0], afb=starting_point[1], _bin=int(i))
            k = Minuit(ll_dG_dctk, fl=starting_point[0], _bin=int(i))
            p = Minuit(ll_dG_dphi, fl=starting_point[0], at=starting_point[0], aim=starting_point[0], _bin=int(i))
        
            l.fixed['_bin'] = True  # fixing the bin number as we don't want to optimize it
            l.limits=((-1.0, 1.0), (-1.0, 1.0), None)
            l.migrad()
            l.hesse()
        
            k.fixed['_bin'] = True  # fixing the bin number as we don't want to optimize it
            k.limits = ((-1.0, 1.0), None)
            k.migrad()
            k.hesse()
        
            p.fixed['_bin'] = True  # fixing the bin number as we don't want to optimize it
            p.limits = ((-1.0, 1.0), (-1.0, 1.0), (-1.0, 1.0), None)
            p.migrad()
            p.hesse()
        
            # Append all the values
            self.fls_l.append(l.values[0])
            self.afbs.append(l.values[1])
            self.fl_errs_l.append(l.errors[0])
            self.afb_errs.append(l.errors[1])
        
            self.fls_k.append(k.values[0])
            self.fl_errs_k.append(k.errors[0])
        
            self.fls_p.append(p.values[0])
            self.ats.append(p.values[1])
            self.aims.append(p.values[2])
            self.fl_errs_p.append(p.errors[0])
            self.at_errs.append(p.errors[1])
            self.aim_errs.append(p.errors[2])
        
            #print(f"Bin {i}: {np.round(fls_l[i], decimal_places)} pm {np.round(fl_errs_l[i], decimal_places)},",
            #      f"{np.round(afbs_l[i], decimal_places)} pm {np.round(afb_errs_l[i], decimal_places)}. "
            #      f"Function minimum considered valid: {m.fmin.is_valid}")


    def plot_observable(self):
        """
        PLOTTING OBSERVABLES
        """
        plotting_bool = True
        # plt.rcParams.update({'errorbar.capsize': 2, 'text.usetex': True})
        
        if plotting_bool == True:
            plt.figure()
            plt.title("Values of $F_{L}$ for all 3 distributions (l, k \& phi) per $q^2$ bin")
            plt.errorbar(range(0,len(self.bins)), self.fls_p, yerr=self.fl_errs_p, marker='x', markersize=6, linestyle='none')
            plt.errorbar(range(0,len(self.bins)), self.fls_l, yerr=self.fl_errs_l, marker='x', markersize=6, linestyle='none')
            plt.errorbar(range(0,len(self.bins)), self.fls_k, yerr=self.fl_errs_k, marker='x', markersize=6, linestyle='none')
            plt.legend(['$F_{Lphi}$','$F_{Ll}$','$F_{Lk}$'])
            plt.grid()
            plt.show()
        
            plt.figure()
            plt.title("Values of $A_{FB}$ per $q^2$ bin")
            plt.errorbar(range(0,len(self.bins)),self.afbs, yerr=self.afb_errs, marker='x', markersize=6, linestyle='none')
            plt.legend(['$A_{FB}$'])
            plt.grid()
            plt.show()
        
            plt.figure()
            plt.title("Values of $A_{T}$ per $q^2$ bin")
            plt.errorbar(range(0,len(self.bins)), self.ats, yerr=self.at_errs, marker='x', markersize=6, linestyle='none')
            plt.legend(['$A_{T}$'])
            plt.grid()
            plt.show()
        
            plt.figure()
            plt.title("Values of $A_{im}$ per $q^2$ bin")
            plt.errorbar(range(0,len(self.bins)), self.aims, yerr=self.aim_errs, marker='x', markersize=6, linestyle='none')
            plt.legend(['$A_{im}$'])
            plt.grid()
            plt.show()
            
    def run_analysis(self):
        """
        Runs the analysis
        
        set order = 0 to apply probability filter then transverse momentum filter
        set order = 1 to apply transverse momentum filter then probability filter
        
        """
        order = 1
        # Use the filtering functions first
        self.probability_assignment()
        if order == 0:
            self.probability_filter(order)
            self.trasv_mom_filter(1-order)
        elif order == 1:
            self.trasv_mom_filter(1-order)
            self.probability_filter(order)            
            
        # Intermediary plot - comment out if not needed
        self.intermediary_plotting()
        # Separate q bins and Standard Model values
        self.q_separate()
        self.fit_observable()
        self.plot_observable()

if __name__ == '__main__':
    df = pd.read_pickle("total_dataset_f.pkl")
    Cern_Stuff = LHCb(df)
    Cern_Stuff.probability_assignment()
    # Separate q bins and Standard Model values
    Cern_Stuff.q_separate()
    Cern_Stuff.fit_observable()
    Cern_Stuff.plot_observable()


