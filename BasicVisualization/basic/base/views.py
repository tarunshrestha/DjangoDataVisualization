from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def chart_view(request):
    # Example data, can be fetched from your database or API
    labels = ['January', 'February', 'March', 'April']
    data = [12, 19, 3, 5]

    # Pass data to the template
    return render(request, 'chart_page.html', {
        'labels': labels,
        'data': data
    })