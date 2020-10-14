# pylint: skip-file

import setuptools
from importlib.machinery import SourceFileLoader
from os import path
import sys
import pathlib


if sys.version_info < (3, 6):
    raise RuntimeError("aiogeoip requires Python 3.6+")

HERE = pathlib.Path(__file__).parent
IS_GIT_REPO = (HERE / '.git').exists()

module = SourceFileLoader(
    fullname="version", path=path.join("aiogeoip", "version.py"),
).load_module()

libraries = []

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("CHANGES.md", "r") as fh:
    changes = fh.read()

# def read(f):
#     return (HERE / f).read_text('utf-8').strip()

setuptools.setup(
    name="aiogeoip",
    version=module.__version__,
    packages=["aiogeoip"],
    license=module.package_license,
    description=module.package_info,
    author=module.__author__,
    author_email=module.team_email,
    keywords=["aio", "python", "asyncio", "geoip", "io", "geolocation"],
    provides=["aiogeoip"],
    long_description=long_description+'\n\n'+changes,
    long_description_content_type='text/markdown',
    url="https://github.com/py-paulo/aiogeoip.git",
    classifiers=[
        "Environment :: Console",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Framework :: AsyncIO',
    ],
    project_urls={
        'GitHub: issues': 'https://github.com/py-paulo/aiogeoip/issues',
        'GitHub: repo': 'https://github.com/py-paulo/aiogeoip',
        'Read the Docs': 'https://aiogeoip.readthedocs.io/en/latest/',
    },
    python_requires='>=3.6',
    install_requires=["aiohttp~=3.6.0", "requests~=2.24.0", "ujson~=3.2.0"],
)
