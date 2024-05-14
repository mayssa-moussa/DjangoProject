from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from livre.models import Book, Student,Borrowing,Author
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('book-list')  # Rediriger vers la page d'accueil après la connexion

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'authors']
    template_name ='book-create.html'
    success_url = reverse_lazy('book-list')

class BookListView(ListView):
    model = Book
    template_name = 'book-list.html'
    context_object_name = 'books'


    def get_queryset(self):
        queryset = super().get_queryset()
        date_borrowed = self.request.GET.get('date_borrowed')  # Récupérer la date empruntée depuis les paramètres GET

        if date_borrowed:  # Vérifier si la date empruntée est présente dans la requête
            queryset = queryset.filter(date_borrowed=date_borrowed)  # Filtrer les emprunts par date empruntée

        return queryset
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'authors']
    template_name ='book-update.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')
    template_name = 'book_confirm_delete.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'surname']
    template_name ='student-create.html'
    success_url = reverse_lazy('student-list')

class StudentListView(ListView):
    model = Student
    template_name = 'student-list.html'
    context_object_name = 'students'
    paginate_by = 10  # Nombre d'étudiants par page

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'surname']
    template_name ='student-update.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')
    template_name = 'student_confirm_delete.html'
class BorrowingCreateView(CreateView):
    model = Borrowing
    fields = ['student', 'book', 'date_borrowed', 'book_returned']
    template_name = 'borrowing-create.html'
    success_url = '/borrowings/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        context['books'] = Book.objects.all()
        return context
class BorrowingListView(ListView):
    model = Borrowing
    template_name = 'borrowing-list.html'
    context_object_name = 'borrowings'
class BorrowingUpdateView(UpdateView):
    model = Borrowing
    fields = ['student', 'book', 'date_borrowed', 'book_returned']
    template_name = 'borrowing-update.html'
    success_url = '/borrowings/'
class BorrowingDeleteView(DeleteView):
    model = Borrowing
    template_name = 'borrowing_confirm_delete.html'
    success_url = reverse_lazy('borrowing-list')        
class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'surname']
    template_name ='author-create.html'
    success_url = reverse_lazy('author-list')

class AuthorListView(ListView):
    model = Author
    template_name = 'author-list.html'
    context_object_name = 'authors'
class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'surname']
    template_name = 'author-update.html'
    success_url = '/authors/'
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author-list')  
def borrowing_search(request):
  start_date = request.GET.get('start_date')
  end_date = request.GET.get('end_date')
  date_borrowed = request.GET.get('date_borrowed')  # Add this line

  if start_date and end_date:
    borrowings = Borrowing.objects.filter(date_borrowed__range=[start_date, end_date])
  elif start_date:
    borrowings = Borrowing.objects.filter(date_borrowed__gte=start_date)
  elif end_date:
    borrowings = Borrowing.objects.filter(date_borrowed__lte=end_date)
  # Add elif block for single-date search
  elif date_borrowed:
    borrowings = Borrowing.objects.filter(date_borrowed=date_borrowed)
  else:
    borrowings = Borrowing.objects.all()
  context = {'borrowings': borrowings}
  return render(request, 'borrowing-list.html', context)