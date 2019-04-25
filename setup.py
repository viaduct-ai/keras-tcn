from setuptools import setup

setup(
    name='keras-tcn',
    version='2.6.7.1',
    description='Keras TCN',
    author='Philippe Remy + Vincent D',
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    packages=['tcn'],
    # manually install tensorflow or tensorflow-gpu
    install_requires=['numpy',
                      'keras']
)
