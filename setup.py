from setuptools import setup, find_packages


install_requires = [
    'PIL'
]

setup(
    name="facecrap",
    version="0.1",
    author="Quant",
    packages=find_packages(),
    setup_requires=['nose'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'facecrap = facecrap:handler',
        ],
    }
)
