from setuptools import find_packages, setup

setup(
    name="balloon_scan",
    version="0.1",
    description="Scan simulator for a balloon",
    zip_safe=False,
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.19"
    ],
)
