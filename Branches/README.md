Variables
=========

In the data sets provided are many variables. Their meanings are described here.

Coordinate System
-----------------

LHCb uses a right-handed coordinate system with the origin at the nominal interaction point. The 'z' axis is along the beam pipe, from the interaction point towards the muon stations. 'y' is vertically upwards and 'x' is towards the centre of the LHC.

Particles
---------

* The final state particles are labelled by `K`, `Pi`, `mu_plus`, `mu_minus`. The `K` and `Pi` combination is labelled by `Kstar` and the two muons are combined into `J_psi`. Finally the the *B* candidate is labelled by `B0`.

Variables
---------

* `MC15TuneV1_ProbNNx` - the probability that a given track is positively identified as a given hypotheses. For example `mu_plus_MC15TuneV1_ProbNNmu` is the probability that the `mu_plus` is a real muon, `(1 - mu_plus_MC15TuneV1_ProbNNpi)` would be the probability that it is not a pion. The MC15TuneV1 refers to how the neural network that calculates the probabilities was trained.
* `PV` - primary vertex, the point of the proton-proton collision
* `ENDVERTEX` - position of the reconstructed decay vertex of the particle
* `ENDVERTEX_CHI2` - <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> of the vertex fit. Essentially how well do the tracks form a vertex
* `IPCHI2` - The IP in units of the uncertainty in it. The IP is the impact parameter - the perpendicular distance between a trajectory and the PV. The uncertainty is a combination of the vertex <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> and the uncertainty on the particle trajectory.
* `P` - momentum of the particle in units of MeV
* `PT` - momentum of the particle transverse to the beam line in units of MeV
* `PX`, `PY`, 'PZ', `PE` - components of the 4-momentum.
* `FD` - distance between a particles end vertex and origin vertex in units of mm
* `FDCHI2` - FD in units of uncertainty, where the uncertainty is the combination of the <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> of the two vertices
