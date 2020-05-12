from setuptools import setup, find_packages

setup(
    name="project_template",
    version="0.0.1",
    description="Python template",
    python_requires=">=3.6",
    author="Mozilla IT Enterprise Systems",
    author_email="bsieber@mozilla.com",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[],
    project_urls={"Source": "https://github.com/mozilla-it/python-library-template",},
    test_suite="tests.bdd",
    data_files=[],
)
