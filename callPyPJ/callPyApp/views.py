# callPyApp/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .encrypt import encrypt_func
from .decrypt import decrypt_func

class encryptView(TemplateView):
    template_name = "encrypt.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        if 'data_input' in request.POST:
            data_input = request.POST['data_input']
            encrypted_result, key_result = encrypt_func(data_input)

            response_data = f'<p class="result">Encryption: {encrypted_result}</p><p class="key">Key: {key_result}</p>'
            return HttpResponse(response_data)

        return render(request, self.template_name)

class decryptView(TemplateView):
    template_name = "decrypt.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if 'data_input' in request.POST:
            data_input = request.POST['data_input']
            decrypted_result = decrypt_func(data_input)

            response_data = f'<p class="decrypted_result">Decryption: {decrypted_result}</p>'
            return HttpResponse(response_data)

        return render(request, self.template_name)
