import os
import shutil
import setuptools
import subprocess
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt")

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

# copy configuration files
shutil.copy('etc/config.cfg', os.path.expanduser('~/.nellCoin.cfg'))
shutil.copy('etc/miner.cfg', os.path.expanduser('~/.nellCoin-miner.cfg'))

_PKG_ROOT = 'nellCoin'

setuptools.setup(
    name = _PKG_ROOT,
    install_requires=reqs,
    packages = [_PKG_ROOT] + [_PKG_ROOT+'.'+p for p in setuptools.find_packages(_PKG_ROOT)],
    entry_points = {
        'console_scripts': ['nellCoin=nellCoin.bitcoin:run',
                            'minerpy=nellCoin.miner.miner:run',
                            'walletpy=nellCoin.wallet.walletpy:main',],},
    version = "0.0.1",
    description = "Python implementation of Bitcoin",
    url = "https://www.nellCoin.org",
    author = "Obulpathi N Challa",
    author_email = "obulpathi@gmail.com",
    zip_safe = False,
    package_data = {
        _PKG_ROOT: ['data/genesis.dat'],
        },
)
