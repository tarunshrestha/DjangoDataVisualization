from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def chart_view(request):
    # Example data, can be fetched from your database or API
    labels = ['January', 'February', 'March', 'April']
    data = [12, 19, 3, 5]

    pie_labels = ['Red', 'Blue', 'Yellow']
    pie_data = [12, 19, 3]

    # Pass data to the template
    return render(request, 'chart_page.html', {
        'labels': labels,
        'data': data,
        'pie_labels': pie_labels,
        'pie_data': pie_data,
    })