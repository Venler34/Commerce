from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.createListing, name="createListing"),
    path("view/<int:id>", views.viewListing, name="viewListing"),
    path("comment/<int:id>", views.commentListing, name="commentListing"),
    path("addWatchList/<int:id>/<str:username>", views.addWatchlist, name="addWatchList"),
    path("removeWatchList/<int:id>/<str:username>", views.removeWatchList, name="removeWatchList"),
    path("closeListing/<int:id>", views.closeListing, name="closeListing"),
    path("watchlist/<str:username>", views.watchlist, name="watchlist"),
    path("categories", views.getCategories, name="categories"),
    path("viewCategory/<str:category>", views.viewCategory, name="viewCategory")
]
