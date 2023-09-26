from pkg_resources import DistributionNotFound,get_distribution
from distutils.core import setup


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound :
        return None

install_deps = [
    'numpy',
    'regex',
    'tqdm',
    'gym'
]
tf_ver = '2.0.0a'
if get_dist('tensorflow>='+ tf_ver) is None and get_dist('tensorflow_gpu>='+tf_ver) is None:
    install_deps.append('tensorflow>='+tf_ver)

setup(
    name='CNNBias',
    packages=['mitdeeplearning'],
    version='0.3.0',
    license='MIT',
    description= 'A hands on project of CNN through uncovering BIAS',
    author= 'Hingolekar Mahesh Kumar',
    author_email= 'h.msk0075@gmail.com',
    keywords=['deep learning', 'neural networks','tensorflow','introduction'],
    install_requires = install_deps,
    package_data={
    'mitdeeplearning': ['bin/*', 'data/*', 'data/faces/DF/*', 'data/faces/DM/*', 'data/faces/LF/*', 'data/faces/LM/*'],
}

)