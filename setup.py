# API install
from distutils.core import setup

setup(name = 'phylogenetics',
    version = '0.1',
    description = 'Python API that provides simple tools for doing phylogenetics.',
    author = 'Zach Sailer',
    author_email = 'zachsailer@gmail.com',
    url = 'https://github.com/Zsailer/phylogenetics',
    download_url = 'https://github.com/Zsailer/phylogenetics/tarball/0.1',
    packages = ['phylogenetics'],
    scripts = ['scripts/blast-seeds.py',
            'scripts/phylo-edit-names.py',
            'scripts/blast-reverse.py',
            'scripts/blast-process.py',
            'scripts/phylo-add-align.py',
            'scripts/phylo-align.py',
            'scripts/phylo-cdhit.py',
            'scripts/phylo-tree.py'
    ],
    install_requires=[
        'numpy',
    ],
    zip_safe = False
)
