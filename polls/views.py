from django.utils import timezone

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, CreateView, DeleteView
from polls.forms import CreateForm

from .models import Question, Choice



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    model = Question

    def get_queryset(self):
        # return the last five published questions
        return Question.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:5]
        return Question.objects.order_by('-publication_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class QuestionCreateView(CreateView):
    model = Question
    template_name = 'question_new.html'
    fields = ['question_text', 'publication_date']


class QuestionUpdateView(UpdateView):
    model = Question
    fields = ['question_text']
    template_name = 'question_update_form.html'


class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'question_delete.html'
    success_url = reverse_lazy('index')


class ChoiceUpdateView(UpdateView):
    model = Choice
    fields = ['question', 'choice_text']
    template_name = 'polls/choice_update_form.html'


class ChoiceCreateView(CreateView):
    model = Choice
    fields = ['question', 'choice_text']
    template_name = 'polls/choice_create_form.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "Вы не сделали выбор."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def create_form(request):
    return render(request, 'polls/create_form.html')


def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            name = request.POST['question_name']
            new_question = Question(question_text=name, publication_date=timezone.now())
            new_question.save()
            return HttpResponseRedirect(reverse('polls:success_saved'))
    else:
        form = CreateForm()
        return render(request, "pools/create.html", {'form': form})


def success_saved(request):
    return render('success_saved.html')