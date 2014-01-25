from distutils.core import setup

setup(name='pbf.kao_gui',
      version='.1',
      description="Programmer's Best Friend Utility Extension for Kao_gui",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf.kao_gui', 'pbf.kao_gui.Commands', 'pbf.kao_gui.templates'],
      package_data = {'pbf.kao_gui.templates':['*']},
     )