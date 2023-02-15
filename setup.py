from setuptools import setup

setup(
    name="pylift",
    version="0.0.1",
    py_modules=["lib.commands"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "pylift = lib.commands:cli",
        ]
    },
)
