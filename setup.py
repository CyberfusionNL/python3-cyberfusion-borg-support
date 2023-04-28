"""A setuptools based setup module."""

from setuptools import setup

setup(
    name="python3-cyberfusion-borg-support",
    version="1.3.10.1",
    description="BorgSupport Python library/tools",
    author="William Edwards",
    author_email="wedwards@cyberfusion.nl",
    url="https://vcs.cyberfusion.nl/shared/python3-cyberfusion-borg-support",
    license="Closed",
    packages=[
        "cyberfusion.BorgSupport",
        "cyberfusion.BorgSupport.exceptions",
    ],
    package_dir={"": "src"},
    platforms=["linux"],
    data_files=[],
)
