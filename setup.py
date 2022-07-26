from setuptools import setup, find_packages


setup(
    name='paseri',
    version="0.0.0.9000",
    install_requires=["mecab-python3", "pandas"],
    author="suzuna",
    description="paseri: wrapper of MeCab converting pandas DataFrame",
    url="https://github.com/suzuna/paseri",
    packages=find_packages(where="setup"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10"
)
