import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model(model_name='gpt2'):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    return model, tokenizer

def generate_response(message, model, tokenizer, max_length=100, temperature=0.7, top_k=50, top_p=0.9):
    inputs = tokenizer.encode(message, return_tensors="pt")
    
    # Ensure pad_token_id is defined, if not, set to eos_token_id
    pad_token_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id

    # Generate the response with better control over repetition and variability
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=pad_token_id,
        attention_mask=torch.ones(inputs.shape, dtype=torch.long, device=inputs.device),
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

model, tokenizer = load_model()

def generate_dungeon_master_response(user_input, model, tokenizer, max_length=150, temperature=0.7, top_k=50, top_p=0.9):
    prompt = (
        "You are a Dungeon Master guiding a group of adventurers through an epic quest. "
        "Respond to the adventurers' actions and queries with rich, detailed descriptions and narrative. "
        f"Adventurer: {user_input}\nDungeon Master: "
    )
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Ensure pad_token_id is defined, if not, set to eos_token_id
    pad_token_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id

    # Generate the response with better control over repetition and variability
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=pad_token_id,
        attention_mask=torch.ones(inputs.shape, dtype=torch.long, device=inputs.device),
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract the Dungeon Master's part of the response
    response_split = response.split("Dungeon Master: ", 1)
    if len(response_split) > 1:
        response = response_split[1].strip()

    return response

