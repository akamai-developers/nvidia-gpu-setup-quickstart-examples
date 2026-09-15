from vllm import LLM, SamplingParams

model = "Qwen/Qwen3-0.6B"

llm = LLM(model=model)

sampling_params = SamplingParams(
    temperature=0.7,
    max_tokens=100
)

prompt = "Explain what a GPU is in one sentence."

outputs = llm.generate([prompt], sampling_params)

print("Prompt:", prompt)
print("Response:", outputs[0].outputs[0].text)