import setuptools

setuptools.setup(
    name="uml-generator",
    version="0.1.0",
    author="Milind Nair",
    author_email="nairmilind3@ga.com",
    description="A LangChain-based AI agent that converts natural language to UML diagrams (PlantUML)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/milind-nair/uml-generator",
    packages=["uml_generator"],
    package_dir={"": "src"},
    install_requires=[
        "langchain==0.3.27",
        "openai==2.13.0",
        "requests==2.32.5",
        "python-dotenv==1.2.1",
        "plantuml==0.3.0"
    ],
    entry_points={
        "console_scripts": [
            "uml-generator=uml_generator.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    include_package_data=True,
)
