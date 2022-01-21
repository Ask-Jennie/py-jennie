
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ask-jennie',
     version='0.0.1',
     author="Saurabh Pandey",
     py_modules=["jennie"],
     install_requires=['pyperclip'],
     entry_points={
        'console_scripts': [
            'jennie=jennie:execute'
        ],
     },
     author_email="scoder91@gmail.com",
     description="Ask Jennie is a developer autobot.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/dextrop/ask-jennie",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )