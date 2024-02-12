from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Source agnostic data visualization tool'
LONG_DESCRIPTION = 'A package that allows you to visualize data from any source in a simple and easy way'

# Setting up
setup(
    name="Viz",
    version=VERSION,
    author="AlessioRimoldi",
    author_email="<alessio.rimoldi.work@neuralnine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['bokeh','calmap','numpy','pandas','matplotlib','scikit-learn','scipy','seaborn','sqlalchemy'],
    keywords=['python', 'web', 'data', 'visualization', 'bokeh', 'tool'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)

