from setuptools import setup, find_packages

setup(
    name="see_docker",
    version="0.1",
    packages=find_packages(),
    author="retrodaredevil",
    author_email="retrodaredevil@gmail.com",
    description="A CLI Python program to help you understand your Docker infrastructure a little better ",
    url="https://github.com/retrodaredevil/see-docker",
    entry_points={
        "console_scripts": [
            "see-docker = see_docker:do_see_docker",
        ],
    },
    install_requires=["wheel", "docker==6.1.3"]
)
