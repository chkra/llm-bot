# Simple llm bot demos

## About

This repository shows simple proof-of-concept for two llm-based chat bots:

 First, a simple ChatGPT-based Bot with RAG. We use llama_index to for with data from the website of  <a href="htw-berlin.de"><font color="#76B900">HTW Berlin</font></a>. Right now, the data (found in `./data` contains only a few sentences and was scraped manually. In the demo shown below, we ask specifically for content mentioned in this text file.
Second, we show another simple proof of concept to use ChatGPT as an ad-hoc code writer for an interactive analytics tool. We create JavaScript code based on user input, and execute it client side to analyse client side data. This code was inspired by a post by <a href="https://towardsdatascience.com/exploring-data-analysis-via-natural-language-approach-1-224965d1fb16#0ecb"><font color="#76B900">Luciano Abrata</font></a>.
<br><br>

---

HTW Chatbot Demo:
<img src="other/anim1.gif width="50%">

<br><br>
Analytics Bot Demo:
<img src="other/anim2.gif width="50%">

---


## Local Setup

Make environment and setup dependencies:
```
conda create --name htw-bot python=3.11
conda activate htw-bot
pip install -r requirements.txt
```

You need to replace the ChatGPT API Key in `app.py` with your own key to get the code running.

Run Flask demo:
```
python app.py
```
Move to to URL in your browser to see the demo.


## Sources

The following tutorials were used to build this:

* [HowTo Lllama](https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5)
* [HowTo Flask](https://codinginfinite.com/chatbot-in-python-flask-tutorial/)
* [HowTo more Flask with Llama](https://gpt-index.readthedocs.io/en/latest/guides/fullstack_app_guide.html#flask-backend)
* [How to use LLMs to create Code](https://towardsdatascience.com/exploring-data-analysis-via-natural-language-approach-1-224965d1fb16#0ecb)

Also helpful:
* https://github.com/logan-markewich/llama_index_starter_pack
* https://betterprogramming.pub/how-to-build-your-own-custom-chatgpt-with-custom-knowledge-base-4e61ad82427e
* https://beebom.com/how-build-own-ai-chatbot-with-chatgpt-api/