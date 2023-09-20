from sileo.sileo.resource import Resource
from sileo.sileo.fields import ResourceTypeConvert, ResourceModelManager
from polls.models import Question
from polls.forms import QuestionForm
from sileo.sileo.registration import register
# from .choice import ChoiceResource

class QuestionResource(Resource):
    query_set = Question.objects.all()
    allowed_methods = [
        'get_pk', 'filter', 'create', 'update', 'delete'
    ]

    fields = [
        'pk', 'question_text',
        ResourceTypeConvert('pub_date', str),
        # ResourceModelManager('choices', resource=ChoiceResource)
    ]
    
    update_filter_fields = ['pk']
    delete_filter_fields = ['pk']
    filter_fields = ['pk']
    size_per_request = 50
    form_class = QuestionForm

register('polls', 'questions', QuestionResource, version='v1')
