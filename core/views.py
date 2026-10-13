from django.shortcuts import render, redirect
from .models import Salary, Expense, Saving


def dashboard(request):
    salaries = Salary.objects.all().order_by('-date_added')
    total_salary = sum([s.amount for s in salaries])
    total_expense = sum([e.amount for e in Expense.objects.all()])
    total_saving = total_salary - total_expense

    context = {
        'salaries': salaries,
        'total_salary': total_salary,
        'total_expense': total_expense,
        'total_saving': total_saving,
        'expenses': Expense.objects.all()
    }
    return render(request, 'dashboard.html', context)


def add_salary(request):
    if request.method == 'POST':
        month = request.POST.get('month')
        amount = request.POST.get('amount')
        s = Salary.objects.create(month=month, amount=amount)
        Saving.objects.create(salary=s, total_expenses=0, saved_amount=amount)
        return redirect('/')
    return render(request, 'add_salary.html')


def add_expense(request):
    if request.method == 'POST':
        salary_id = request.POST.get('salary')
        category = request.POST.get('category')
        desc = request.POST.get('description')
        amount = request.POST.get('amount')
        salary = Salary.objects.get(id=salary_id)
        Expense.objects.create(salary=salary, category=category, description=desc, amount=amount)
        return redirect('/')
    salaries = Salary.objects.all()
    return render(request, 'add_expense.html', {'salaries': salaries})
