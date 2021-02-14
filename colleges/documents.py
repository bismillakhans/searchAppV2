from elasticsearch_dsl import Index
from django_elasticsearch_dsl import Document,fields
from django_elasticsearch_dsl.registries import registry
from .models import NewCollegeBasicInfo,NewCollegeCollegeCities

# The name of your index
college = Index('colleges')
# See Elasticsearch Indices API reference for available settings
college.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
@college.document
class NewCollegeBasicInfoDocument(Document):
    name = fields.TextField(
        attr='college_name',
        fields={
            'suggest': fields.Completion(),
        }
    )
    city_name = fields.TextField(fields={
            'suggest': fields.Completion(),
        })

    def prepare_city_name(self, instance):
        try:
            city_text=NewCollegeCollegeCities.objects.get(id=instance.city)
        except NewCollegeCollegeCities.DoesNotExist:
            city_text=None
        if city_text:
            return city_text.city
        return "default"

    class Django:
        model = NewCollegeBasicInfo
        fields = [
            'id',
            'college_name',
        ]

    queryset_pagination = 50

