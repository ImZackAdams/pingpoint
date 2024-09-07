from setuptools import setup, find_packages

setup(
    name='api_diagnostic_tool',  # Your unique package name
    version='1.0.1',
    description='A CLI tool for API diagnostics',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/api_diagnostic_tool',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        api-diagnostic=api_diagnostic_tool.cli:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
