import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='builton-sdk',
      version='0.2.1',
      description='BuiltOn Python SDK',
      long_description=long_description,
      long_description_content_type="text/markdown",
      keywords='builton api sdk ai',
      url='https://github.com/BuiltonDev/python-sdk',
      author='BuiltOn',
      author_email='hello@builton.dev',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
          'requests',
      ],
      setup_requires=["pytest-runner"],
      tests_require=['pytest', 'pytest-mock'],
      project_urls={
          "Bug Tracker": "https://github.com/BuiltonDev/python-sdk/issues",
          "Documentation": "https://docs.builton.dev"
      },
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.0",
          "Programming Language :: Python :: 3.1",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      python_requires=">=2.7",
      zip_safe=False)
