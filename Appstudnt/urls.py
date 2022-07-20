from Appstudnt import views
from django.urls import path


urlpatterns = [
    path('',views.addStudent,name='addStudent'),
    path('add_student_details',views.add_student_details,name='add_student_details'),
    path('show_students',views.show_students,name='show_students'),

    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('show/<int:pk>',views.show,name='show'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
    path('load_index_page',views.load_index_page,name='load_index_page'),
]