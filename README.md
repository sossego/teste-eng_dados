# 🚀 Teste Técnico - Engenharia de Dados

## 📋 Objetivo

Você deve **revisar e corrigir** o script Python fornecido para que ele execute corretamente as seguintes tarefas:

1. **Baixar** um arquivo CSV de produtos de forma automatizada
2. **Filtrar** produtos da categoria **AUTOMÓVEL** 
3. **Selecionar** os **TOP 5 produtos de MAIOR valor**
4. **Salvar** o resultado em arquivo JSON na pasta `data/`

## 🎯 Entregáveis

### ✅ Obrigatório
- [ ] Script `main.py` funcionando corretamente
- [ ] Arquivo `data/output.json` com os 5 produtos mais caros da categoria Automóvel
- [ ] Código revisado e sem erros
- [ ] Upload do projeto no **GitHub** (repositório público)
- [ ] Compartilhar o **link do repositório** com o aplicador do teste

### 🌟 Desafio Extra (opcional - apenas se sobrar tempo)
- [ ] Modificar o script para baixar a versão **comprimida (.zip)** do arquivo
- [ ] Extrair e processar o CSV de dentro do arquivo comprimido

## 📁 Estrutura do Projeto

```
teste-tecnico/
├── data/                    # Pasta para arquivos gerados
│   ├── products.csv        # CSV baixado  
│   └── output.json         # Resultado final (TOP 5)
├── main.py                 # Script principal (REVISAR E CORRIGIR)
├── gabarito.py             # Versão de referência (não modificar)
├── requirements.txt        # Dependências
└── README.md              # Documentação
```

## 🔧 Como Executar

### 1. Configurar ambiente
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac  
source .venv/bin/activate
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
python -m playwright install
```

### 3. Executar script
```bash
python main.py
```

## ⚠️ Importante

- O arquivo `main.py` **contém erros intencionais** que devem ser identificados e corrigidos
- O script deve executar **do início ao fim sem falhas**
- Certifique-se de que o resultado final esteja na pasta `data/output.json`

## 🎯 Critérios de Avaliação

- **Identificação de erros**: Capacidade de encontrar problemas no código
- **Correção técnica**: Implementação das soluções corretas
- **Boas práticas**: Organização e qualidade do código
- **Resultado final**: Arquivo JSON correto gerado
- **Documentação**: Commits claros no GitHub

## 📤 Entrega

1. Faça um **fork** ou crie um **novo repositório** no GitHub
2. Faça **commits** das suas correções com mensagens descritivas
3. Certifique-se de que o repositório é **público**
4. Envie o **link do repositório** para o aplicador do teste

---

**Tempo sugerido**: 45-60 minutos  
**Boa sorte! 🍀**
