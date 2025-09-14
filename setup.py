from setuptools import setup, find_packages

setup(
    name="zoran-asim",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=2.1",
        "numpy",
        "scipy",
        "pyyaml",
    ],
    author="Frédéric Tabary",
    description="Zoran aSiM — Artificial Super-Intelligence Mimétique core modules",
    url="https://github.com/AIformpro/Zoran-2040-aSiM",
    license="MIT",
)
