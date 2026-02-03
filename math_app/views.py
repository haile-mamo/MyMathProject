from django.shortcuts import render, redirect # redirect እዚህ ጋር ተጨምሯል
from .models import Calculation

# 1. ዋናው ገጽ (ለማስላት እና ዝርዝር ለማየት)
def index(request):
    if request.method == "POST":
        n_text = request.POST.get('num_x')
        user_note = request.POST.get('note_text')
        
        if n_text:
            n = int(n_text)
            c = n * 32
            # መረጃውን በዳታቤዝ ውስጥ መመዝገብ
            Calculation.objects.create(number=n, result=c, note=user_note)
        
        # ስሌቱ ተሰርቶ ሲያልቅ ገጹን እንደገና እንዲጭነው (Refresh) ያደርጋል
        return redirect('/eee/')
    
    # ሁሉንም መረጃ በቅደም ተከተል ያመጣል
    all_data = Calculation.objects.all().order_by('-id')
    return render(request, "math.html", {"all_data": all_data})

# 2. ለማጥፋት የሚያገለግል ፈንክሽን
def delete_item(request, item_id):
    # መታወቂያ ቁጥሩን (ID) በመጠቀም መረጃውን መፈለግ
    item = Calculation.objects.get(id=item_id)
    # መረጃውን ማጥፋት
    item.delete()
    # ወደ ዋናው ገጽ መመለስ
    return redirect('/eee/')