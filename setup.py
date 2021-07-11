from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.1'
DESCRIPTION = 'Library to learn git'
LONG_DESCRIPTION = 'A package that allows to query git commands easily'

# Setting up
setup(
    name="easygit",
    version=VERSION,
    author="Sharan Babu",
    author_email="sharanbabu2001@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=['wit', 'colorama'],
    keywords=['python', 'chatbot', 'git', 'interactive terminal'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
