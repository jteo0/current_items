from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Jeslyn Theodora',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# 'name': 'Katana',
# 'amount': '1',
# 'description': 'A silver blade with a gold-green hilt, approximately two shaku in length. Familiar and reliable. +1 to Shinagami no Hokori and +1 to Savoir Faire.',
# 'type': 'Weapon'