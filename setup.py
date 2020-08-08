import setuptools

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setuptools.setup(
    name="dero-merchant-python-sdk",
    version="1.0.0",
    author="Peppinux",
    description="Python SDK for DERO Merchant REST API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/peppinux/dero-merchant-python-sdk",
    license=license,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
)
