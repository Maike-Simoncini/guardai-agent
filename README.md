# GuardAI: Agente Inteligente para Cibersegurança e Análise de Vulnerabilidades 🛡️🤖

O **GuardAI** é uma especialização do **DIO Agent**, projetada para atuar como um mentor e auditor interativo de Cibersegurança e Segurança de Aplicações (AppSec). 

Diferente de assistentes de IA genéricos que entregam soluções prontas imediatamente, o GuardAI foi configurado para agir como um profissional de segurança experiente: investiga o contexto do ambiente antes de sugerir intervenções, avalia riscos com matrizes estruturadas e orienta a remediação de falhas com base em padrões consolidados da indústria.

---

## 🎯 A Especialização e seus Motivos

Em Segurança da Informação, aplicar um "fix" ou executar comandos de mitigação sem compreender a arquitetura e o ambiente do sistema pode ser desastroso (causando indisponibilidade de serviços ou correções ineficazes).

A especialização do GuardAI foi modelada sob três pilares:
1. **Coleta de Contexto Obrigatória**: O agente pergunta e valida as características do ambiente (ex.: laboratório, ambiente produtivo, permissões) antes de fornecer scripts ou recomendações de mitigação.
2. **Avaliação Qualitativa de Risco**: Diagnósticos de vulnerabilidade seguem sempre o formato estruturado de **Impacto**, **Probabilidade** e **Severidade**.
3. **Mapeamento Normativo**: Todas as falhas detectadas são correlacionadas com categorias do **OWASP Top 10** e táticas/técnicas do framework **MITRE ATT&CK**.

---

## 📂 Estrutura e Arquivos do Repositório

O projeto foi construído de forma 100% declarativa, utilizando apenas arquivos Markdown (`.md`) e código de laboratório, sem a necessidade de treinamento de modelos de linguagem.

```text
guardai-agent/
├── README.md                          # Documentação principal do projeto
├── AGENTS.md                          # Catálogo de agentes e mapeamento de skills
├── agent/
│   ├── persona.md                     # Persona, tom defensivo e diretrizes do GuardAI
│   └── knowledge/
│       └── security-basics.md         # Conhecimento base em CID, OWASP e MITRE ATT&CK
├── skills/
│   └── vulnerability-analysis/
│       ├── SKILL.md                   # Roteiro passo a passo da skill de análise
│       └── README.md                  # Documentação humana da skill
└── lab/
    └── app.py                         # Código Python de teste com SQL Injection e fix
```

Detalhes das Alterações e Adições:
 * AGENTS.md: Atualizado na raiz para registrar a nova habilidade vulnerability-analysis na tabela lida pelos Harnesses.
 * agent/persona.md: Ajustado com as diretrizes do GuardAI, definindo a mentalidade defensiva e a obrigatoriedade de perguntas contextuais.
 * agent/knowledge/security-basics.md: Criado com conceitos cruciais como a Tríade CID (Confidencialidade, Integridade e Disponibilidade), diferença entre Vulnerabilidade/Ameaça/Risco, categorias do OWASP Top 10 e táticas do MITRE ATT&CK.
 * skills/vulnerability-analysis/SKILL.md: Criado contendo o algoritmo de análise que o agente executa ao investigar um código ou infraestrutura.
 * skills/vulnerability-analysis/README.md: Criado para documentar a utilidade da skill para leitores do repositório.
 * lab/app.py: Aplicação Python contendo um login vulnerável a SQL Injection (login_vulneravel) e a versão mitigada com consulta parametrizada (login_seguro).

### 🛠️ Como Executar o GuardAI no Hermes
 * Clone o repositório:

git clone [https://github.com/Maike_Simoncini/guardai-agent.git](https://github.com/Maike_Simoncini/guardai-agent.git)
cd guardai-agent


 * Instalação do Harness:
   Certifique-se de ter o Hermes instalado conforme as instruções da documentação oficial.
 * Execução no Terminal:

> ⚠️ Importante: Abra o terminal exatamente dentro da pasta raiz do projeto (guardai-agent/). Se aberto em outro local, o Hermes não encontrará os arquivos AGENTS.md e a pasta skills/.
>

   Inicie o agente com o comando: **hermes**

### 🚀 Melhorias Escolhidas

Para evoluir o agente além do escopo básico do desafio, foram implementadas as seguintes melhorias:
 * Matriz de Risco Padronizada: A skill garante que toda análise retorne obrigatoriamente a tríade de avaliação de risco (Impacto, Probabilidade e Severidade), permitindo comparar diferentes vulnerabilidades no mesmo formato.
 * Fluxo Estilo DevSecOps: O agente atua preventivamente revisando alterações no código (Pull Requests de laboratório), sugerindo testes com consultas parametrizadas (Prepared Statements) antes que o código chegue a um ambiente produtivo.

### 📸 Evidências de Testes e Validação

Teste 1: Auditoria Inicial de Código (lab/app.py)
Ao solicitar a análise da função login_vulneravel presente no arquivo lab/app.py, o GuardAI identificou a falha de SQL Injection, mapeou para o OWASP A03:2021 - Injection e relacionou à técnica MITRE ATT&CK T1190 (Exploitation of Public-Facing Application).

Teste 2: Pergunta de Contexto Antes da Ação
Antes de gerar o script de correção ou propor comandos no terminal, o GuardAI questionou o ambiente de execução, perguntando se o teste era realizado em ambiente de laboratório isolado e se o SGBD utilizado era o SQLite.

Teste 3: Revalidação e Confirmação de Mitigação
Após a substituição do código pela função login_seguro utilizando consultas parametrizadas com placeholders (?), o GuardAI fez uma nova varredura e confirmou a eliminação da vulnerabilidade.

### 🖖 Considerações Finais
O projeto demonstra como a engenharia de prompts estruturada em arquivos Markdown (.md) e um Harness como o Hermes conseguem especializar um LLM em uma disciplina técnica complexa sem a necessidade de re-treinamento ou fine-tuning de modelos.


Long live and prosper! 🖖

