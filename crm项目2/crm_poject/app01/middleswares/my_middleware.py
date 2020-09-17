
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,reverse
from app01 import models
class Authmiddle(MiddlewareMixin):
    def process_request(self,request):
        if request.path_info in [reverse('app01:login'),reverse('app01:register')]:
            return
        if request.path_info.startswith('/admin'):
            return
        if not request.session.get('is_login'):
            return redirect(reverse('app01:login'))
        request.user_obj = models.UserProfile.objects.filter(username=request.session.get('username')).first()