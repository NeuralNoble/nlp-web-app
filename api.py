import paralleldots
paralleldots.set_api_key("zX3onRM0xRviTy1PpoeqazXbQXVgRHFVdiYnnXKLpos")

def ner(text):
    ner = paralleldots.ner(text)
    return ner
