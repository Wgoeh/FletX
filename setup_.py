from setuptools import find_packages, setup

# LOADING DOCUMENTATION
with open("PYPI.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'FletXr',
    version = '0.1.4.b230',
    packages = find_packages(),
    install_requires = [
        "aiohttp>=3.12.13",
        "build>=1.2.2.post1",
        "flet[all]>=0.28.3",
        "httpx>=0.28.1",
        "pydantic>=2.11.5",
        "pytest>=8.4.0",
        "setuptools>=80.8.0",
        "uvloop>=0.21.0",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = '#Einswilli',
    author_email = 'einswilligoeh@email.com',
    description = 'The GetX-inspired Python Framework for Building Reactive, Cross-Platform Apps with Flet',
    url = 'https://github.com/AllDotPy/FletX',
)