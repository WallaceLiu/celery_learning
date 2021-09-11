from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='canvas_kaboom',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=[
          'celery>=3.1.0',
          'librabbitmq',
          'redis',
      ],
      entry_points="""
      [console_scripts]
      canvas_kaboom=canvas_kaboom:main
      """,
      )
