import streamlit as st
from PIL import Image
import os
from google import genai
from google.genai import types
from datetime import datetime

# Verificar configurações essenciais
if "api" not in st.secrets or "gemini_api_key" not in st.secrets["api"]:
    st.error("""
    ❌ **API Key do Gemini não configurada!**
    
    Para configurar o sistema:
    1. Configure o arquivo `.streamlit/secrets.toml`
    2. Adicione sua API Key do Google Gemini
    3. Obtenha sua API Key em: https://aistudio.google.com/app/apikey
    
    Exemplo de configuração:
    ```toml
    [api]
    gemini_api_key = "sua_api_key_aqui"
    ```
    """)
    st.stop()

# Configurações da página usando secrets
st.set_page_config(
    page_title=st.secrets["ui"]["page_title"],
    layout=st.secrets["ui"]["layout"],
)

def analyze_conversation_to_soap(conversation_text):
    """
    Analisa a conversa médica usando Google Gemini 2.5 e converte para formato SOAP
    """
    if not conversation_text.strip():
        return None
    
    # Obter API key dos secrets
    api_key = st.secrets["api"]["gemini_api_key"]
    
    try:
        # Configurar cliente do Gemini
        client = genai.Client(api_key=api_key)
        
        # Prompt específico para análise SOAP
        prompt = f"""
        Analise a seguinte transcrição de consulta médica e organize as informações no formato SOAP médico padrão.
        
        TRANSCRIÇÃO:
        {conversation_text}
        
        Organize as informações nos seguintes campos OBRIGATÓRIOS:
        
        SUBJETIVO (S):
        - Liste todos os sintomas, queixas e histórico relatados pelo paciente
        - Inclua início dos sintomas, intensidade, localização, fatores de melhora/piora
        - Use bullet points para cada informação
        
        OBJETIVO (O):
        - Liste sinais vitais (PA, FC, FR, Tax, SatO2)
        - Exame físico por sistemas (inspeção, palpação, percussão, ausculta)
        - Dados antropométricos se mencionados
        - Use bullet points para cada informação
        
        AVALIAÇÃO (A):
        - DIAGNÓSTICO PRINCIPAL ou hipótese diagnóstica mais provável (seja específico, evite termos genéricos)
        - Diagnósticos diferenciais se aplicável
        - Justificativa baseada nos achados do subjetivo e objetivo
        - CID-10 se possível identificar
        - Use bullet points para cada informação
        
        PLANO (P):
        - Tratamento medicamentoso com posologia específica
        - Exames complementares solicitados
        - Orientações e cuidados gerais
        - Retorno e acompanhamento
        - Encaminhamentos se necessário
        - Use bullet points para cada item
        
        IMPORTANTE: Na seção AVALIAÇÃO, sempre forneça um diagnóstico específico baseado nos sintomas e achados apresentados. Evite termos vagos como "a esclarecer" ou "aguardar exames".
        
        Responda APENAS com as 4 seções organizadas, sem explicações adicionais.
        """
        
        model = st.secrets["model"]["model_name"]
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt),
                ],            ),
        ]
        generate_content_config = types.GenerateContentConfig(
            response_mime_type=st.secrets["model"]["response_mime_type"],
        )

        # Gerar resposta usando stream
        response_text = ""
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            response_text += chunk.text
        
        # Processar a resposta para extrair as seções SOAP
        sections = {
            "subjetivo": "",
            "objetivo": "",
            "avaliacao": "",
            "plano": ""
        }
        
        current_section = None
        lines = response_text.split('\n')
        
        for line in lines:
            line = line.strip()
            if 'SUBJETIVO' in line.upper() or line.upper().startswith('S'):
                current_section = "subjetivo"
                continue
            elif 'OBJETIVO' in line.upper() or line.upper().startswith('O'):
                current_section = "objetivo"
                continue
            elif 'AVALIAÇÃO' in line.upper() or 'AVALIACAO' in line.upper() or line.upper().startswith('A'):
                current_section = "avaliacao"
                continue
            elif 'PLANO' in line.upper() or line.upper().startswith('P'):
                current_section = "plano"
                continue
            elif current_section and line:
                sections[current_section] += line + "\n"
        
        # Limpar as seções
        for key in sections:
            sections[key] = sections[key].strip()
        
        return sections
        
    except Exception as e:
        st.error(f"Erro ao processar com Gemini: {str(e)}")
        return None

