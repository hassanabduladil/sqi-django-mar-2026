from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'freelancer/index.html')

def blog_view(request):
    return render(request, 'freelancer/blog.html')

def services_view(request):
    services = ["Data Analysis", "Web Dev", "Data Science", "Software Engr.", "Cybersecurity"]

    context =  {'services': services, 'name': "TOBI dada" }
    return render(request, 'freelancer/services.html', context)

def testimonials_view(request):

    testimonials = {
        'tobi': "Django is stressful",
        "jon": "Django is a shortcut",
        "francis": "Django is dynamic"
    }


    return render(request, 'freelancer/testimonials.html', {'testimonials': testimonials})


