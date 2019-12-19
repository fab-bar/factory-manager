from setuptools import setup, find_packages

setup(
    name='factory-manager',
    author='Fabian Barteld',
    author_email='fabian.barteld@rub.de',
    url="https://github.com/fab-bar/factory-manager",
    version='0.1.0',
    python_requires='>=3.6',
    packages=find_packages(),
    install_requires=['typing-inspect'],
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)
