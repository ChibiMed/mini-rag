# mini-rag

This is a minimal project of the RAG model fro asking documents and fils.

# Requirements

- Python 3.8 or later

#### Install Python using MiniConda

1) Download and install Miniconda 

2) Create a new environment using the following command :

```bash
$ conda create -n mini-rag-app python=3.8
```

3) activate the environment:
```bash
$ conda activate mini-rag-app
```

## Installation

### Installation the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.exemple .env
```

Set your environment variables in `.env` file. Like 
`OPENAI_API_KEY` value.