from setuptools import setup
from stargazerz import __version__

setup(
    name='stargazerz',
    version=__version__,
    description='Efficiently Retrieve Email Addresses and Usernames of Stargazers from GitHub Repositories',
    author='Tanveet',
    author_email='tanveet.gill@gmail.com',
    url='https://github.com/tsinghgill/stargazerz',
    packages=['stargazerz'],
    install_requires=[
        'beautifulsoup4==4.12.2',
        'requests==2.31.0',
        'tqdm==4.66.1',
    ],
    long_description='A Python tool that scrapes GitHub for stargazers\' emails and usernames using multithreading for speed and efficiency. No API key required.',
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)