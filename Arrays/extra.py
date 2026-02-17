
# i = 1
# n = 8  # Example value for n
# while i < n:
#     for j in range(n):
#         print(i, j)
#     i *= 2


import os

from fastapi import FastAPI, HTTPException
from openai import OpenAI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/generate/")
async def generate_text(prompt: str):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY is not set")

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return {"result": response.choices[0].message.content}
