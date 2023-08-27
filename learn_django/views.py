
"""
to render html page
"""
from django.http import HttpResponse
name='abhishek'
def home_view(request):
    """
    take a html string and return html response"""
    print(10*10)
    html_string = f"""
    <h1> hello {name} </>
    """

    return HttpResponse(html_string)