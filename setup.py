from setuptools import setup

setup(
    name='project_name',
    version='0.1.0',
    packages=[
        # explicitly list packages, or use find_packages()
        'package_name',
    ],
    setup_requires=[],
    install_requires=[
        'numpy',
    ],
    extras_require={
        'test': [
            'pytest',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/project_name',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)
