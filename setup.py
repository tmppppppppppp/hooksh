import setuptools

AUTHOR = 'B'
MAINTAINER = 'B'
EMAIL = 'tmp@gmail.com'
NAME = 'check-copyright'
SHORT_DESCRIPTION = 'The script for'
URL = 'https://github.com/tmppppppppppp/hooksh'
REQUIRES = []
LICENSE = ''

setuptools.setup(
    
    name=NAME,
    description=SHORT_DESCRIPTION,
    long_description_content_type='text/markdown',
    license=LICENSE,
    version='0.0.1',
    author=AUTHOR,
    maintainer=MAINTAINER,
    author_email=EMAIL,
    url=URL,
    install_requires=REQUIRES,
    py_modules=['check_copyright'],
    scripts=['check_copyright.py'],
    entry_points={'console_scripts': ['check-copyright=check_copyright:main']},
)