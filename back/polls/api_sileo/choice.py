from sileo.sileo.resource import Resource
from sileo.sileo.fields import ResourceTypeConvert, ResourceModelManager, ResourceModel
from polls.models import Choice
from polls.forms import ChoiceForm
from sileo.sileo.registration import register
from .question import QuestionResource

class ChoiceResource(Resource):
    query_set = Choice.objects.all()
    allowed_methods = [
        'get_pk', 'filter', 'create', 'update', 'delete'
    ]

    fields = [
        'pk', 'choice_text', 
        ResourceTypeConvert('pub_date', str),
        ResourceModel("question", resource=QuestionResource),
        'votes'
        # ResourceModelManager('choices', resource=ChoiceResource)
    ]
    
    update_filter_fields = ['pk']
    delete_filter_fields = ['pk']
    filter_fields = ['pk','question']
    size_per_request = 50
    form_class = ChoiceForm

register('polls', 'choices', ChoiceResource, version='v1')
