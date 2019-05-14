import io
import re
from setuptools import setup

with io.open('amitypes/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name="amityping",
    version=version,
    description='LCLS analysis monitoring type annotations',
    long_description='The package used at LCLS-II for type annotations for online analysis monitoring',
    author='Seshu Yamajala, Daniel Damiani',
    author_email='',
    url='http://github.com/slac-lcls/amityping',
    packages=["amitypes"],
    package_data={
        "amitypes": ["py.typed"],
    },
    install_requires=['numpy', 'mypy_extensions'],
    classifiers=[
        'Development Status :: 1 - Planning'
        'Environment :: Other Environment',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)
