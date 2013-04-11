from pyramid.view import view_config
from .models import MyModel


@view_config(context=MyModel, renderer='templates/bibliotekdk.pt')
@view_config(route_name='home.frontpage', renderer='templates/bibliotekdk.pt')
def my_view(request):
    return {'project': 'Ping',
            'search_path': '/search',
            'search_form_method': 'GET'}
