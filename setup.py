from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='batbelt',
      version='0.1',
      description='Useful things like grapple gun and batarangs',
      url='http://github.com/jenkspt/batbelt',
      author='Penn',
      author_email='jenkspt@gmail.com',
      license='MIT',
      packages=['batbelt'],
      install_requires=['pytest', 'requests'],
      include_package_data=True,
      zip_safe=False)