import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="functional-functions",
    version = "0.0.2",
    author = "Lawrence Chin",
    author_email = "lawrence.chin@compass.com",
    description = "Commonly used functions by the Compass FBI Team",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UrbanCompass/Functional-Functions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", 
    ],
    python_requires='>=3.6'
)