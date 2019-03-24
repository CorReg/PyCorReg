import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CorReg",
    version="0.0.2",
    author="Clément Thery",
    author_email="corregeous@correg.org",
    description="The Concept, the Method, the Power",
    long_description="The Concept, the Method, the Power",
    long_description_content_type="text/markdown",
    url="http://www.correg.org",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
	install_requires=[
          'pyttsx3',
      ]
)