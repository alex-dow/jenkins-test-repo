from setuptools import setup, find_packages

setup(name='jtr',
      version='0.0.1',
      description='Jenkins Test Repo',
      url='https://github.com/alex-dow/jenkins-test-repo',
      author='Alex Dow',
      author_email='adow@psikon.com',
      license='MIT',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      zip_safe=False
)
