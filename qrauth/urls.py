# import re
# from django.urls import re_path
# from qrauth import views
# from django.urls import path

# urlpatterns = [
#         re_path(r'^pic/(?P<auth_code>[a-zA-Z\d]{50})/$', views.qr_code_picture, name='auth_qr_code'),
#         re_path(r'^(?P<auth_code_hash>[a-f\d]{40})/$',  views.login_view, name='qr_code_login'),
#         re_path(r'invalid_code/$',  TemplateView.as_view(template_name='qrauth/invalid_code.html'), name='invalid_auth_code'),
#         re_path(r'^$', views.qr_code_page, name='qr_code_page'),
# ]