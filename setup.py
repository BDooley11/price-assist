from setuptools import setup

requirements = [requests,bs4,xlxwriter,xlrb,time]

setup(name="priceAssist",
      version="0.1",
      description="used car price check from done deal",
      url="",
      author="Barry Dooley",
      author_email="barry.dooley@ucd.ie",
      licence="GPL3",
      packages=['priceAssist'],
      install_requires=requirements,
      entry_points={
        'console_scripts':['run_priceAssist=priceAssist.main:main']
        }
      )
