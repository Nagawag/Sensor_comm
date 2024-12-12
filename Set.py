from setuptools import setup, find_packages

setup(
    name="mqtt-base-client",  # Name of your library
    version="0.1.0",          # Initial version
    description="A simple MQTT client wrapper for IoT systems",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/mqtt-base-client",  # Repository URL
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=["paho-mqtt"],  # Dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
