from setuptools import setup

setup(
    name="spdclient",
    version="0.1",
    description="Python Wrapper for Scrapyd WebServie",
    long_description="It is a Python Wrapper for Scrapyd WebService for easy use of Scrapyd API",
    author="Kanchan Sapkota",
    author_email="kanchansapkota27@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="scrapyd scrapy python scrapydapi scrapyd-client api",
    packages=["spd-client"],
    zip_safe=False,
)
