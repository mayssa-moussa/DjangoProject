from django.contrib import admin
from django.urls import path
from livre import views
from livre.views import BookCreateView,BookListView,StudentCreateView,StudentListView,BorrowingCreateView,BorrowingListView,RegisterView, LoginView,AuthorCreateView,AuthorListView

urlpatterns = [
     path('', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('create/', BookCreateView.as_view(), name='book-create'),  # Utilise la vue 'BookCreateView'
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('createStudent/', StudentCreateView.as_view(), name='student-create'),  # Utilise la vue 'BookCreateView'
    path('students/',StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),
    path('createBorrowing/', BorrowingCreateView.as_view(), name='borrowing-create'),  # Utilise la vue 'BookCreateView'
    path('borrowings/',BorrowingListView.as_view(), name='borrowing-list'),
    path('borrowings/<int:pk>/update/', views.BorrowingUpdateView.as_view(), name='borrowing-update'),
    path('borrowings/<int:pk>/delete/', views.BorrowingDeleteView.as_view(), name='borrowing-delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
     path('createAuthor/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/', AuthorListView.as_view(), name='author-list'),  
    path('books/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author-update'),
    path('books/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),   
    path('students/search/', StudentListView.as_view(), name='student-search'),
    #path('borrowings/search/', BorrowingListView.as_view(), name='borrowing-search'),
    path('borrowing-search/', views.borrowing_search, name='borrowing-search'),
]




