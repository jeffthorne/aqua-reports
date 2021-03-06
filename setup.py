from setuptools import setup, find_packages

setup(
    name='aqua-reports',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'aqua == 0.1.6',
        'openpyxl',
        'PyYaml'
    ],
    entry_points={
        'console_scripts': ['aqua-reports = app.cli:cli']
      }
)