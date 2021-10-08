Data samples
============

You are given various simulated data samples as Pandas dataframes, serialised with pickle. The `total_dataset.pkl` is the data to analyse. It is a representation of the real data that would come out of the LHCb detector. It will therefore contain the interesting signal decay, as well as various backgrounds. To help you understand these backgrounds simulation samples of them are provided as listed below:

* `sig.pkl` - The signal decay, simulated as per the Standard Model
* `jpsi.pkl` - <img src="https://latex.codecogs.com/gif.latex?B^{0}\rightarrow{}J/\psi{}K^{\ast{}0} " /> with <img src="https://latex.codecogs.com/gif.latex?J/\psi\rightarrow\mu\mu " />
* `psi2S.pkl` - <img src="https://latex.codecogs.com/gif.latex?B^{0}\rightarrow{}\psi{}(2S)K^{\ast{}0} " /> with <img src="https://latex.codecogs.com/gif.latex?\psi{}(2S)\rightarrow\mu\mu " />
* `jpsi_mu_k_swap.pkl` - <img src="https://latex.codecogs.com/gif.latex?B^{0}\rightarrow{}J/\psi{}K^{\ast{}0} " /> with the muon reconstructed as kaon and the kaon reconstructed as a muon
* `jpsi_mu_pi_swap.pkl` - <img src="https://latex.codecogs.com/gif.latex?B^{0}\rightarrow{}J/\psi{}K^{\ast{}0} " /> with the muon reconstructed as pion and the pion reconstructed as a muon
* `k_pi_swap.pkl` - signal decay but with the kaon reconstructed as a pion and the pion reconstructed as a kaon
* `phimumu.pkl` - <img src="https://latex.codecogs.com/gif.latex?B_{s}^{0}\rightarrow{}\phi\mu\mu " /> with <img src="https://latex.codecogs.com/gif.latex?\phi{}\rightarrow{}KK " /> and one of the kaons reconstructed as a pion
* `pKmumu_piTok_kTop.pkl` - <img src="https://latex.codecogs.com/gif.latex?\Lambda_{b}^{0}\rightarrow{}pK\mu\mu " /> with the proton reconstructed as a kaon and the kaon reconstructed as a pion
* `pKmumu_piTop.pkl`  - <img src="https://latex.codecogs.com/gif.latex?\Lambda_{b}^{0}\rightarrow{}pK\mu\mu " /> with the proton reconstructed as a pion

In addition you are given a sample of simulation called `acceptance.pkl`. This is generated to be flat in the three anglular variables and <img src="https://latex.codecogs.com/gif.latex?q^{2}" />
