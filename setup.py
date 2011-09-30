from distutils.core import setup

setup(
    name="schemutt",
    version="0.1",
    provides=["schemutt"],
    author="Steve Johnson",
    author_email="steve@steveasleep.com",
    url="http://github.com/irskep/schemutt",
    description='XML schema figure-outer',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    packages=["schemutt"],
    scripts=['bin/schemutt'],
    long_description="""schemutt - an XML schema figure-outer"""
)

