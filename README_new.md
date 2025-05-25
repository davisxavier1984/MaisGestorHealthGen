# MedSOAP Analyzer

Sistema inteligente para análise de consultas médicas no formato SOAP (Subjetivo, Objetivo, Avaliação, Plano) usando IA do Google Gemini.

## 🩺 Funcionalidades

- **Análise SOAP Automática**: Converte transcrições de consultas em formato SOAP estruturado
- **Interface Moderna**: Aplicação web com Streamlit
- **IA Médica**: Utiliza Google Gemini 2.0 Flash para análise inteligente
- **Configuração Segura**: API Key via arquivo .env
- **Logo Personalizada**: Interface com logo.png personalizada
- **Sugestões Clínicas**: Gera diagnósticos diferenciais e planos terapêuticos
- **Exportação**: Download da análise em formato texto
- **Contador de Análises**: Estatísticas de uso em tempo real

## 🚀 Instalação e Configuração

### Aplicação Streamlit (Recomendado) ⭐

1. **Prepare o ambiente:**
   ```bash
   git clone <repository-url>
   cd MaisGestorHealthGen
   ```

2. **Configure a API Key:**
   - Obtenha sua API Key em: [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Edite o arquivo `.env` e substitua `your_api_key_here` pela sua API Key:
   ```env
   GEMINI_API_KEY=AIzaSy...sua_api_key_aqui
   ```

3. **Execute a aplicação:**
   - **Windows**: Duplo clique em `start_streamlit.bat`
   - **Manual**:
     ```bash
     pip install -r requirements.txt
     streamlit run app.py
     ```

4. **Acesse:** http://localhost:8501

### Versões Alternativas

#### Servidor Python HTTP
- **Windows**: Duplo clique em `start.bat`
- **Manual**: `python server.py`
- **Acesso**: http://localhost:8000

#### Frontend Estático (HTML)
- Abra o arquivo `index.html` diretamente no navegador
- Configure a API Key pela interface web

## 📝 Como Usar

### 1. Análise de Consulta (Streamlit)
1. Cole a transcrição da consulta médico-paciente no campo de texto
2. Clique em "🧠 Analisar Consulta"
3. Aguarde o processamento (alguns segundos)
4. Visualize os resultados organizados por seções SOAP coloridas

### 2. Recursos Adicionais
- **📋 Exemplo**: Carrega uma consulta de exemplo automaticamente
- **📄 Baixar Análise**: Download da análise completa em formato texto
- **🔄 Nova Análise**: Limpa os resultados para uma nova consulta
- **📊 Estatísticas**: Contador de análises realizadas na sessão

### 3. Exemplo de Transcrição
Veja o arquivo `exemplo-consulta.txt` para um exemplo completo.

```
Médico: Boa tarde! Como posso ajudá-lo hoje?
Paciente: Doutor, estou com uma dor de cabeça muito forte há 3 dias...
```

## 🛠️ Tecnologias Utilizadas

- **Frontend**: Streamlit, HTML5, CSS3, JavaScript
- **Backend**: Python, HTTP Server  
- **IA**: Google Gemini 2.0 Flash API
- **Configuração**: python-dotenv
- **Interface**: Pillow (PIL) para logo

## 📁 Estrutura do Projeto

```
MaisGestorHealthGen/
├── app.py                  # Aplicação Streamlit principal ⭐
├── index.html              # Interface HTML alternativa
├── server.py               # Servidor Python HTTP
├── logo.png                # Logo da aplicação
├── .env                    # Configurações (API Key)
├── requirements.txt        # Dependências Python
├── start_streamlit.bat     # Script de inicialização Streamlit ⭐
├── start.bat              # Script de inicialização servidor HTTP
├── exemplo-consulta.txt   # Exemplo de transcrição
└── README.md              # Documentação
```

## 🎨 Interface Streamlit

A nova aplicação Streamlit oferece:

- **🖼️ Logo Personalizada**: Exibe logo.png no topo da aplicação
- **🎨 Design Médico**: Cores e ícones temáticos da área médica
- **📱 Responsivo**: Interface adaptável para diferentes tamanhos de tela
- **⚙️ Sidebar**: Configurações e estatísticas em painel lateral
- **🔄 Estado Persistente**: Mantém dados durante a sessão
- **📊 Métricas**: Contador de análises e informações do modelo

## 🔒 Segurança

- ✅ API Key armazenada em arquivo .env (não versionado)
- ✅ Validação de entrada e tratamento de erros robusto
- ✅ Interface segura com Streamlit
- ✅ Configuração automática de dependências

## 🆘 Resolução de Problemas

### Erro: "API Key não configurada"
- Verifique se a API Key está correta no arquivo `.env`
- Confirme que obteve a API Key em: https://aistudio.google.com/app/apikey

### Erro: "Streamlit não encontrado"
- Execute: `pip install -r requirements.txt`
- Verifique se o Python está instalado

### Erro: "Logo não encontrada"
- Verifique se `logo.png` está na pasta raiz
- A aplicação funcionará sem a logo (ícone de fallback)

### Erro: "Porta em uso"
- Streamlit: `streamlit run app.py --server.port 8502`
- Servidor HTTP: Modifique a porta no `server.py`

## ⚠️ Considerações Médicas

> **ATENÇÃO**: Este sistema é uma ferramenta de apoio educacional e não substitui o julgamento clínico profissional.

### Limitações
- Não substitui avaliação médica presencial
- Sugestões devem ser validadas pelo profissional
- Limitado à qualidade da transcrição fornecida

### Uso Responsável
- Use apenas para fins educacionais e de apoio
- Mantenha confidencialidade dos dados do paciente
- Sempre aplique seu julgamento clínico

---

**Desenvolvido para apoio educacional médico** | **Versão 2.0 - Streamlit**
