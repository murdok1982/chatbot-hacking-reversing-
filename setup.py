from setuptools import setup, find_packages

setup(
    name="chatbot-hacking-reversing",
    version="0.2.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langchain>=0.1.0",
        "langchain-ollama>=0.0.1",
        "langchain-community>=0.0.10",
        "python-dotenv>=1.0.0",
        "pytest>=7.0.0",
    ],
    extras_require={
        "dev": ["pytest-cov>=4.0"],
    },
    entry_points={
        "console_scripts": [
            "h4ckbot=chatbot.main:chat_loop",
        ],
    },
    python_requires=">=3.8",
)
