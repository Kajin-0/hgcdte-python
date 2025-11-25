# hgcdte

A lightweight Python library for HgCdTe (MCT) material parameters.

This initial version implements:

- Hansen (1982) bandgap model:
  Eg(x, T) in eV
- Cutoff wavelength:
  - Derived from Eg: λc = 1.23984 / Eg
  - Hansen direct polynomial fit λp(x, T)

More modules (carriers, mobility, Auger, optics) will be added in future phases.
