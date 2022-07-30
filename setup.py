from setuputil import *

setuptools.setup(
    name=projectname,
    version=version,
    author="k. goger",
    author_email=f"k.r.goger+{projectname}@gmail.com",
    url=f"https://github.com/kr-g/{projectname}",
    packages=setuptools.find_packages(exclude=[]),
    include_package_data=True,
    install_requires=install_requires,
    python_requires=python_requires,
)

# python3 -m setup sdist build bdist_wheel

# test.pypi
# twine upload --repository testpypi dist/*
# python3 -m pip install --index-url https://test.pypi.org/simple/ gitonic --extra-index-url https://pypi.org/simple/
# python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps gitonic

# pypi
# twine upload dist/*
