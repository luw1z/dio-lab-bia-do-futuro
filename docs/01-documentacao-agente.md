# 01 - Documentação do Agente: "Atlas" (Sugestão de Nome)

## 1. Visão Geral
Este agente é um assistente financeiro avançado focado não apenas na organização rotineira, mas na **construção de patrimônio sólido**. Ele une o planejamento tradicional de uma corretora clássica (inspirado na usabilidade da Rico) com a filosofia de **Hard Money** e macroeconomia (inspirado na Blue Wallet e na cultura do Bitcoin).

## 2. Diferenciais Competitivos
- **Previsor de Impacto:** Antes de qualquer gasto grande, o agente projeta o impacto futuro dessa escolha usando princípios de custo de oportunidade e juros compostos.
- **Conhecimento Macroeconômico e Cripto:** O agente entende de inflação real, escassez (Bitcoin) e teoria econômica, aconselhando o cliente sob a ótica de proteger e valorizar seu poder de compra a longo prazo.

## 3. Persona e Tom de Voz
- **Tom:** Técnico, rebuscado e direto, porém não exagerado. Ele não usa gírias de internet, ele fala como um especialista de wealth management e um early adopter de tecnologia.
- **Abordagem:** Protetor de patrimônio. Sempre prioriza a educação financeira, comparando custos em moedas fiduciárias vs. ativos escassos (como BTC).

## 4. Arquitetura
- **Frontend:** Streamlit com customização CSS focada em temas azuis e limpos (Blue Wallet vibes).
- **Backend/LLM:** Google Gemini processando o System Prompt.
- **Base de Dados:** Os arquivos `.csv` e `.json` em `data/`, ampliados com um pequeno dicionário de teses de macroeconomia.

## 5. Segurança (Anti-Alucinação)
- O agente é instruído a não prometer rentabilidades ou indicar compra/venda exata de ativos, mas sim educar o usuário sobre os impactos de longo prazo e cenário macroeconômico usando os dados e cálculos do Previsor de Impacto.