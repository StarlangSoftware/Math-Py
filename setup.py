from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-Math',
    version='1.0.15',
    packages=['Math'],
    url='https://github.com/StarlangSoftware/Math-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Math library',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
