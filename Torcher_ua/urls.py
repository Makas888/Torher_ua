from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view, registration_view, logout_view, activate, \
                           password_recovery_view, password_reset_view, password_reset_confirm

urlpatterns = [
    path('', include('home_page.urls', namespace='home_page')),
    path('admin/', admin.site.urls),
    path('send_email/', include('send_email.urls', namespace='send_email')),
    path('product/', include('product.urls', namespace='product')),
    path('about_as/', include('about_as.urls', namespace='about_as')),
    path('contacts/', include('contacts_page.urls', namespace='contacts')),
    path('news_latter/', include('news_letter_form.urls', namespace='news_latter')),
    path('captcha/', include('captcha.urls')),
    path('manager/', include('manager.urls', namespace='manager')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('unsubscribe/<email_pk>/', include('unsubscribe.urls', namespace='unsubscribe')),
    path('coupons/', include('coupons.urls', namespace='coupons')),

    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('password_recovery', password_recovery_view, name='password_recovery'),
    path('password_reset/', password_reset_view, name='password_reset'),
    path('reset/<uidb64>/<token>', password_reset_confirm, name='password_reset_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
