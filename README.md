# easygit [![Upload Python Package](https://github.com/Sharan-Babu/easygit/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Sharan-Babu/easygit/actions/workflows/python-publish.yml) [![Python application](https://github.com/Sharan-Babu/easygit/actions/workflows/python-app.yml/badge.svg)](https://github.com/Sharan-Babu/easygit/actions/workflows/python-app.yml)
Generate git syntax, commands by interacting with the terminal in English.

Documentation: [Link](https://github.com/Sharan-Babu/easygit/wiki/Documentation)

## How to use:
~~~python
from easygit import Easygit
git = Easygit()
git.interactive()
~~~

## Installation
~~~
pip install easygit
~~~

## Cloning repo 
_Note_: Will likely contain changes not yet released in PyPI library.
~~~
pip install colorama wit
git clone https://github.com/Sharan-Babu/easygit.git
~~~

## Versioning
You can download specific versions of the library [here](https://github.com/Sharan-Babu/easygit/releases).

## Overview

`easygit` library comes with the Easygit class which has the following methods:
### 1) `query()` 
Used to retrieve explanation/_git_ syntax for given sentence.

Example Usage:
~~~python
git = Easygit()
git.query("How to clone a repository using git?")
~~~

Output:<br>
~~~
git clone <repository_web_url>
~~~

### 2) `interactive()` 
Used to start interactive mode in terminal.
~~~python
git = Easygit()
git.interactive()
~~~

Output:<br>
~~~
Interactive mode:

Enter your query: 
~~~

## License
MIT License

## Awesome Contributors
Sharan Babu<br>
Silvoj Rajesh

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
