from setuptools import setup, find_packages

setup(name='my_project', version='0.1', packages=find_packages(), entry_points={'console_scripts':['echo_hello = my_package.my_module:echo']})