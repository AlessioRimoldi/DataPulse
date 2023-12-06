from setuptools import setup, find_packages

setup(
    name='data_visualization_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'your-script = your_package.module:main_function',
        ],
    },
    # metadata to display on PyPI
    author="Your Name",
    author_email="your.email@example.com",
    description="This is an Example Package",
    keywords="hello world example examples",
    url="http://example.com/HelloWorld/",   # project home page, if any
)