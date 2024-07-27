import openai
from nltk.tokenize import word_tokenize
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel, pipeline

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.pad_token = tokenizer.eos_token
model = TFGPT2LMHeadModel.from_pretrained('gpt2')
summarizer = pipeline('summarization', model="facebook/bart-large-cnn")
def tokenize_text(texto):
    tokens= tokenizer.tokenize(texto)
    token_count= len(tokens)
    return token_count

def generar_resumen(texto, token_count):
    token_count= tokenize_text(texto)
    try:
        if token_count<100:
            resumen = summarizer(texto, max_length=int(token_count*0.5), min_length=int(token_count*0.25), do_sample=False)
            return resumen
        elif token_count<300:
            resumen = summarizer(texto, max_length=int(token_count*0.35), min_length=int(token_count*0.20), do_sample=False)
            print (token_count)
            return resumen
        elif token_count>300:
            resumen = summarizer(texto, max_length=int(token_count*0.25), min_length=int(token_count*0.15), do_sample=False)
            return resumen
    except Exception as error:
        print(f"Ocurrió un error al momento de resumir el texto: {error}")
def generar_texto(texto):
    try:
        encoded_input = tokenizer(texto, return_tensors='tf')
        output = model.generate(encoded_input['input_ids'], attention_mask=encoded_input['attention_mask'], max_length=80, num_return_sequences=1)
        decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
        return decoded_output
    except Exception as error:
        print(f"Ocurrió un error al generar texto: {error}")

