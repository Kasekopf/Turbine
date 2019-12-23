import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read().replace(
        "](", "](https://github.com/Kasekopf/Turbine/blob/master/"
    )

setuptools.setup(
    name="turbine",
    version="0.1.0",
    author="Jeffrey Dudek",
    author_email="jeffreydudek@gmail.com",
    description="A Python 3 tool to harness the google cloud to run shell scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kasekopf/Turbine",
    packages=setuptools.find_packages(),
    license="MIT",
    platforms="Posix; MacOS X; Windows",
    install_requires=["google-cloud-pubsub", "google-cloud-storage", "google-cloud-logging", "google-api-python-client"],
    python_requires='>=3.6',
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
