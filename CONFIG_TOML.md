# Configuração em Formato TOML

Este projeto agora suporta configuração usando o formato TOML (Tom's Obvious, Minimal Language), que é mais estruturado e legível que arquivos `.env`.

## 🔧 Como Configurar

### 1. Criando o arquivo de configuração

Copie o arquivo de exemplo:
```bash
copy config.toml.example config.toml
```

### 2. Editando as configurações

Abra o arquivo `config.toml` e configure suas chaves:

```toml
[api]
# Google Gemini API Configuration
# Obtenha sua API Key em: https://aistudio.google.com/app/apikey
gemini_api_key = "AIzaSy...sua_api_key_aqui"

[app]
# Configurações da aplicação
name = "MaisGestorHealth"
version = "2.0"
description = "Análise Inteligente de Consultas Médicas em Formato SOAP"

[model]
# Configurações do modelo de IA
model_name = "gemini-2.5-flash-preview-05-20"
response_mime_type = "text/plain"

[ui]
# Configurações da interface
page_title = "MaisGestorHealth"
layout = "centered"
logo_path = "logo.png"

[security]
# Configurações de segurança
sensitive_data = true
```

## 📋 Vantagens do TOML

### Comparação: .env vs TOML

**Arquivo .env (formato antigo):**
```env
GEMINI_API_KEY=AIzaSyB-vXA8JHCzDe2cAf88L4gKehb5qqXVa0U
PAGE_TITLE=MaisGestorHealth
MODEL_NAME=gemini-2.5-flash-preview-05-20
```

**Arquivo TOML (formato novo):**
```toml
[api]
gemini_api_key = "AIzaSyB-vXA8JHCzDe2cAf88L4gKehb5qqXVa0U"

[ui]
page_title = "MaisGestorHealth"

[model]
model_name = "gemini-2.5-flash-preview-05-20"
```

### Benefícios do TOML:

1. **🗂️ Organização**: Agrupa configurações relacionadas em seções
2. **📖 Legibilidade**: Sintaxe mais clara e hierárquica
3. **🔧 Flexibilidade**: Suporta tipos de dados nativos (strings, números, arrays, booleanos)
4. **📝 Comentários**: Comentários mais organizados por seção
5. **🛡️ Validação**: Estrutura mais fácil de validar
6. **🔄 Reutilização**: Fácil de compartilhar configurações entre ambientes

## 🔐 Segurança

- O arquivo `config.toml` está incluído no `.gitignore`
- Use sempre o arquivo `config.toml.example` como modelo
- Nunca commite o arquivo `config.toml` com dados reais
- Mantenha suas API keys seguras

## 🚀 Executando a Aplicação

Após configurar o `config.toml`:

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
streamlit run app.py
```

## 🔄 Migração do .env para TOML

Se você estava usando o arquivo `.env`, suas configurações foram migradas automaticamente. O sistema agora lê exclusivamente do arquivo TOML.

Para manter compatibilidade, você pode manter ambos os arquivos, mas o TOML terá prioridade.

## ⚠️ Troubleshooting

### Erro: "config.toml não encontrado"
- Certifique-se de que o arquivo `config.toml` existe na pasta raiz
- Copie o arquivo de exemplo: `copy config.toml.example config.toml`

### Erro: "API Key não encontrada"
- Verifique se a chave `gemini_api_key` está preenchida no arquivo `config.toml`
- Confirme que a API key é válida no Google AI Studio

### Erro: "Erro ao carregar config.toml"
- Verifique a sintaxe TOML do arquivo
- Use um validador TOML online se necessário
- Certifique-se de que as strings estão entre aspas duplas

---

**Configuração moderna e organizada para o MaisGestorHealth** 🏥
