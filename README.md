# 🏥 MedSOAP Analyzer

Uma aplicação web moderna para análise inteligente de consultas médicas e conversão automática para o formato SOAP usando Google Gemini AI.

## 📋 Sobre o Projeto

O MedSOAP Analyzer é uma ferramenta que utiliza inteligência artificial para analisar transcrições de consultas médicas e organizá-las automaticamente no formato SOAP (Subjetivo, Objetivo, Avaliação, Plano), facilitando a documentação médica.

## ✨ Funcionalidades

- 🤖 **Análise por IA**: Utiliza o Google Gemini 2.5 para análise inteligente
- 📝 **Formato SOAP**: Organização automática em formato médico padrão
- 🎯 **Interface Simples**: Design limpo e intuitivo
- 💾 **Download de Resultados**: Exportação em formato texto
- 🔒 **Segurança**: Configuração segura via variáveis de ambiente

## 🚀 Como Usar

### 1. Configuração Inicial

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd MaisGestorHealthGen
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure a API Key do Google Gemini:
   - Copie o arquivo `.env.example` para `.env`
   - Obtenha sua API Key em: https://aistudio.google.com/app/apikey
   - Edite o arquivo `.env` e adicione sua chave:
```
GEMINI_API_KEY=sua_api_key_aqui
```

### 2. Executando a Aplicação

```bash
streamlit run app.py
```

A aplicação será aberta em seu navegador no endereço `http://localhost:8501`

### 3. Usando o Sistema

1. **Cole a Transcrição**: Insira a transcrição completa da consulta médica
2. **Clique em Analisar**: O sistema processará automaticamente com IA
3. **Visualize o SOAP**: Os resultados serão organizados nas 4 seções
4. **Baixe o Resultado**: Use o botão de download para salvar

## 📊 Formato SOAP

O sistema organiza as informações em:

- **🗣️ SUBJETIVO**: Sintomas e queixas relatadas pelo paciente
- **🔍 OBJETIVO**: Sinais vitais, exame físico e dados observáveis  
- **🎯 AVALIAÇÃO**: Diagnóstico ou hipótese diagnóstica
- **📋 PLANO**: Tratamento, medicações, exames e orientações

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit**: Interface web
- **Google Gemini AI**: Processamento de linguagem natural
- **Python-dotenv**: Gerenciamento de variáveis de ambiente

## 📁 Estrutura do Projeto

```
MaisGestorHealthGen/
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências Python
├── .env.example          # Template de configuração
├── .env                  # Configurações (não versionado)
├── .gitignore           # Arquivos ignorados pelo Git
├── README.md            # Documentação
├── logo.png             # Logo da aplicação
└── exemplo-consulta.txt # Exemplo de uso
```

## 🔒 Segurança

- A API Key é armazenada em variáveis de ambiente
- O arquivo `.env` é ignorado pelo Git
- Não há exposição de credenciais na interface

## 🎯 Exemplo de Uso

**Entrada (Transcrição):**
```
Médico: Boa tarde! Como posso ajudá-lo hoje?
Paciente: Doutor, estou com uma dor de cabeça muito forte há 3 dias...
```

**Saída (Formato SOAP):**
- Organização automática em seções estruturadas
- Identificação de sintomas, sinais vitais, diagnósticos
- Plano de tratamento e orientações

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## 🆘 Suporte

Para suporte ou dúvidas, abra uma issue no repositório do projeto.

---

**Desenvolvido para profissionais de saúde • Powered by Google Gemini**
