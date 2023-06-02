from setuptools import setup, find_packages

setup(
    name="wordpress-auth",
    version="0.1.0",
    author="Keyvan Hardani",
    author_email="hello@keyvan.ai",
    description="A Python package that provides WordPress authentication for Streamlit applications.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Keyvanhardani/streamlit-wordpress-authentication",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
    python_requires='>=3.8',
    install_requires=[
        'streamlit',
        'requests'
    ],
)
