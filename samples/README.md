Data samples
============

You are given various simulated data samples as Pandas dataframes in `.csv` format. These should not be dependent on the python version (although they are larger and slower to open than pickles). These can be opened with 

```python
import pandas
my_frame = pandas.read_csv('/path/to/file.csv')
```

The `total_dataset.csv` is the data to analyse. It is a representation of the real data that would come out of the LHCb detector. It will therefore contain the interesting signal decay, as well as various backgrounds. To help you understand these backgrounds simulation samples of them are provided as listed below:

* `sig.csv` - The signal decay, simulated as per the Standard Model
* `jpsi.csv` - <img src="https://latex.codecogs.com/gif.latex?B^{0}\rightarrow{}J/\psi{}K^{\ast{}0} " /> with <img src="https://latex.codecogs.com/gif.latex?J/\psi\rightarrow\mu\mu " />
* `psi2S.csv` - <img src="https://latex.codecogs.com/gif.latex?B^{0}\rightarrow{}\psi{}(2S)K^{\ast{}0} " /> with <img src="https://latex.codecogs.com/gif.latex?\psi{}(2S)\rightarrow\mu\mu " />
* `jpsi_mu_k_swap.csv` - <img src="https://latex.codecogs.com/gif.latex?B^{0}\rightarrow{}J/\psi{}K^{\ast{}0} " /> with the muon reconstructed as kaon and the kaon reconstructed as a muon
* `jpsi_mu_pi_swap.csv` - <img src="https://latex.codecogs.com/gif.latex?B^{0}\rightarrow{}J/\psi{}K^{\ast{}0} " /> with the muon reconstructed as pion and the pion reconstructed as a muon
* `k_pi_swap.csv` - signal decay but with the kaon reconstructed as a pion and the pion reconstructed as a kaon
* `phimumu.csv` - <img src="https://latex.codecogs.com/gif.latex?B_{s}^{0}\rightarrow{}\phi\mu\mu " /> with <img src="https://latex.codecogs.com/gif.latex?\phi{}\rightarrow{}KK " /> and one of the kaons reconstructed as a pion
* `pKmumu_piTok_kTop.csv` - <img src="https://latex.codecogs.com/gif.latex?\Lambda_{b}^{0}\rightarrow{}pK\mu\mu " /> with the proton reconstructed as a kaon and the kaon reconstructed as a pion
* `pKmumu_piTop.csv`  - <img src="https://latex.codecogs.com/gif.latex?\Lambda_{b}^{0}\rightarrow{}pK\mu\mu " /> with the proton reconstructed as a pion
* `Kmumu.csv` - <img src="https://latex.codecogs.com/svg.image?B^{&plus;}\to&space;K^{&plus;}\mu^{&plus;}\mu^{-} " />
* `Kstarp_pi0.csv` - <img src="https://latex.codecogs.com/svg.image?B^{&plus;}\to&space;K^{\ast{}0}\mu^{&plus;}\mu^{-} " /> with <img src="https://latex.codecogs.com/gif.latex?J/\psi\rightarrow\mu\mu " />
* `Jpsi_Kstarp_pi0.csv` - <img src="https://latex.codecogs.com/svg.image?B^{&plus;}\to&space;K^{\ast{}0}J/\psi "/> with <img src="https://latex.codecogs.com/svg.image?K^{\ast{}0}\to{}K^{&plus;}\pi^{0} " /> and <img src="https://latex.codecogs.com/gif.latex?J/\psi\rightarrow\mu\mu " />

In addition you are given a sample of simulation called `acceptance.csv`. This is generated to be flat in the three angular variables and <img src="https://latex.codecogs.com/gif.latex?q^{2}" />
