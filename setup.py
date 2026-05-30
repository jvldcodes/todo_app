from setuptools import setup

setup(
    name="todo",
    version="0.1",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "todo=main:run",  # This says: command 'todo' calls function 'run' in 'main.py'
        ],
    },
)