def main():
    # Header com logo e título usando configurações do TOML
    app_name = st.secrets["app"]["name"]
    app_description = st.secrets["app"]["description"]
    
    st.markdown(f"### {app_name}")
    st.markdown(f"**{app_description}**")
    
    # Verificar se o logo existe e exibi-lo usando configuração do TOML
    logo_path = st.secrets["ui"]["logo_path"]
    if os.path.exists(logo_path):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            image = Image.open(logo_path)
            st.image(image, width=120)
    
    st.markdown("---")
    
    # Campo de texto para a transcrição
    st.markdown("**📝 Transcrição da Consulta**")
    conversation_text = st.text_area(
        "Transcrição da Consulta",
        placeholder="Cole aqui a transcrição completa da consulta médica...\n\nExemplo:\nMédico: Boa tarde! Como posso ajudá-lo hoje?\nPaciente: Doutor, estou com uma dor de cabeça muito forte há 3 dias...",
        height=200,
        label_visibility="collapsed"
    )
    
    # Botão de análise
    analyze_button = st.button("🔍 Analisar Consulta", type="primary")
    
    # Informação sobre o formato SOAP
    st.info("""
**📋 Sobre o formato SOAP:**  
**S**ubjetivo - Sintomas e queixas relatadas pelo paciente  
**O**bjetivo - Sinais vitais, exame físico e dados observáveis  
**A**valiação - Diagnóstico ou hipótese diagnóstica  
**P**lano - Tratamento, exames complementares e orientações
    """)
    
    # Processamento e exibição dos resultados
    if analyze_button:
        if not conversation_text.strip():
            st.warning("⚠️ Por favor, insira a transcrição da consulta antes de analisar.")
        else:
            with st.spinner("🤔 Analisando consulta com IA..."):
                soap_result = analyze_conversation_to_soap(conversation_text)
                
                if soap_result:
                    st.markdown("---")
                    st.markdown("### 📋 Análise SOAP")
                    st.markdown("*Resultado da análise automática com Inteligência Artificial*")
                    st.markdown("")
                    
                    # Exibir cada seção do SOAP em expanderes estilizados
                    sections = [
                        ("🗣️ SUBJETIVO", soap_result["subjetivo"], "Sintomas e queixas relatadas pelo paciente"),
                        ("🔍 OBJETIVO", soap_result["objetivo"], "Sinais vitais, exame físico e observações"),
                        ("🎯 AVALIAÇÃO", soap_result["avaliacao"], "Hipótese diagnóstica e raciocínio clínico"),
                        ("📋 PLANO", soap_result["plano"], "Tratamento, medicações e orientações")
                    ]
                    
                    for title, content, description in sections:
                        with st.expander(f"{title} - {description}", expanded=True):
                            if content:
                                # Dividir o conteúdo em linhas e processar
                                lines = content.split('\n')
                                formatted_items = []
                                
                                for line in lines:
                                    line = line.strip()
                                    if line:
                                        # Remover marcadores existentes e padronizar
                                        if line.startswith('•') or line.startswith('-') or line.startswith('*'):
                                            clean_line = line[1:].strip()
                                        else:
                                            clean_line = line.strip()
                                        
                                        if clean_line:
                                            formatted_items.append(clean_line)
                                
                                if formatted_items:
                                    for item in formatted_items:
                                        st.write(f"• {item}")
                                else:
                                    st.info("Não identificado na transcrição")
                            else:
                                st.info("Não identificado na transcrição")
                    
                    # Botão de download do resultado
                    soap_text = f"""ANÁLISE SOAP - {datetime.now().strftime('%d/%m/%Y %H:%M')}

SUBJETIVO:
{soap_result["subjetivo"]}

OBJETIVO:
{soap_result["objetivo"]}

AVALIAÇÃO:
{soap_result["avaliacao"]}

PLANO:
{soap_result["plano"]}

---
Gerado pelo MaisGestorHealth
"""
                    
                    st.download_button(
                        label="📥 Baixar Análise SOAP",
                        data=soap_text,
                        file_name=f"analise_soap_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                        mime="text/plain"                    )
    
    # Footer discreto
    st.markdown("---")
    app_name = st.secrets["app"]["name"]
    app_version = st.secrets["app"]["version"]
    st.markdown(f"*{app_name} v{app_version} • Desenvolvido para profissionais de saúde")

if __name__ == "__main__":
    main()
