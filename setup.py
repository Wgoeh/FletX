from setuptools import find_packages, setup

# LOADING DOCUMENTATION
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'FletX',
    version = '1.0.0',
    packages = find_packages(),
    install_requires = [
        'httpx',
        'simplejson',
        'colorlog',
        'flet>=0.3.0',
        'pydantic>=2.11.5',
        'typing-extensions',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = '#Einswilli',
    author_email = 'einswilligoeh@email.com',
    description = 'SwitchPay Python SDK for AllDotPy internal use. ',
    url = 'https://github.com/AllDotPy/iSwitch.git',
)