Variables
=========

In the data sets provided are many variables. Their meanings are described here.

Particles
---------

* The final state particles are labelled by `K`, `Pi`, `mu_plus`, `mu_minus`. The `K` and `Pi` combination is labelled by `Kstar` and the two muons are combined into `Jpsi`. Finally the the *B* candidate is labelled by `B0`.

Variables
---------

* `ProbNNx` - the probability that a give track is positively identified as a given hypotheses. For example `mu_plus_ProbNNmu` is the probability that the `mu_plus` is a real muon, `(1 - mu_plus_ProbNNpi)` would be the probability that it is not a pion
* `PV` - primary vertex, the point of the proton-proton collision
* `ENDVERTEX` - position of the reconstructed decay vertex of the particle
* `ENDVERTEX_CHI2` - <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> of the vertex fit. Essentially how well do the tracks form a vertex
* `IP` - impact parameter. The perpendicular distance between a particle trajectory and some point.
* `IPCHI2` - The IP in units of the uncertainty in it. The uncertainty is a combination of the vertex <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> and the uncertainty on the particle trajectory.
* `P` - momentum of the particle in units of MeV
* `PT` - momentum of the particle transverse to the beam line in units of MeV
* `FD` - distance between a particles end vertex and origin vertex in units of mm
* `FDCHI2` - FD in units of uncertainty, where the uncertainty is the combination of the <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> of the two vertices
