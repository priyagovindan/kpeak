from setuptools import setup

def readme():
    with open('README.MD') as f:
        return f.read()

setup(name = 'peaklib',
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
      url = 'https://github.com/lovingmage/mountainplotlib',
      author = 'Priya Govindan, Chenghong Wang and Sucheta Soundarajan',
      author_email = 'cwang132@syr.edu',
      license = 'MIT',
      packages = ['peaklib'],
      install_requires = [
          'networkx', 'matplotlib '
      ],
      include_package_data=True,
      zip_safe=False)