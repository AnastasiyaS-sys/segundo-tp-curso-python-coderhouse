from setuptools import setup, find_packages

setup(
    name='mi_paquete_compras',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'compras = main:main'
        ]
    },
    author='Nastya',
    description='Sistema de clientes para página de compras usando POO',
)
