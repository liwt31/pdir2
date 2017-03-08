from setuptools import setup


setup(name='pdir2',
      version='0.0.1',
      description='Pretty dir printing with joy',
      author='laike9m',
      author_email='laike9m@gmail.com',
      url='',
      packages=['pdir', ],
      install_requires=[
          'colorama',
          'enum34;python_version<"3.4"',
      ],
      )