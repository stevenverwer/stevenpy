import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
  name = 'stevenpy',         # How you named your package folder (MyLib)
  packages = ['stevenpy'],   # Chose the same as "name"
  version = '0.0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Parallel Pooling Batch Document Processor',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Steven Verwer',                   # Type in your name
  author_email = 'stevenverwer@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/stevenverwer/stevenpy',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['PARALLEL POOLING', 'MULTI CORE', 'PDF', 'SCRAPER', 'PDFMINER', 'PDFMINER.SIX'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pdfminer.six',
          'pathlib',
          'os',
          'tqdm',
          'math',
          'multiprocessing',
          'csv',
          're',
          'io',          
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)