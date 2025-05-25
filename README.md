# MaisGestorHealth

Análise Inteligente de Consultas Médicas em Formato SOAP.

## Configuração

1. Crie um arquivo `.env` copiando o `.env.example`:
```bash
cp .env.example .env
```

2. Configure suas secrets no arquivo `.streamlit/secrets.toml`:
```toml
[api]
gemini_api_key = "sua_api_key_aqui"  # Obtenha em https://aistudio.google.com/app/apikey

[app]
name = "MaisGestorHealth"
version = "2.0"
description = "Análise Inteligente de Consultas Médicas em Formato SOAP"

[model]
model_name = "gemini-2.5-flash-preview-05-20"
response_mime_type = "text/plain"

[ui]
page_title = "MaisGestorHealth"
layout = "centered"
logo_path = "logo.png"

[security]
sensitive_data = true
```

3. Certifique-se que os arquivos `.env` e `.streamlit/secrets.toml` estão no `.gitignore` para manter suas credenciais seguras.

## Executando o Aplicativo

```bash
streamlit run app.py
```

## Formato SOAP

O aplicativo analisa transcrições de consultas médicas e organiza as informações no formato SOAP:

- **S**ubjetivo: Sintomas e queixas relatadas pelo paciente
- **O**bjetivo: Sinais vitais, exame físico e dados observáveis
- **A**valiação: Diagnóstico ou hipótese diagnóstica
- **P**lano: Tratamento, exames complementares e orientações

## Recursos

- Análise automatizada usando IA (Google Gemini)
- Interface intuitiva para entrada da transcrição
- Formatação clara em seções SOAP
- Download do resultado em formato de texto
- Processamento seguro das informações
