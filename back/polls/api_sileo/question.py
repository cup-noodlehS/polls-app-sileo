from sileo.sileo.resource import Resource
from sileo.sileo.fields import ResourceTypeConvert, ResourceModelManager
from sileo.sileo.registration import register
# from sileo.sileo.fields import ResourceMethodField
# from .choice import ChoiceResource
from polls.models import Question
from polls.forms import QuestionForm

class QuestionResource(Resource):
    query_set = Question.objects.all() #scope of the resource

    #methods allowed
    allowed_methods = [
        'get_pk', 'filter', 'create', 'update', 'delete'
    ]

    #data that you will send to the font-end
    fields = [
        'pk', 'question_text',
        ResourceTypeConvert('pub_date', str),
        # ResourceMethodField('fullname', method_name='get_full_name') #making a field from field(s) in the model
        # ResourceModelManager('choices', resource=ChoiceResource)
    ]
    
    #accessing post methods
    update_filter_fields = ['pk']
    delete_filter_fields = ['pk']
    filter_fields = ['pk']

    #number of instances
    size_per_request = 50

    #form
    form_class = QuestionForm

#register(namespace=appname, resource name, class resource, version {v1: web, v2: android, v3: desktop})
register('polls', 'questions', QuestionResource, version='v1')
