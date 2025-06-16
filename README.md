# Langchain_QnA : QnA with OpenAI

A simple Langchain + Streamlit application to interact with OpenAI models and get responses to your questions in real-time.

## 🚀 Features

- Choose between OpenAI's `gpt-3.5-turbo` and the older `text-davinci-003` model.
- Get answers to any questions using Langchain's intuitive interface.
- Easy-to-use Streamlit front-end.

## ⚠️ Important Notice

> **The `text-davinci-003` model is deprecated and should no longer be used.**  
> Please use the **`gpt-3.5-turbo`** model for best results and continued support.

## 🛠️ Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone git@github.com:dotdotsg/Langchain_QnA.git
   cd Langchain_QnA
    ```


   
2. **Create and Activate a Virtual Environment**

```bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Create a .env File**

Create a .env file in the root of your project and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_paid_openai_api_key_here
```
Note: Make sure you're using a paid-tier API key.
Using a free-tier key or one that has exceeded its quota will result in the following error:
```
openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

```


Running the App
```
streamlit run app.py
```

Once launched, open the browser and interact with the UI to:

Select a model

Enter a question

View the OpenAI-generated response

## 🧰 Tech Stack
🛠️ Langchain

🌐 Streamlit

🤖 OpenAI API

🔐 python-dotenv


## 📝 Notes
✅ The app is optimized for use with gpt-3.5-turbo.

🔐 Never commit your .env file or share your OpenAI API key.

🚧 text-davinci-003 is included for legacy support only.

