from transformers import pipeline
import torch
from fastapi import FastAPI
import uvicorn
import argparse
from pydantic import BaseModel


class Item(BaseModel):
    prompt: str
    max_new_tokens: int
    do_sample: bool
    temperature: float
    top_p: float
    top_k: int


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str)
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=1155)
    args = parser.parse_args()

    app = FastAPI()
    @app.post("/v1/")
    def generate(payload: Item):
        results = model(
            payload.prompt,
            do_sample=payload.do_sample,
            max_new_tokens=payload.max_new_tokens,
            temperature=payload.temperature,
            top_p=payload.top_p,
            top_k=payload.top_k,
            eos_token_id=model.tokenizer.eos_token_id
        )
        results = results[0]['generated_text']
        return {"responses": results, "prompt": payload.prompt}

    # bnb_config = dict(
    #     load_in_4bit=True,
    #     bnb_4bit_use_double_quant=True,
    #     bnb_4bit_quant_type="nf4",
    #     bnb_4bit_compute_dtype=torch.float16 
    # )

    model = pipeline(
        "text-generation", 
        model=args.model_path, 
        device_map="auto", 
        torch_dtype=torch.float16,
        # attn_implementation="flash_attention_2"
        # model_kwargs=bnb_config
        )

    uvicorn.run(app, host=args.host, port=args.port)
