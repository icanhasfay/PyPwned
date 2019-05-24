from setuptools import setup

setup(
    name="pypwned",
    packages=["pypwned"],
    package_dir={"pypwned": "pypwned"},
    version="0.1.7",
    description="A Python client for the HaveIBeenPwned REST API",
    long_description=open("README.md").read() + "\n\n" + open("CHANGES.rst").read(),
    author="Eric Fay",
    author_email="icanhasfay@gmail.com",
    url="https://github.com/icanhasfay/PyPwned",
    license="MIT",
    install_requires=["requests"],
    long_description_content_type="text/markdown",
    classifiers=(
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Topic :: Security",
    )
)
