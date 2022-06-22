# UBCpdk 1.6.4

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gdsfactory/ubc/HEAD)
[![pypi](https://img.shields.io/pypi/v/ubcpdk)](https://pypi.org/project/ubcpdk/)
[![issues](https://img.shields.io/github/issues/gdsfactory/ubc)](https://github.com/gdsfactory/ubc/issues)
![forks](https://img.shields.io/github/forks/gdsfactory/ubc)
![Stars](https://img.shields.io/github/stars/gdsfactory/ubc)
[![mit](https://img.shields.io/github/license/gdsfactory/ubc)](https://choosealicense.com/licenses/mit/)
[![codecov](https://codecov.io/gh/gdsfactory/ubc/branch/master/graph/badge.svg?token=T3kCV2gYE9)](https://codecov.io/gh/gdsfactory/ubc)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


UBC SiEPIC Ebeam PDK from [edx course](https://www.edx.org/course/silicon-photonics-design-fabrication-and-data-ana) for gdsfactory.
It provides a fully python driven flow alternative for the edx course for the most advanced users.

## Documentation

- run notebooks on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gdsfactory/ubc/HEAD)
- [UBCpdk docs](https://gdsfactory.github.io/ubc/) and [code](https://github.com/gdsfactory/ubc)
- [gdsfactory docs](https://gdsfactory.github.io/gdsfactory/)
- [miniforge install instructions](https://github.com/conda-forge/miniforge#mambaforge)


## Installation

### Installation for users


If you are on Windows, I recommend you install gdspy with Anaconda3, Miniconda3 or [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) (faster conda alternative) and `pip` for gdsfactory.


```
mamba install gdspy -y
pip install ubcpdk --upgrade
gf tool install
```

If you want to get all the extras (mode solvers, meep, circuit simulation ...)

```
mamba install gdspy -y
mamba install pymeep=*=mpi_mpich_* -y
pip install ubcpdk --upgrade
gf tool install
```

Mamba is a faster alternative to conda, if you don't want to install mamba, you can also replace `mamba install gdspy -y` with `conda install -c conda-forge gdspy -y`

If you use linux or MacOs you can install directly from pip `pip install ubcpdk` specify a specific version `pip install ubcpdk==1.6.4`
and update to the latest version with `pip install ubcpdk --upgrade`

I also recommend you install the gdsfactory link to klayout `gf tool install`



### Installation for developers

For developers you need to `git clone` the GitHub repository, fork it, git add, git commit, git push and merge request your changes.

```
git clone https://github.com/gdsfactory/ubc.git --shallow-exclude=gh-pages
cd ubc
pip install -e .
pip install pre-commit
pre-commit install
python install_tech.py
gf tool install
```

## Acks

UBCpdk top contributors:

- Joaquin Matres (Google): maintainer of gdsfactory
- Thomas Dorch (Freedom Photonics): for Meep's material database access, MPB sidewall angles, and add_pin_path
- Lukas Chrostowski (UBC professor): creator of the course and maintainer of the PDK cells

Links:

- [UBC docs](https://gdsfactory.github.io/ubc/) and [repo](https://github.com/gdsfactory/ubc)
- [gdsfactory docs](https://gdsfactory.github.io/gdsfactory/)
- [edx course](https://www.edx.org/course/silicon-photonics-design-fabrication-and-data-ana)
- [siepic Ebeam PDK](https://github.com/lukasc-ubc/SiEPIC_EBeam_PDK)
- [awesome photonics list](https://github.com/joamatab/awesome_photonics)
