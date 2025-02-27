from setuptools import setup, find_packages
import os

VERSION = "0.0.1"

def get_requirements():
    reqs_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    with open(reqs_path, encoding="utf-8") as reqsf:
        return reqsf.read().splitlines()

setup(
    name="jepa",
    version=VERSION,
    description="JEPA research code.",
    python_requires=">=3.9",
    install_requires=get_requirements(),
    packages=find_packages(where="src"),  # Looks inside src/
    package_dir={"": "src"},  # Treats src/ as the package root
)
