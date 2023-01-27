prefix = '.'

def get_response(message : str) -> str:
    p_message = message.lower()

    if p_message == f'{prefix}add project':
        return 'Add Project Test.'

    if p_message == f'{prefix}help':
        return '`This will be a help message.`'