import requests
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import WebShellcode, LinuxShellcode, WindowsShellcode  # 메인 서버의 모델을 임포트

# Ollama 서버에 요청하는 함수
def get_completion(prompt):
    url = 'http://localhost:11434/api/generate'
    headers = {'Content-Type': 'application/json'}
    
    data = {
        'model': 'llama3',
        'prompt': prompt,
        'options': {
            'temperature': 0.5,
            'max_tokens': 1024
        }
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_data = response.json()
        return response_data.get('text', '')  # 분석 결과 텍스트 반환
        
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# WebShellcode AI 분석 요청
def web_shellcode_detail(request, shellcode_id):
    shellcode = get_object_or_404(WebShellcode, pk=shellcode_id)  # 메인 서버 모델 사용
    if request.method == 'POST':
        decrypted_content = shellcode.content
        analysis_result = get_completion(decrypted_content)
        shellcode.analysis_result = analysis_result
        shellcode.save()
        
        return JsonResponse({'message': 'Analysis completed', 'analysis_result': analysis_result})
    
    return render(request, 'web_shellcode_detail.html', {'shellcode': shellcode})

# LinuxShellcode AI 분석 요청
def linux_shellcode_detail(request, shellcode_id):
    shellcode = get_object_or_404(LinuxShellcode, pk=shellcode_id)
    if request.method == 'POST':
        decrypted_content = shellcode.content
        analysis_result = get_completion(decrypted_content)
        shellcode.analysis_result = analysis_result
        shellcode.save()
        
        return JsonResponse({'message': 'Analysis completed', 'analysis_result': analysis_result})
    
    return render(request, 'linux_shellcode_detail.html', {'shellcode': shellcode})

# WindowsShellcode AI 분석 요청
def windows_shellcode_detail(request, shellcode_id):
    shellcode = get_object_or_404(WindowsShellcode, pk=shellcode_id)
    if request.method == 'POST':
        decrypted_content = shellcode.content
        analysis_result = get_completion(decrypted_content)
        shellcode.analysis_result = analysis_result
        shellcode.save()
        
        return JsonResponse({'message': 'Analysis completed', 'analysis_result': analysis_result})
    
    return render(request, 'windows_shellcode_detail.html', {'shellcode': shellcode})

from django.shortcuts import render

def index_view(request):
    # index.html 파일을 렌더링함
    return render(request, 'index.html')
