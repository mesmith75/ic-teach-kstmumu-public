SM Predictions
==============

The two `.json` files here contain the SM predictions for the <img src="https://latex.codecogs.com/gif.latex?S_{i}" />  and optimised <img src="https://latex.codecogs.com/gif.latex?P_{i}" /> observables along with their theoretical uncertainties. These were calculated in bins of <img src="https://latex.codecogs.com/gif.latex?q^{2}" /> with the [`flavio`](https://flav-io.github.io/) package.

The binning scheme is:

|Bin number| <img src="https://latex.codecogs.com/gif.latex?q^{2}" /> range |
|----------|--------------|
| 0 | 0.1 - 0.98 |
| 1 | 1.1 - 2.5 |
| 2 | 2.5 - 4.0 |
| 3 | 4.0 - 6.0 |
| 4 | 6.0 - 8.0 |
| 5 | 15.0 - 17.0 |
| 6 | 17.0 - 19.0 |
| 7 | 11.0 - 12.5 |
| 8 | 1.0 - 6.0 |
| 9 | 15.0 - 17.9 |

The python notebook [`print_predictions.ipynb`](print_predictions.ipynb) loads the `.json` files and prints their contents.
