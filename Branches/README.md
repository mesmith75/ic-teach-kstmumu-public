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

* `ProbNNx` - the probability that a given track is positively identified as a given hypotheses. For example `mu_plus_ProbNNmu` is the probability that the `mu_plus` is a real muon, `(1 - mu_plus_ProbNNpi)` would be the probability that it is not a pion.
* `PV` - primary vertex, the point of the proton-proton collision
* `ENDVERTEX` - position of the reconstructed decay vertex of the particle
* `ENDVERTEX_CHI2` - <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> of the vertex fit. Essentially how well do the tracks form a vertex
* `IPCHI2` - The IP <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> . The IP is the impact parameter - the perpendicular distance between a trajectory and the PV. The uncertainty is a combination of the vertex <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> and the uncertainty on the particle trajectory. The `IPCHI2` is the square of the IP divided by the square of the uncertainty to from a <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> type qauntity.
* `P` - momentum of the particle in units of MeV
* `PT` - momentum of the particle transverse to the beam line in units of MeV
* `PX`, `PY`, `PZ`, `PE` - components of the 4-momentum.
* `M`, 'mass' - the invariant mass of a particle. If the particle is composite the mass is the product of a fit of the kinematics of the decay products.
* `FD` - distance between a particles end vertex and origin vertex in units of mm
* `FDCHI2` - FD <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" />, where the uncertainty is the combination of the <img src="https://latex.codecogs.com/gif.latex?\chi^{2}" /> of the two vertices
* `ETA` - the pseudorapidity of the particle
* `DIRA` - the cosine of the angle between the particle's flight vector and momentum vector
* `OWNPV` - quantities labelled with `OWNPV` mean they are calculated with respect to that particle's assigned primary vertex.

Other
-------

* `year` - The data taking year. This is not interesting information.
* `polarity` - The magnet polarity of the LHCb detector. As this is not real data the value is meaningless. This is not interesting information.
