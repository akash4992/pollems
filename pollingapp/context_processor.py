from pollingapp.models import Question
def polls_count(request):
    count = Question.objects.count()
    return {"poll_count":count}