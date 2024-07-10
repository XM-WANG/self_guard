# SELF-GUARD: Empower the LLM to Safeguard Itself (In development)

### Checklist:
We will not release the data containing harmful content. The following is a checklist of the content that will be made public:
- [ ] Guidelines for constructing stage 1 training data.
- [ ] Guidelines for constructing stage 2 training data.
- [ ] Checkpoints of the model trained using the self-guard strategy.
- [ ] Testing script.
- [ ] Training script.
- [x] Typical Jailbreak attack instructions.
- [ ] Wild Jailbreak, XSTest, Open LLM Leadboard testing guidelines.
- [ ] Guidelines for obtaining HarmfulQ, Alpaca, and other data.


### Evaluation

#### Start the LLM as a service 

Here are two methods available. The first one is to deploy the service using the [vllm](https://github.com/vllm-project/vllm) inference framework. The advantage of this approach is faster inference speed, although it has not been verified whether the results obtained through vllm inference are consistent with those obtained using the huggingface framework. The second method is to deploy the service using the huggingface API: this method is used in the experimental part of the paper, but it is less efficient.

Execute the following command to start a vllm service.

```bash
python -m vllm.entrypoints.openai.api_server \
--api-key dummy \
--host 0.0.0.0 \
--port 1155 \
--model ./path/to/vicuna-7b-v.15/ \
--dtype auto \
--tensor-parallel-size 1 \
--chat-template ./data_tool/empty.jinja
```

If you encounter difficulties installing vllm, you can execute the following command to start a service based on the huggingface API.

```bash
python server.py \
--host 0.0.0.0 \
--port 1155 \
--model ./path/to/vicuna-7b-v.15/
```

#### Attacking!!!
```bash
python attacker.py \
--template vicuna \
--instruction empty \
--input start_injection \
--llm_service_address http://127.0.0.1:1155/llm_service/ \
--model_name vicuna_7b
```
Note: If you start the vllm service, set `llm_service_address` to `http://127.0.0.1:1155/v1/`; if you start the service based on the Hugging Face API, set `llm_service_address` to `http://127.0.0.1:1155/llm_service/`.

### Ethic Statement
This work focuses on enhancing the safety of LLMs through fine-tuning. Our primary objective is to make a positive contribution to society by improving the safety of open-source LLMs. We meticulously manage the release of data and code, ensuring they adhere to the highest ethical norms, to maintain a balance between information dissemination and ethical compliance. We employed ten publicly available attack instructions, sourced from open forums or existing research works. Given that these attack methods are already in the public domain, we conducted a thorough evaluation and concluded that the public use of these widely known instructions has limited negative dissemination effects. On the contrary, drawing from current research, consolidating and summarizing these attacks will prove beneficial for systematically enhancing the safety of LLMs in the future, promoting the forward development in the field of LLM safety. Furthermore, it can enhance the coherence, readability, and reproducibility of this work. Regarding the harmful data synthetically generated in this experiment, due to its potential offensive and harmful impact on readers, we have decided not to disclose it at this stage after careful consideration.
For the same reasons, we will not release any original model output results, except for edited and controlled qualitative examples.

### Cite Us

    @inproceedings{wang-etal-2024-self,
        title = "{SELF}-{GUARD}: Empower the {LLM} to Safeguard Itself",
        author = "Wang, Zezhong  and
        Yang, Fangkai  and
        Wang, Lu  and
        Zhao, Pu  and
        Wang, Hongru  and
        Chen, Liang  and
        Lin, Qingwei  and
        Wong, Kam-Fai",
        editor = "Duh, Kevin  and
        Gomez, Helena  and
        Bethard, Steven",
        booktitle = "Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)",
        month = jun,
        year = "2024",
        address = "Mexico City, Mexico",
        publisher = "Association for Computational Linguistics",
        url = "https://aclanthology.org/2024.naacl-long.92",
        pages = "1648--1668",
        abstract = "With the increasing risk posed by jailbreak attacks, recent studies have investigated various methods to improve the safety of large language models (LLMs), mainly falling into two strategies: safety training and safeguards. Safety training involves fine-tuning the LLM with adversarial samples, which activate the LLM{'}s capabilities against jailbreak. However, it is not always effective in countering new attacks and often leads to potential performance degradation. Safeguards, on the other hand, are methods using additional models to filter harmful content from the LLM{'}s response. Nevertheless, they can only reduce a limited amount of harmful output and introduce extra computational costs. Given the distinct strengths and weaknesses of both, we combine them to balance out their flaws and propose a more effective method called Self-Guard.Specifically, we train the LLM to review its responses for any harmful content and append a [harmful] or [harmless] tag to the end of the response. In this way, Self-Guard possesses the advantages of safety training, leveraging the powerful capabilities of the LLMs themselves to detect harmfulness. Besides that, it gains flexibility like safeguards, making the safety check target the output side, which makes the system less vulnerable to attack updates. Experimental results indicate that our Self-Guard can effectively defend against jailbreak attacks and will not cause LLMs{'} performance degradation.",
    }