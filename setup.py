from setuptools import find_packages, setup
from sphinx.setup_command import BuildDoc

cmdclass = {'build_sphinx': BuildDoc}
name = 'ZenossAPIClient'
version = '0.1'
release = '0.1.0'

setup(name=name,
      version=release,
      description='Zenoss API client module',
      url='https://github.com/Zuora-TechOps/ZenossAPIClient.git',
      author='Mark Troyer',
      author_email='disco@zuora.com',
      license='Apache',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      zip_safe=False,
      cmdclass=cmdclass,
      command_options={
          'build_sphinx': {
              'project': ('setup.py', name),
              'version': ('setup.py', version),
              'release': ('setup.py', release),
          }
      },
      setup_requires=[
          'pytest-runner>=2.12.1',
      ],
      tests_require=[
          'pytest>=3.2.3',
          'pytest-responses>=0.3.0',
      ],
      install_requires=[
          'python-dateutil>=2.6.1',
          'requests>=2.18.4',
          'urllib3>=1.22',
      ]
      )
