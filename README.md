**# 🤖 Agente Financeiro Inteligente com IA Generativa

## Contexto

Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**. Neste desafio, você vai idealizar e prototipar um agente financeiro que utiliza IA Generativa para:

- **Antecipar necessidades** ao invés de apenas responder perguntas
- **Personalizar** sugestões com base no contexto de cada cliente
- **Cocriar soluções** financeiras de forma consultiva
- **Garantir segurança** e confiabilidade nas respostas (anti-alucinação)

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## O Que Você Deve Entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** Qual problema financeiro ele resolve? (ex: consultoria de investimentos, planejamento de metas, alertas de gastos)
- **Persona e Tom de Voz:** Como o agente se comporta e se comunica?
- **Arquitetura:** Fluxo de dados e integração com a base de conhecimento
- **Segurança:** Como evitar alucinações e garantir respostas confiáveis?

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilize os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Perfil e preferências do cliente |
| `produtos_financeiros.json` | JSON | Produtos e serviços disponíveis |

Você pode adaptar ou expandir esses dados conforme seu caso de uso.

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- Chatbot interativo (sugestão: Streamlit, Gradio ou similar)
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas Sugeridas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Grave um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Dicas Finais

1. **Comece pelo prompt:** Um bom system prompt é a base de um agente eficaz
2. **Use os dados mockados:** Eles garantem consistência e evitam problemas com dados sensíveis
3. **Foque na segurança:** No setor financeiro, evitar alucinações é crítico
4. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto
**# 🏦 Atlas | Gestor de Patrimônio (IA)

Bem-vindo ao repositório oficial do **Atlas**, um agente financeiro inteligente desenvolvido como parte do Desafio de IA Generativa da [Digital Innovation One (DIO)](https://www.dio.me/).

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
