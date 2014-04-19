from distutils.core import setup

setup(name='pbf_kao_gui',
      version='.2',
      description="Programmer's Best Friend Utility Extension for the KaoGUI Python Library",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf_kao_gui', 'pbf_kao_gui.Commands', 'pbf_kao_gui.templates'],
      package_data = {'pbf_kao_gui.templates':['*']},
     )