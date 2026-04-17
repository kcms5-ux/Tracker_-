from django.shortcuts import render
from .models import Study
 
 
def study_list(request):
    studies = Study.objects.all()
 
    total_count = studies.count()
    total_minutes = sum(study.total_minutes for study in studies)
    total_hours = total_minutes // 60
    remain_minutes = total_minutes % 60
 
    context = {
        'studies': studies,
        'total_count': total_count,
        'total_hours': total_hours,
        'remain_minutes': remain_minutes,
    }
    return render(request, 'study/study_list.html', context)