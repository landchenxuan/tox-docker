from setuptools import setup

setup(
    name="tox-docker",
    description="Launch a docker instance around test runs",
    maintainer="Dan Crosta",
    maintainer_email="dcrosta@late.am",
    install_requires=[
        "docker>=2.3.0,<3.0",
        "tox>=2.7.0,<3.0",
    ],
    py_modules=["tox_docker"],
    entry_points={"tox": ["docker = tox_docker"]},
    setup_requires=["vcversioner"],
    vcversioner={"version_module_paths" : ["_version.py"]},
)