from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

async def query_deepseek(query, cisco_output, answer_format):
    deepseek_api = os.getenv('DEEPSEEK_API')
    client = OpenAI(api_key=deepseek_api, base_url="https://api.deepseek.com")
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": f"""
                {query}
                {cisco_output}
                
                {answer_format}
            """},
        ],
        stream=False
    )
    
    return response.choices[0].message.content.strip().split('\n')