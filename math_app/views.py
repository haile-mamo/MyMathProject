from django.shortcuts import render

def home(request):
    result = None
    if request.method == 'POST':
        # ከ HTML የመጣውን ቁጥር መቀበል
        input_num = request.POST.get('number')
        if input_num:
            try:
                # በ 32 ማባዛት
                result = float(input_num) * 32
                # ውጤቱ የአስርዮሽ ቁጥር ከሆነ እንዲያጥር (.00) ማድረግ
                if result.is_integer():
                    result = int(result)
            except ValueError:
                result = "ስህተት፡ እባክህ ትክክለኛ ቁጥር አስገባ"
                
    return render(request, 'index.html', {'result': result})