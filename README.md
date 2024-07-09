```bash
CUDA_VISIBLE_DEVICES=2,3 python -m vllm.entrypoints.openai.api_server \
--host 0.0.0.0 \
--port 1155 \
--model ../../../..//LLM_models/english/models--lmsys--vicuna-7b-v1.5/snapshots/vicuna-7b-v1.5/ \
--dtype auto \
--api-key token-abc123 \
--tensor-parallel-size 2 \
--chat-template ./vicuna_template.jinja
```

```bash
CUDA_VISIBLE_DEVICES=0,1,2,3 python server.py \
--host 0.0.0.0 \
--port 8080 \
--model_path ../../../..//LLM_models/english/models--lmsys--vicuna-7b-v1.5/snapshots/vicuna-7b-v1.5/
```


```bash
python attacker.py \
--template vicuna \
--template_idx  1 \
--instruction hhh \
--instruction_idx 0 \
--input empty \
--input_idx 0 \
--model_name vicuna_7b
```

 # empty, prefix_injection