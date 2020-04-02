import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="linkedin-jobs-filter", # Replace with your own username
    version="0.0.1",
    author="Kais Kawar",
    author_email="kaiskawar@gmail.com",
    description="Retrieve linkedin jobs with advanced search functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kais-viz/linkedin-jobs-filter/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)