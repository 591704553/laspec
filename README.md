## laspec
[![DOI](https://zenodo.org/badge/202476664.svg)](https://zenodo.org/badge/latestdoi/202476664) ![Upload Python Package](https://github.com/hypergravity/laspec/workflows/Upload%20Python%20Package/badge.svg)

Modules for basic operations on **LA**MOST **spec**tra, etc.

If you make use of this package in your research, please cite the paper below:
- [Deriving the Stellar Labels of LAMOST Spectra with the Stellar LAbel Machine (SLAM)](https://ui.adsabs.harvard.edu/abs/2020ApJS..246....9Z/abstract)
## author
Bo Zhang, [bozhang@nao.cas.cn](mailto:bozhang@nao.cas.cn)

## home page
- [https://github.com/hypergravity/laspec](https://github.com/hypergravity/laspec)
- [https://pypi.org/project/laspec/](https://pypi.org/project/laspec/)

## install
- for the latest **stable** version: `pip install -U laspec`
- for the latest **github** version: `pip install -U git+git://github.com/hypergravity/laspec`

## module structure
- **binning** \
    module for rebinning spectra
    - rebin(wave, flux, flux_err, mask): rebin spectra
- **ccf** \
    module for cross correlation function
    - sine_bell: a sine bell function
    - wxcorr: weigted cross-correlation
    - wxcorr_cost: negative CCF function
    - wxcorr_spec: weigted cross-correlation of two spectra
    - wxcorr_rvgrid: weighted cross correlation given an RV grid
    - wxcorr_cost_binary: negative CCF function
    - wxcorr_spec_binary: weigted cross-correlation of two spectra
    - wxcorr_rvgrid_binary: weighted cross correlation given an RV grid
    - **RVM** Radial Velocity Machine
        - measure: measure the RV of single stars
        - measure_binary: measure the RV of binary systems
- **convolution** \
    module for spectral Gaussian convolution
    - conv_spec: capable to tackle arbitrary R_hi and R_lo but relatively slow
- **interpolation** \
    interpolation, but slow, please do not use.
    - Interp1q: use numpy.interp instead
- **lamost** \
    module for LAMOST spectra and files
    - lamost_filepath(planid, mjd, spid, fiberid)
    - lamost_filepath_med(planid, mjd, spid, fiberid)
    - sdss_filepath(plate, mjd, fiberid)
- **mrs** \
    MRS module
    - MrsSpec: MRS spectrum (B / R)
    - MrsEpoch: MRS epoch spectrum (B + R)
    - MrsFits(astropy.io.fits.HDUList): MRS fits reader
    - MrsSource(numpy.ndarray): MRS source constructor 
- **line_indices** \
    module to measure spectral line index (EW)
    - measure_line_index: measure line index (EW)
- **normalization** \
    module to normalize spectra
    - normalize_spectrum_spline: a Python version of Chao's method (recommended)
    - normalize_spectrum_poly: polynomial normalization
    - normalize_spectrum_general： a unified wrapper of spline and poly
    - NOTE: bad pixels (e.g., cosmic rays) should be properly removed before normallization
- **qconv** \
    quick convolution, designed for two cases:
    - conv_spec_Gaussian(wave, flux, R_hi=3e5, R_lo=2000): scalar resolution to scalar resolution instrumental broadening
    - conv_spec_Rotation(wave, flux, vsini=100., epsilon=0.6): stellar rotation broadening    
- **read_spectrum** \
    module to read LAMOST/SDSS spectra
    - read_spectrum(fp): read LAMOST low-res spectra
    - read_lamostms(fp): read LAMOST medium-res spcetra    
- **spec** \
    modules for operations on general spectra (deprecated)
    - Spec: spec class
- **wavelength** \
    module to convert wavelength between air and vacuum
    - wave_log10: log10 wavelength grid
    - vac2air: convert wavelength from vacuum to air
    - air2vac: convert wavelength from air to vacuum


## acknowledgements

...
