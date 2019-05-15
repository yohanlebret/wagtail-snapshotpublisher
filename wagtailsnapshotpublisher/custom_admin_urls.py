from django.urls import path

from . import views


# Override Wagtail paths
app_name = 'wagtailsnapshotpublisher_custom_admin'
urlpatterns = [
    path('pages/<int:page_id>/unpublish/<int:release_id>/', views.unpublish_page, name='unpublish-page-from-release'),
    path('pages/<int:page_id>/unpublish/<int:release_id>/recursively/', views.unpublish_recursively_page, name='unpublish-recursively-page-from-release'),
    path('pages/<int:page_id>/remove/<int:release_id>/', views.remove_page, name='remove-page-from-release'),
    path('pages/<int:page_id>/remove/<int:release_id>/recursively/', views.remove_recursively_page, name='remove-recursively-page-from-release'),

    path('<slug:content_app>/<slug:content_class>/unpublish/<int:content_id>/<int:release_id>/', views.unpublish, name='unpublish-from-release'),
    path('<slug:content_app>/<slug:content_class>/edit/<int:content_id>/preview/<slug:preview_mode>/', views.preview_model, name='preview-model-admin'),

    path('wagtailsnapshotpublisher/wsspcontentrelease/details/<int:release_id>/', views.release_detail, name='release-detail'),
    path('wagtailsnapshotpublisher/wsspcontentrelease/setlive/<int:release_id>/', views.release_set_live, name='release-set-live'),
    path('wagtailsnapshotpublisher/wsspcontentrelease/setlivedetails/<int:release_id>/', views.release_set_live_detail, name='release-set-live-detail'),
    path('wagtailsnapshotpublisher/wsspcontentrelease/archive/<int:release_id>/', views.release_archive, name='release-archive'),
    path('wagtailsnapshotpublisher/wsspcontentrelease/restore/<int:release_id>/', views.release_restore, name='release-restore'),
    path('wagtailsnapshotpublisher/wsspcontentrelease/unfreeze/<int:release_id>/', views.release_unfreeze, name='release-unfreeze'),
]