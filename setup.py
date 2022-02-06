import setuptools

with open("READMEOLD.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='py-jennie',
     version='0.0.1',
     author="Saurabh Pandey",
     py_modules=["jennie"],
     install_requires=['requests'],
     entry_points={
        'console_scripts': [
            'jennie=jennie:execute'
        ],
     },
     author_email="saurabh@ask-jennie.com",
     description="The package targets to automate development task using single line command, The package include task with UI gallery to automate development of small to medium project. The package is a part of ASK Jennie Complete Product.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Ask-Jennie/py-jennie",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )