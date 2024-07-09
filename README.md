# SELF-GUARD: Empower the LLM to Safeguard Itself (In development)

### Checklist:

- [ ] Guidelines for constructing stage 1 training data.
- [ ] Guidelines for constructing stage 2 training data.
- [ ] Checkpoints of the model trained using the self-guard strategy.
- [ ] Testing script.
- [ ] Training script.
- [x] Typical Jailbreak attack instructions.
- [ ] Wild Jailbreak, XSTest, Open LLM Leadboard testing guidelines.
- [ ] Guidelines for obtaining HarmfulQ, Alpaca, and other data.

```bash
CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server \
--chat-template ./vicuna_template.jinja
--dtype auto \
--host 0.0.0.0 \
--port 1155 \
--model ./path/to/vicuna-7b-v.15/ \
--tensor-parallel-size 4 \
```

```bash
CUDA_VISIBLE_DEVICES=0,1,2,3 python server.py \
--host 0.0.0.0 \
--port 1155 \
--model_path ./path/to/vicuna-7b-v.15/
```


```bash
python attacker.py \
--template vicuna \
--instruction empty \
--input empty \
--model_name vicuna_7b
```