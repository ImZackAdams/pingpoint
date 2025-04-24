from setuptools import setup, find_packages

# Load README.md as long_description for PyPI
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pingpoint',  # PyPI project name
    version='1.0.1',  # Bump version from 1.0.0 for new release
    description='A fast CLI tool for HTTP, DNS, and SSL diagnostics',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Zack Adams',
    author_email='imZackAdams@protonmail.com',
    url='https://github.com/ImZackAdams/pingpoint',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'pingpoint=pingpoint.cli:cli',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: System :: Networking :: Monitoring",
    ],
    python_requires='>=3.6',
)
