from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup_params = dict(
    name="ilihelp_bot",
    version="1.0.0",
    description="Family helper bot for Telegram",
    url="https://github.com/vvegorova/ilihelp_bot",
    author="Vera Ilina",
    author_email="vilina.develop@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Chatbots",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="Telegram",
    package_dir={"": "src"},
    packages=find_packages("src"),
    # python_requires=[],
    install_requires=[],  # Optional
    extras_require={
        "test": ["pytest"],
    }
)

if __name__ == "__main__":
    setup(**setup_params)