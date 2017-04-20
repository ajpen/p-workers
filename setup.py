import setuptools

setuptools.setup(
    name="P-Workers",
    version="0.2.0",
    url="https://github.com/ajpen/P-Workers",

    author="Anfernee Jervis",
    author_email="anferneejervis@gmail.com",

    description="Process workers with multiple capabilities.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
