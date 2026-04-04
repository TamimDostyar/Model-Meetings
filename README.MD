This is just a test to see how different models if were human would react in an acutal based meetings. 

For this test I am using free models from two well-known sources such as Ollama and Groq.

You can use any models but I would recommend using something large for leaders and something average to engineers to see how they react. I have ran and tested and the example can be found in `output.md`.

You will need to get your ollama models pulled in your machine and and get the api keys - for reference please review `ex-env.sh`.
Ensure you have Ollama installed.

Ollama: <b>`https://docs.ollama.com/api/introduction`</b><br>
Groq: `https://console.groq.com/docs/overview`


Create your virtual enviroments and install the libraries. Once done, then ensure you have all the api keys with model names added in the .env. Below are a few steps you may initiate to run the sopftware.

- To install required libraries:
    `pip install -r requirements txt`

- To pull models in ollama:
    `Ollama pull <model-name>`

- To run the app:
    `python app.py`
