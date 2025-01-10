from setuptools import setup

setup(
    name='taskd',
    version='1.0.0',
    py_modules=["app"],
    entry_points={
        'console_scripts': [
            'hello-world = app:main',
        ]
    },
    python_requires=">=3.12.3"
)