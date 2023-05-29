# Nifty-Bridge-AI

This app is an AI assistant that answers questions related to the Terms of Service.

## Quick Start

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install --requirement requirements.txt
```

## .env

```shell
API_KEY=
OPENAI_API_KEY=
```

## Launch

To start the application you need to generate an API key
```shell
python3 utils.py
```
Then copy the key and paste it into the API_KEY variable in the .env
After that we start the server for the API
```shell
uvicorn api:app --reload
```

Use ```/send``` endpoint to send question to the bot.
Documentation is available on ```/docs```
