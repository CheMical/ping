from pyramid.view import view_config



@view_config(route_name='search', renderer='templates/bibliotekdk-search.pt')
def search(request):
    attributes = {'project': 'Ping',
                  'search_path': '/search',
                  'search_form_method': 'GET'}

    
    return attributes
