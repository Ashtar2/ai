import ollama
import uvicorn
from fastapi import FastAPI, HTTPException

from models.generate_request import GenerateRequest

app = FastAPI()


@app.post("/generate")
async def generate_text(request: GenerateRequest):
    try:
        options = {
            "temperature": request.temperature,
        }

        # deepseek-r1:14b
        response = ollama.chat(
            model="gemma3:12b",
            messages=[{"role": "user", "content": request.prompt}],
            options=options,
        )

        return {"response": response["message"]["content"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    return {"status": "ok"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
