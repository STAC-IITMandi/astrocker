reg={'astropy': 'https://github.com/astropy/astropy',
 'specutils': 'https://github.com/astropy/specutils',
 'astroquery': 'https://github.com/astropy/astroquery',
 'photutils': 'https://github.com/astropy/photutils',
 'ginga': 'https://github.com/ejeschke/ginga',
 'astroML': 'https://github.com/astroML/astroML',
 'pydl': 'https://github.com/weaverba137/pydl',
 'APLpy': 'https://github.com/aplpy/aplpy',
 'reproject': 'https://github.com/astropy/reproject',
 'pyvo': 'https://github.com/pyvirtobs/pyvo',
 'gammapy': 'https://github.com/gammapy/gammapy',
 'ccdproc': 'https://github.com/astropy/ccdproc',
 'sncosmo': 'https://github.com/sncosmo/sncosmo',
 'glueviz': 'https://github.com/glue-viz/glue',
 'pyregion': 'https://github.com/astropy/pyregion',
 'imexam': 'https://github.com/spacetelescope/imexam',
 'spherical-geometry': 'https://github.com/spacetelescope/spherical_geometry',
 'gwcs': 'https://github.com/spacetelescope/gwcs',
 'spectral-cube': 'https://github.com/radio-astro-tools/spectral-cube',
 'astroplan': 'https://github.com/astropy/astroplan',
 'astroscrappy': 'https://github.com/astropy/astroscrappy',
 'naima': 'https://github.com/zblz/naima',
 'omnifit': 'https://github.com/RiceMunk/omnifit',
 'astro-gala': 'https://github.com/adrn/gala',
 'galpy': 'https://github.com/jobovy/galpy',
 'hendrics': 'https://github.com/StingraySoftware/HENDRICS',
 'stingray': 'https://github.com/StingraySoftware/stingray',
 'halotools': 'https://github.com/astropy/halotools',
 'cluster-lensing': 'https://github.com/jesford/cluster-lensing',
 'marxs': 'https://github.com/Chandra-MARX/marxs',
 'pyspeckit': 'https://github.com/pyspeckit/pyspeckit',
 'linetools': 'https://github.com/linetools/linetools',
 'poliastro': 'https://github.com/poliastro/poliastro',
 'hips': 'https://github.com/hipspy/hips',
 'regions': 'https://github.com/astropy/regions',
 'synphot': 'https://github.com/spacetelescope/synphot_refactor',
 'astropy-healpix': 'https://github.com/astropy/astropy-healpix',
 'saba': 'https://github.com/astropy/saba',
 'dust_extinction': 'https://github.com/karllark/dust_extinction',
 'feets': 'https://github.com/carpyncho/feets',
 'corral-pipeline': 'https://github.com/toros-astro/corral',
 'baseband': 'https://github.com/mhvk/baseband',
 '': 'https://github.com/NASA-Planetary-Science/sbpy',
 'einsteinpy': 'https://github.com/einsteinpy/einsteinpy',
 'astroalign': 'https://github.com/toros-astro/astroalign'}

import sys
import os
import subprocess
import git
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
dev=sys.argv[1]
pkg=sys.argv[2]
if dev=='false':
    install(pkg)
else:
    str='./'+pkg
    repo = git.Repo.clone_from(reg[pkg],str)
    print("successfully installed",pkg,'in dev mode')
