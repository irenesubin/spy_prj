from django.shortcuts import render 
from django.http import JsonResponse 
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from .utils import spy_shellcode_with_openai

import openai
import os

# OpenAI API 키 설정
openai.api_key = settings.OPENAI_API_KEY

def get_completion(prompt): 
	print(prompt) 
	query = openai.ChatCompletion.create( 
		messages=[
        	{'role':'user','content': prompt}
    	], 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5, 
	) 
	response = query.choices[0].message["content"]
	print(response) 
	return response 


def query_view(request): 
	if request.method == 'POST': 
		prompt = request.POST.get('prompt') 
		prompt=str(prompt)
		response = get_completion(prompt)
		return JsonResponse({'response': response}) 
	return render(request, 'index.html')