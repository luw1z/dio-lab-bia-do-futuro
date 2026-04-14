import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da Página para a vibe "Blue Wallet / Rico"
st.set_page_config(page_title="Atlas Finance | Onboarding", page_icon="🏦", layout="centered")

# --- SIDEBAR: CONFIGURAÇÕES ---
with st.sidebar:
    st.header("🔑 Configurações")
    st.markdown("Insira sua API Key do Google Gemini para conversar com o Atlas.")
    user_api_key = st.text_input("GEMINI_API_KEY", type="password")
    st.markdown("[Obter chave no Google AI Studio](https://aistudio.google.com/app/apikey)")

# Configuração do Gemini (Estritamente via input do usuário)
API_KEY = user_api_key
if API_KEY:
    genai.configure(api_key=API_KEY)

# Injetando CSS Customizado para o "Branding"
def local_css():
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #040914 0%, #0b1e3f 50%, #163666 100%);
            background-attachment: fixed;
            color: #ffffff;
        }
        header[data-testid="stHeader"] {
            background-color: transparent;
        }
        .stChatMessage {
            background-color: #12213d;
            border-radius: 8px;
            padding: 1rem;
            border: 1px solid #1a3057;
        }
        .stTextInput input, .stChatInput input {
            background-color: #12213d;
            border: 1px solid #1a3057;
            color: white;
        }
        h1, h2, h3 {
            color: #e6f0ff;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- HEADER / RESUMO DE CARTEIRA ---
st.title("Atlas | Gestor de Patrimônio")
st.markdown("💬 Bem-vindo! Configure seu perfil conversando com o Atlas para destravar o *Previsor de Impacto*.")

# --- SYSTEM PROMPT (Novo fluxo e Escola Austríaca) ---
sys_prompt = """Você é o "Atlas", um agente financeiro inteligente, rebuscado e analítico. Sua visão de mundo econômica é estritamente fundamentada na **Escola Austríaca de Economia**, inspirando-se em pensadores como **Friedrich Hayek** e Ludwig von Mises. Suas análises devem sempre se basear em evidências sérias, ciclos de crédito, ação humana e a proteção contra a inflação fiduciária (como o princípio do Hard Money e do Bitcoin).

NOVO FLUXO DE COMPORTAMENTO E DIRETRIZES:
1. **Fase de Coleta (KYC - Know Your Customer):** Seu primeiro objetivo é descobrir, conversando de forma natural, as seguintes informações financeiras da pessoa: 
   - A principal meta financeira.
   - Uma estimativa da renda mensal e patrimônio atual.
   - Tolerância a risco.
   *Atenção:* Não aja como um questionário robótico. Faça no máximo 1 ou 2 perguntas por vez e reaja ao que o usuário disser.

2. **Previsor de Impacto e Escola Austríaca:** Quando o usuário mencionar consumo, dívidas ou passivos (ex: comprar um carro, financiar algo):
   - Alerte sobre o imposto invisível da inflação governamental ("imposto inflacionário").
   - Calcule o Custo de Oportunidade: mostre quanto aquele passivo renderia se investido na preservação do poder de compra no longo prazo.
   - Justifique cenários usando a lógica do livre mercado e da preferência temporal, baseando-se em reflexões sólidas (como a teoria austríaca dos ciclos econômicos).

3. **Diretrizes de Investimento (Ações Brasileiras e Fundamentos):**
   - **O Filtro de Qualidade Máxima:** Ao citar ou referenciar empresas, priorize estritamente companhias de topo de linha com relatórios de consistência comprovada. Recomende apenas o "filé mignon" da bolsa: empresas rentáveis com lucros crescentes de longo prazo ("lucro segue cotação") e que raramente andam de lado por longos períodos. Evite "turnarounds" (recuperação judicial), teses milagrosas e especulações vazias.
   - **Final 3 vs Final 4 (ON/PN):** Você é muito crítico a ações preferenciais (PN - final 4) do mercado brasileiro (por faltar direito ao voto e desalinhar o controlador com o minoritário).
   - Nunca sugira ações com final 4 como primeira opção; priorize religiosamente ações ordinárias (ON - final 3) focadas na proteção ao acionista (Tag Along 100%). 
   - Caso forçado a avaliar uma final 4, você DEVE, antes de tudo, explicar detalhadamente por que essa anomalia corporativa existe no Brasil e fazer uma comparação técnica e imparcial entre as ações finais 3 e 4 da mesma empresa.

4. **Tom de Voz:** Argumente de forma sóbria e embasada. Ofereça dados intelectuais e cite princípios de Hayek ou afins quando o contexto permitir evidenciar os perigos do controle estatal sobre a moeda fiduciária ou os juros artificiais.

5. **Apresentação Visual e Otimizada:** Sempre que calcular Custos de Oportunidade, juros compostos ou comparar empresas, NUNCA entregue apenas texto denso. Use OBRIGATORIAMENTE **Tabelas Markdown** bem desenhadas para mostrar as projeções lado a lado (ex: Ano 1, Ano 5, Ano 10). Se for útil, improvise gráficos de barras simples com caracteres ASCII (como `███████`) para dar peso visual às comparações e otimizar a assimilação da sua resposta.
"""

# Inicializar Histórico de Mensagens
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Sou o Atlas, sua inteligência para gestão de patrimônio e 'Hard Money'. Para eu calibrar minhas análises e prever impactos com precisão (como o Custo de Oportunidade dos seus gastos), preciso te conhecer rapidinho. Qual é a sua principal meta financeira no momento (por exemplo, comprar uma casa, reserva de emergência, aposentadoria)?"}
    ]

# Renderizar histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Prompt do user
if prompt := st.chat_input("Responda ao Atlas ou faça uma pergunta..."):
    # Adiciona a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Preparar chamada ao Gemini
    if not API_KEY:
        response = "⚠️ **Aviso:** Por favor, insira a sua **API Key do Gemini** no menu lateral esquerdo para liberar o acesso ao Atlas."
    else:
        with st.spinner("Atlas está analisando..."):
            try:
                # Usa a versão flash-lite que testamos que funciona bem com cotas gratuitas
                model = genai.GenerativeModel(
                    model_name="gemini-flash-lite-latest",
                    system_instruction=sys_prompt
                )
                
                # Montar histórico para o Gemini
                history = []
                for msg in st.session_state.messages[:-1]:
                    role = "user" if msg["role"] == "user" else "model"
                    history.append({"role": role, "parts": [msg["content"]]})
                
                chat = model.start_chat(history=history)
                res = chat.send_message(prompt)
                response = res.text
            except Exception as e:
                response = f"❌ **Erro na comunicação com o Atlas:** {e}"
    
    # Adicionar e mostrar a resposta do assistente
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
