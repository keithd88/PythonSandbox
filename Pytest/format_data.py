
def format_data_for_display(people):
    people_display = []
    for person in people:
        people_display.append(f'{person['given_name']} {person['family_name']}: {person['title']}')

    return people_display

def format_data_for_excel(people):
    people_excel = f'given,family,title\n'
    for person in people:
        people_excel += f'{person['given_name']},{person['family_name']},{person['title']}\n'

    return people_excel
