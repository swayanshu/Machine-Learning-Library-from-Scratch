from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='summary_classification',
  version='0.0.1',
  description='Basic metrics for evaluating classification results',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGElog.txt').read(),
  url='',  # the URL of your package's home page e.g. github link
  author='Swayanshu Shanti Pragnya',
  author_email='swayanshu1997@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='summary, F1 score, accuracy, confusion matrix, FDR', 
  packages=find_packages(),
  install_requires=[''] # a list of other Python modules which this module depends on.  For example RPi.GPIO
)