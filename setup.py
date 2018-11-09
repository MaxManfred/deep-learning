from setuptools import find_packages
from setuptools import setup

long_description = '''
    TODO
'''

setup(
    name='2017-python-deep-learning',
    version='1.0.0',
    description='Python Deep Learning training',
    long_description=long_description,
    author='Massimo Manfredino',
    author_email='massimo.manfredino@gmail.com',
    url='https://github.com/MaxManfred/deep-learning',
    download_url='https://github.com/MaxManfred/deep-learning',
    license='GNU General Public License v3.0',
    install_requires=[
        'keras>=2.2.4'
        # 'numpy>=1.9.1',
    #                   'scipy>=0.14',
    #                   'six>=1.9.0',
    #                   'pyyaml',
    #                   'h5py',
    #                   'keras_applications>=1.0.6',
    #                   'keras_preprocessing>=1.0.5'
    ],
    extras_require={
    #     'visualize': ['pydot>=1.2.4'],
        'tests': [
            'pytest'
            # ,
    #               'pytest-pep8',
    #               'pytest-xdist',
    #               'pytest-cov',
    #               'pandas',
    #               'requests'
        ],
    },
    # classifiers=[
    #     'Development Status :: 5 - Production/Stable',
    #     'Intended Audience :: Developers',
    #     'Intended Audience :: Education',
    #     'Intended Audience :: Science/Research',
    #     'License :: OSI Approved :: MIT License',
    #     'Programming Language :: Python :: 2',
    #     'Programming Language :: Python :: 2.7',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.6',
    #     'Topic :: Software Development :: Libraries',
    #     'Topic :: Software Development :: Libraries :: Python Modules'
    # ],
    packages=find_packages()
)
