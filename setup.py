from setuptools import setup

setup(
    name = 'grover_controlled_diffuser',
	packages = ['grover_controlled_diffuser'],
    version = '1.1',
	license = 'Apache-2.0',
    description = 'Grover controlled-diffuser (CUs)',
    author = 'Ali Al-Bayaty',
	author_email = 'albayaty@pdx.edu',
    url = 'https://github.com/albayaty/',
    download_url = 'https://github.com/albayaty/grover_controlled_diffuser/',
	keywords = ['quantum computing', 'quantum algorithm', 'Grover\'s algorithm', 'diffusion operator'],
    classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache 2.0 License',
		'Operating System :: POSIX :: Linux :: Windows',
        'Programming Language :: Python',
		'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
		'Programming Language :: Python :: 3.12',
    ],
    install_requires = [],
)
