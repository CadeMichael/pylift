from setuptools import setup

setup(
    name="pylift",
    version="0.0.1",
    py_modules=["commands"],
    install_requires=[
        "Click",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "pylift = commands:cli",
        ]
    },
)
