import re


def clean_corpus(chat_export_file):
    """Prepara una exportación de chatpara entrenar con chatterbot."""
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus

def get_feedback():

    text = input()

    if 'si' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Por favor, Escriba si o no')
        return get_feedback()

def remove_chat_metadata(chat_export_file):
    """Elimina los metadatos del chat.

    Las exportaciones de chats vienen con metadatos sobre cada mensaje:

     date    time    username  message
    ---------------------------------------
    8/26/22, 17:47 - Jane Doe: Message text

    Esta función elimina todos los metadatos hasta el texto de cada mensaje.

    Args:
        chat_export_file (str): El nombre del archivo de exportación del chat

    Devuelve:
        tuple: El texto de cada mensaje de la conversación
    """
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # e.g. "8/26/22, 17:47"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # e.g. "Jane Doe"
    metadata_end = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_end

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern, "", content)
    return tuple(cleaned_corpus.split("\n"))

def remove_non_message_text(export_text_lines):
    """Elimina el texto irrelevante para la conversación de la exportación del chat.

    Las exportaciones de chat de WhatsApp vienen con una línea de introducción estandarizada
    y una línea vacía al final del archivo.
    Las exportaciones de texto también sustituyen los mensajes multimedia por texto que no es
    relevante para la conversación. Esta función elimina todo eso.

    Args:
        export_text_lines (tuple): Todas las líneas del archivo de exportación

    Devuelve:
        tuple: Mensajes que forman parte relevante de la conversación
    """
    messages = export_text_lines[1:-1]

    filter_out_msgs = ("<Media omitted>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))