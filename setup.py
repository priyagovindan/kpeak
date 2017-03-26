from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name = 'mountainplotlib',
      version = '0.1',
      description = 'The python package for k-peak decomposition and mountain plot visualization.',
      long_description = readme(),
      classifiers=[
        'Development Status :: 1 - Beta',
        'License :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Graph Mining :: Network Analysis',
      ],
      keywords = 'k-peak mountain plot graph mining',
      url = 'http://github.com/storborg/funniest',
      author = 'Flying Circus',
      author_email = 'flyingcircus@example.com',
      license = 'MIT',
      packages = ['mountainplotlib'],
      install_requires = [
          'networkx', 'matplotlib '
      ],
      include_package_data=True,
      zip_safe=False)