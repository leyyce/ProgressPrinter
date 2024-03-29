from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
  name='ProgressPrinter',
  packages=['ProgressPrinter'],
  version='0.1.1',
  license='MIT',
  description='Simple library that allows you to add a progress bar to your console output.',
  long_description_content_type='text/markdown',
  long_description=long_description,
  author='Yannic Wehner',
  author_email='yannic.wehner@elcapitan.io',
  url='https://github.com/ElCap1tan/ProgressPrinter',
  download_url='https://github.com/ElCap1tan/ProgressPrinter/archive/v0.1.1.tar.gz',
  keywords=['terminal', 'console', 'shell', 'progress bar'],
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
