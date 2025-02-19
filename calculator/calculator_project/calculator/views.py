# from django.shortcuts import render,HttpResponse
# from django.http import JsonResponse
# from .models import Calculation
# import re

# def calculator(request):
#     if request.method == "POST":
#         expression = request.POST.get('expression', '')
        
#         # Validate input to prevent code injection
#         if not re.match(r'^[\d\+\-\*/\(\)\. ]+$', expression):
#             return JsonResponse({'error': 'Invalid expression'})

#         try:
#             result = eval(expression)
#             Calculation.objects.create(expression=expression, result=result)
#             return JsonResponse({'expression': expression, 'result': result})
#         except Exception as e:
#             return JsonResponse({'error': 'Calculation error'})

#     calculations = Calculation.objects.all().order_by('-timestamp')[:10]
#     return render(request, "index.html", {"calculations": calculations})
#     # return HttpResponse("this")

# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Calculation
# import re

# def calculator(request):
#     if request.method == "POST":
#         expression = request.POST.get('expression', '')

#         # ✅ Validate input to prevent errors
#         if not re.match(r'^[\d\+\-\*/\(\)\. ]+$', expression):
#             return JsonResponse({'error': 'Invalid input'})

#         try:
#             result = eval(expression)
#             Calculation.objects.create(expression=expression, result=result)
#             return JsonResponse({'expression': expression, 'result': result})  # ✅ Return JSON response
#         except Exception:
#             return JsonResponse({'error': 'Calculation error'})

#     # ✅ Fetch last 10 calculations for history
#     history = Calculation.objects.all().order_by('-timestamp')[:10]
#     return render(request, "calculator/index.html", {"history": history})


# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Calculation
# import re

# def calculator(request):
#     if request.method == "POST":
#         expression = request.POST.get('expression', '')

#         # Validate input to allow only numbers and basic operators
#         if not re.match(r'^[\d\+\-\*/\(\)\. ]+$', expression):
#             return JsonResponse({'error': 'Invalid input'})

#         try:
#             result = eval(expression)
#             Calculation.objects.create(expression=expression, result=str(result))
#             return JsonResponse({'expression': expression, 'result': result})
#         except Exception as e:
#             return JsonResponse({'error': 'Calculation error'})

#     history = Calculation.objects.all().order_by('-timestamp')[:10]
#     return render(request, "index.html", {"history": history})


from django.shortcuts import render
from django.http import JsonResponse
from .models import Calculation
import re
import json

def calculator(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            expression = data.get('expression', '')

            # Validate input to allow only numbers and basic operators
            if not re.match(r'^[\d\+\-\*/\(\)\. ]+$', expression):
                return JsonResponse({'error': 'Invalid input'})

            result = eval(expression)  # Caution: eval() can be unsafe, consider safer alternatives
            Calculation.objects.create(expression=expression, result=str(result))
            return JsonResponse({'expression': expression, 'result': result})
        except Exception as e:
            return JsonResponse({'error': 'Calculation error'})

    history = Calculation.objects.all().order_by('-timestamp')[:10]
    return render(request, "index.html", {"history": history})
