import cohere
import re

from src.audioGenerate import gerar_audio

def com_cohere(tema, keywords):

    co = cohere.Client('')

    caminho = './src/prompt_model.txt'
          
    # Lê arquivo de texto padrão
    with open(caminho, 'r') as file:
        prompt = file.read()

    # Crie uma entrada com a formatação correta, incluindo as palavras-chave
    keywords_str = ", ".join(keywords)  # Converte a lista de palavras-chave em uma string
    entrada = f"""Input:

    Theme: {tema}
    Key Words: {keywords_str}
    Exact number of Lines: 12

    What is the expected output?
    """

    prompt = prompt + entrada

    response = co.generate(
        prompt=prompt,  # Use a entrada formatada, não a string literal
    )

    # Use uma expressão regular para encontrar o texto entre os marcadores "```"
    match = re.search(r'```(.*?)```', response[0], re.DOTALL)

    lyrics = match.group(1)  # Obtém o conteúdo entre os marcadores "```"

    gerar_audio(lyrics.strip())

    return (lyrics.strip())
