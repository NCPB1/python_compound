from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'calculation/index.html')

def calculate_profit(request):
    if request.method == "POST":
        try:
            # Get form data
            monthly_invest =float(request.POST.get('monthly_invest'))
            
            roi = float(request.POST.get('roi'))/100
            tenure_in_months = int(request.POST.get('tenure'))

            # Investment calculation logic
            invest1 = monthly_invest
            for i in range(1, tenure_in_months+1):
                monthly_invest = monthly_invest + (roi * monthly_invest) + invest1
            overall_profit = round(monthly_invest, 2)
            

            # Return the result
            return JsonResponse({"overall_profit": overall_profit})

        except Exception as e:
            return JsonResponse({"error": str(e)})
    return JsonResponse({"error": "Invalid request method"})

