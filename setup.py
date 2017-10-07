from setuptools import setup, find_packages

setup(
    name='terrace',
    url='https://github.com/outsideris/terrace',
    license='Mozilla Public License 2.0',
    author='Outsider',
    author_email='outsideris@gmail.com',
    description='Web management UI for Terraform',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
