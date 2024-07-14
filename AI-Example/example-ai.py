import openai
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel, pipeline

####
note_pad = "note_pad.db"

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

tokenizer.pad_token = tokenizer.eos_token

model = TFGPT2LMHeadModel.from_pretrained('gpt2')



try:
    text = "what is the size of my penis?"
    encoded_input = tokenizer(text, return_tensors='tf')
    output = model.generate(encoded_input['input_ids'], attention_mask=encoded_input['attention_mask'], max_length=80, num_return_sequences=1)
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=False)
    print(decoded_output)
except Exception as error: 
    print(f"Error durante la generacion de texto {error}")