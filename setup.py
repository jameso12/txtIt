from setuptools import find_packages, setup

setup(
    name='textit',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
# to deploy copy th file at dist
# pip install it
# and run:
# $ export FLASK_APP=flaskr
# $ flask init-db

#   581  export FLASK_APP=appT
#   582  export FLASK_ENV=development
#   583  flask run