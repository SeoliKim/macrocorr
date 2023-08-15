from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()


setup(
    name = 'macrocorr',
    version = '0.0.2',
    author = 'Seoli Kim',
    author_email = 'seolikim1225@gmail.com',
    description = 'a Python package for analyzing the correlation between macroeconomic indicators and time-series data',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = "https://github.com/SeoliKim/macrocorr",
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    
    keywords = ['economics', 'correlation', 'time-series'],
    license = "MIT",
    packages=find_packages('macrocorr', exclude=['test']),
    setup_requires=['wheel'],
    install_requires=["numpy>=1.23.5", 
                      "pandas>=1.5.2", 
                      "matplotlib>=3.7.2", 
                      "scipy>=1.11.1", 
                      "yfinance>=0.2.26",
                        "wbgapi>=1.0.12"],
    classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Science/Research',      
    'Topic :: Office/Business :: Financial',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
  ],
)