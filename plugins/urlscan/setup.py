# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="urlscan-rapid7-plugin",
      version="4.0.1",
      description="Analyze URLs for malicious indicators using the URLScan website scanner",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_urlscan']
      )
