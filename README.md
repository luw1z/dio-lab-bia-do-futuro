# 🏦 Atlas | Gestor de Patrimônio (IA)

Bem-vindo ao repositório oficial do **Atlas**, um agente financeiro inteligente desenvolvido como parte do Desafio de IA Generativa da [Digital Innovation One (DIO)](https://www.dio.me/).

Video no youtube explicando o projeto, o video ficou rápido pois o tempo máximo era de apenas 3 minutos. 
(https://youtu.be/jtzs4puqXpA)

Enquanto as ferramentas do mercado apenas exibem saldos passivamente, o Atlas atua como um parceiro e conselheiro patrimonial. Desenvolvido sob a ótica da **Escola Austríaca de Economia** e alinhado aos princípios de preservação do poder de compra (Hard Money), ele ajuda usuários a fugirem de gastos impulsivos e ciladas contábeis.

## 🚀 Principais Funcionalidades

- **Onboarding Investigativo (KYC Automático):** Em vez de usar formulários extensos, o Atlas realiza um questionário elegante e conversacional para mapear o perfil financeiro, as metas e a renda do usuário de forma orgânica.
- **Previsor de Impacto:** A grande joia do agente. Toda vez que o usuário mencionar a intenção de contrair dívidas, financiar passivos atrelados à inflação governamental (ex: compra de carro novo), o Atlas não apenas o alerta, como faz um *mockup* de **Custo de Oportunidade**, renderizando tabelas comparativas.
- **Filtro de Qualidade Máxima (Ações):** O Atlas é ensinado a abominar o mecanismo das ações preferenciais ("Final 4") que retiram poder de voto do minoritário no mercado brasileiro e foca em recomendar empresas provadas ("lucro acompanhando a cotação").
- **UI Responsiva e Premium:** O Chatbot tem aparência refinada baseada no layout dos principais Wealth Managements do mundo.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** - Essência do projeto local.
- **[Google Gemini API](https://ai.google.dev/)** (`gemini-flash-lite-latest`) - O LLM que alimenta a lógica complexa e interativa do Agente.
- **[Streamlit](https://streamlit.io/)** - Renderização instantânea do Fron-end para o Chat e visualização UI/UX.

---

## ⚙️ Como Executar Localmente

### Pré-requisitos
- Ter o Python instalado (3.9+ recomendado)
- Uma chave API do Google [Gemini (Google AI Studio)](https://aistudio.google.com/)

### Instalação

1. **Clone este repositório:**
```powershell
git clone https://github.com/luw1z/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro
```

2. **Crie um ambiente virtual e o ative:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # No Windows (PowerShell)
```

3. **Instale as dependências:**
```powershell
pip install -r requirements.txt
```
*(Caso não possua o requirements, instale as bibliotecas base: `pip install streamlit pandas google-generativeai python-dotenv`)*

4. **Execute a aplicação:**
```powershell
streamlit run src/app.py
```

Assim que a aplicação abrir no seu navegador, a barra lateral irá solicitar sua `GEMINI_API_KEY`. Após colá-la, o diálogo com o Atlas é liberado imediatamente!

---

## 📂 Organização do Projeto
* `src/app.py`: Arquivo base e ponto zero de execução do agente (Streamlit e GenerativeAI).
* `docs/`: Regras, Documentação, Rascunhos do Pitch e Prompts do Sistema do Agente.
* `.gitignore`: Tranca a publicação indevida de dados do Virtual Environment (`.venv`) e variáveis (`.env`).

---

**Desenvolvido com dedicação por @luw1z na trila de IA da DIO.** 🚀
