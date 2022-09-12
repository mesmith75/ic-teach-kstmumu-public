Multi Variate Analysis
======================

A multivariate analysis (MVA) is a catch-all term for data analysis that combines features of several variables. Examples of MVAs include Fisher Discriminants, Decision Trees, Boosted Decision Trees (BDTs), Neural Networks (NN). The precise choice of MVA is up to the analyst, depending on what they are trying to achieve.

Many HEP analyses use an MVA for the purpose of classification - usually to divide the data into background and signal for improved precision. An MVA is often more powerful than a simple cut-based selection as it can exploit non-linear relations between many variables.

[This notebook](https://github.com/mesmith75/ic-teach-kstmumu-public/blob/main/MVA/MVA_example.ipynb) provides a brief example of an MVA with two variables. You can launch it with [![Binder here](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mesmith75/ic-teach-kstmumu-public/main?filepath=MVA/MVA_example.ipynb)

For a more in-depth introduction you are advised to follow the [scikit-learn tutorial](https://scikit-learn.org/stable/tutorial/index.html). A quick google will give you many more tutorials for MVAs.
