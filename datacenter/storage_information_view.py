from datacenter.models import Visit
from django.shortcuts import get_list_or_404, render


def storage_information_view(request):
    non_closed_visits = []
    people_in_storage = get_list_or_404(Visit, leaved_at=None)
    for person in people_in_storage:
        view_info = {
            'who_entered': person.passcard.owner_name,
            'entered_at': person.entered_at,
            'duration': person.format_duration(),
        }
        non_closed_visits.append(view_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
