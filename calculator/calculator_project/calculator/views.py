

# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Calculation
# import re
# import json

# def calculator(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             expression = data.get('expression', '')

#             # Validate input to allow only numbers and basic operators
#             if not re.match(r'^[\d\+\-\*/\(\)\. ]+$', expression):
#                 return JsonResponse({'error': 'Invalid input'})

#             result = eval(expression)  # Caution: eval() can be unsafe, consider safer alternatives
#             Calculation.objects.create(expression=expression, result=str(result))
#             return JsonResponse({'expression': expression, 'result': result})
#         except Exception as e:
#             return JsonResponse({'error': 'Calculation error'})

#     history = Calculation.objects.all().order_by('-timestamp')[:10]
#     return render(request, "index.html", {"history": history})

from django.shortcuts import render
from django.http import JsonResponse
from .models import Calculation
import json
import re

def calculator(request):
    if 'history' not in request.session:
        request.session['history'] = []

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            expression = data.get('expression', '')

            # Validate input to allow only numbers and basic operators
            if not re.match(r'^[\d\+\-\*/\(\)\. ]+$', expression):
                return JsonResponse({'error': 'Invalid input'})

            result = eval(expression)  # Caution: eval() can be unsafe
            Calculation.objects.create(expression=expression, result=str(result))

            # Update session history
            request.session['history'].append({'expression': expression, 'result': str(result)})
            request.session.modified = True  # Mark session as changed
            
            return JsonResponse({'expression': expression, 'result': result, 'history': request.session['history']})
        except Exception:
            return JsonResponse({'error': 'Calculation error'})

    history = request.session.get('history', [])
    return render(request, "index.html", {"history": history})

def clear_history(request):
    if request.method == "POST":
        request.session['history'] = []  # Clear only session history
        request.session.modified = True  # Save session changes
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)
