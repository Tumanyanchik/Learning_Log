from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import Http404

# Create your views here.


def check_topic_owner(owner, user):
    """Check that the topic belongs to the current user"""
    if (owner != user):
        raise Http404


def index(request):
    """Home page learning log application"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """All topics list"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Detailed information about 1 topic"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic.owner, request.user)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Determine new theme"""
    if (request.method != 'POST'):
        # Data wasn`t sent; creating new form
        form = TopicForm()
    else:
        # Data was sent; processing data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Output empty or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Entry on a specific topic"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic.owner, request.user)
    if request.method != 'POST':
        # Data wasn`t sent; create empty form
        form = EntryForm()
    else:
        # Data was sent; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # Output empty or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit exist record"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_topic_owner(topic.owner, request.user)

    if request.method != 'POST':
        # Default request; form contain exist record
        form = EntryForm(instance=entry)
    else:
        # Sending data 'POST'; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
