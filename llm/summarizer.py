"""
# summarizer.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load model once
tokenizer = AutoTokenizer.from_pretrained("Falconsai/medical_summarization")
model = AutoModelForSeq2SeqLM.from_pretrained("Falconsai/medical_summarization")
summarizer = pipeline("text2text-generation", model=model, tokenizer=tokenizer)


# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
summarizer = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
"""
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

summarizer = pipeline("text2text-generation", model="google/flan-t5-large")

def get_medical_summary(prompt_text: str):
    result = summarizer(
        prompt_text,
        max_length=512,
        min_length=150,
        do_sample=True,                # Enable sampling for more varied output
        temperature=0.7,               # Introduce controlled randomness
        top_k=50,                      # Use top-k sampling to restrict to best tokens
        top_p=0.95,                    # Nucleus sampling
        repetition_penalty=1.5         # Penalize repeated phrases
    )
    return result[0]['generated_text']
