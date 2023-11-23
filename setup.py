from setuptools import setup
from setuptools import find_packages

extras = {}

setup(
    name="lazymodule",
    version="0.0.1",
    description="Lazy Module",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="draft",
    license="Apache",
    author="hz",
    author_email="hzji210@gmail.com",
    url="https://github.com/statelesshz/lazymodule",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.8.0",
    install_requires=[],
    extras_require=extras,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)