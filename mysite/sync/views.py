from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Participant
from .forms import ParticipantForm
from django.http import HttpResponseRedirect

def index(request):
    form = ParticipantForm()
    return render(request, 'sync/index.html', {'form': form})

def participants(request):
    participant_list = Participant.objects.order_by('-id')
    context = {
        'participant_list': participant_list
        }
    return render(request, 'sync/participants.html', context)

def new_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            p = Participant(name = form.cleaned_data['name'],
                            age = form.cleaned_data['age'],
                            siblings = form.cleaned_data['siblings'],
                            exposures = form.cleaned_data['exposures'],
                            mutations = form.cleaned_data['mutations'])
            p.save()
            return HttpResponseRedirect('/sync/participants')
        else:
            errors = form.errors
            form = ParticipantForm()
            return render(request, 'sync/index.html', {'form_error':errors, 'form': form})

def new_participant_status(request, participant_id, participant_status):
    participant = get_object_or_404(Participant, pk=participant_id)
    participant.status = participant_status
    participant.save()
    return HttpResponseRedirect('/sync/participants')
