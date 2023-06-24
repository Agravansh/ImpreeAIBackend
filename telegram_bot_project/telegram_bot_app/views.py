from django.shortcuts import render
from .models import User, ButtonCall

# Create your views here.
def user_statistics(request):
    users = User.objects.all()
    statistics = []

    for user in users:
        button_calls = ButtonCall.objects.filter(user=user)
        total_calls = button_calls.aggregate(Sum('count')).get('count__sum', 0)
        statistics.append({
            'user': user,
            'total_calls': total_calls,
            'button_calls': button_calls
        })

    return render(request, 'user_statistics.html', {'statistics': statistics})

