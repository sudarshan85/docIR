from setuptools import setup, find_packages
import docIR

setup(
    name='docIR',
    version=docIR.__version__,
    author='Sudarshan Srinivasan',
    author_email='srinivasans@ornl.gov',
    packages=find_packages(include=['docIR', 'docIR.*']),
    install_requires=open('./requirements.txt').readlines(),
    entry_points={
      'console_scripts': [
        'ingest=docIR.ingest.ingest:entry_point',
        'chat=docIR.chat.chat:entry_point',
        ]
      },
    python_requires='>=3.10'
)
