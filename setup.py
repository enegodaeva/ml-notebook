from setuptools import setup, find_packages

setup(
    name="ml-notebook",
    version='0.0.1',
    packages=find_packages(exclude=("test",)),
    classifiers=["Programming Language :: Python :: 3"],
    python_requires='>=3.8.*',
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'sklearn',
        'lightgbm',
        'datetime',
        'nltk',
        'pyspellchecker',
        'category_encoders'
    ],
)
