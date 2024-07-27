from pathlib import Path
from setuptools import setup, find_packages

# Extract version from the package's __init__.py file
version = None
with open("gwrt/__init__.py") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[-1].strip().strip('"').strip("'")
            break

# Read long description from README.md file if it exists
long_description = ""
readme_path = Path("README.md")
if readme_path.is_file():
    long_description = readme_path.read_text()

setup(
    author="Andreas Panteli",
    long_description=long_description,
    long_description_content_type="text/markdown",  # assuming you use Markdown for README
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'sounddevice',
        'numpy',
        'pytest'
    ],
    entry_points={
        "console_scripts": [
            "gwrt=gwrt.cli:main",
        ],
    },
    description="TBA",
    license="MIT License",
    include_package_data=True,
    name="gwrt",
    test_suite="tests",
    url="TBA",
    py_modules=["gwrt"],
    version=version,  # use the version extracted from __init__.py
)
