import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="youtube-search-fork",
    version="1.2.3",
    description="Search on youtube avoiding the use their heavily rate-limited API. Fork of original youtube-search by joetats",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/pluja/youtube_search-fork",
    author="Pluja",
    author_email="pluja@r3d.red",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["youtube_search"],
    include_package_data=True,
    install_requires=["requests"],
)
