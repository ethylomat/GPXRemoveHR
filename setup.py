from setuptools import setup

setup(
    name='GPXRemoveHeartrate',
    version='0.1',
    py_modules=['remove_hr'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        remove-hr=remove_hr:remove_hr
    ''',
)