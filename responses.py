import modals

prefix = '.'

def get_response(message : str) -> str:
    p_message = message.lower()

    if p_message == f'{prefix}add project':
        interaction.response.send_modal(project_modal)
        return

    if p_message == f'{prefix}help':
        return '`This will be a help message.`'