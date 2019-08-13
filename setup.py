from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

name = 'nbimport'

setup(
    name=name,
    version='0.0.0',
    description=long_description.splitlines()[0],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ravindra Marella',
    url='https://github.com/marella/{}'.format(name),
    project_urls={
        'Source Code': 'https://github.com/marella/{}'.format(name),
        'Bug Tracker': 'https://github.com/marella/{}/issues'.format(name),
    },
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: IPython',
    ],
    keywords='{} ipython'.format(name),
)
