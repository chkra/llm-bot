# Simple Text Based Chat Bot for a Website

## About

This repository shows a simple proof-of-concept for a ChatGPT-based Chat Bot. We use llama_index to fine tune ChatGPT with data from the website of the _Hochschule für Technik und Wirtschaft Berlin_. 

Right now, the data (found in `htw-data/htw-data.txt` contains only a few sentences and was scraped manually (!). In the demo shown below, we ask specifically for content mentioned in this text file.

![Demo of HTW Chat Bot](other/Animation.gif "Demo of HTW Chat Bot")

## Local Setup

Make environment and setup dependencies:
```
conda create --name htw-bot python=3.11
pip install -r requirements.txt
```

You need to replace the ChatGPT API Key in `app.py` with your own key to get the code running. You can request your own API Key [here](https://platform.openai.com/account/api-keys) at OpenAI.

Run Flask demo:
```
python app.py
```
Move to to URL in your browser to see the demo.


## Next steps

This is only a proof of concept, obviously. Several improvements are necessary to gain a production-ready app:
* replace ChatGPT model with offline LLaMA model to proof on-premise capabilities
* scrape information from HTW website to build a suitable knowledge base for `llama_index`.

## Sources

The following tutorials were used to build this:

* HowTo Lllama: https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5
* HowTo Flask: https://codinginfinite.com/chatbot-in-python-flask-tutorial/
* HowTo more Flask with Llama: https://gpt-index.readthedocs.io/en/latest/guides/fullstack_app_guide.html#flask-backend 

Also helpful:
* https://github.com/logan-markewich/llama_index_starter_pack
* https://betterprogramming.pub/how-to-build-your-own-custom-chatgpt-with-custom-knowledge-base-4e61ad82427e
https://beebom.com/how-build-own-ai-chatbot-with-chatgpt-api/