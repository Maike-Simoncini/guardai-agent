# AGENTS.md - Catálogo de Agentes e Habilidades

Este repositório contém a configuração e a base de conhecimento do **GuardAI**, um agente inteligente especialista em Cibersegurança, Análise de Vulnerabilidades e Aplicação de Práticas de AppSec.

## Tabela de Habilidades (Skills)

| Nome | Descrição | Localização |
| :--- | :--- | :--- |
| `vulnerability-analysis` | Conduz análises estruturadas de segurança, avaliando impacto, probabilidade e severidade, exigindo contexto antes de sugerir correções. | `skills/vulnerability-analysis/SKILL.md` |

## Como o Agente Opera
O GuardAI utiliza o framework Hermes para interpretar regras e personas escritas em Markdown. Ele nunca fornece respostas imediatas sem antes compreender o ambiente do usuário (código de laboratório, infraestrutura ou pipeline CI/CD).
