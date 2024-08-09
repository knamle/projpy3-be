from django.urls import path
from . import views

#BACKEND PRETTY MUCH 'DONE', UNABLE TO ACCESS PAGES THAT REQUIRE LOGIN

urlpatterns = [
    #path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    #path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path("product/create/", views.ProductCreateView.as_view(), name="create-product"),
    path("product/view/", views.ProductListView.as_view(), name="product-list"),
    path("product/delete/<int:pk>/", views.ProductDeleteView.as_view(), name="delete-product")
]