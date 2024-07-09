# SELF-GUARD: Empower the LLM to Safeguard Itself

```bash
CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server \
--host 0.0.0.0 \
--port 1155 \
--model ../../../../../LLM_models/english/models--lmsys--vicuna-7b-v1.5/snapshots/vicuna-7b-v1.5/ \
--dtype auto \
--api-key token-abc123 \
--tensor-parallel-size 4 \
--chat-template ./vicuna_template.jinja
```

```bash
CUDA_VISIBLE_DEVICES=0,1,2,3 python server.py \
--host 0.0.0.0 \
--port 1155 \
--model_path ../../../../../LLM_models/english/models--lmsys--vicuna-7b-v1.5/snapshots/vicuna-7b-v1.5/
```


```bash
python attacker.py \
--template vicuna \
--instruction empty \
--input empty \
--model_name vicuna_7b
```