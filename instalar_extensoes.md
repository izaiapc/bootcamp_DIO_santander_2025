## Extensões para instalar no VSCode
---

### 🔹 1. **Python** (Microsoft)

Já deve estar instalada, mas vale reforçar.

**Por quê?**

* Suporte oficial da Microsoft.
* IntelliSense, linting, debug, notebooks, ambiente virtual etc.

---

### 🔹 2. **Pylance**

**Complementa** a extensão Python com **análise estática e sugestões precisas**.

**Funcionalidades úteis:**

* Verifica erros antes de executar.
* Sugere tipos e corrige importações.
* Super leve e rápido.

---

### 🔹 3. **isort**

Organiza automaticamente os **import** do seu código Python.

**Vantagem real:**

* Remove imports não utilizados.
* Ordena alfabeticamente.
* Integra bem com o `Black`.

---

### 🔹 4. **Black Formatter**

Aplica formatação automática ao código (sem mudar sua lógica).

**Por quê?**

* Ajuda a manter o código **padronizado** e legível.
* Tira de você a preocupação estética: foca só na lógica.

---

### 🔹 5. **Jupyter**

Permite rodar **notebooks diretamente no VS Code**, ou transformar arquivos `.py` em células interativas.

**Indicado para:**

* Testar pequenos blocos de código.
* Visualizar dados ou saídas passo a passo.

---

### 🔹 6. **Code Runner**

Executa blocos de código rapidamente com um atalho (`Ctrl+Alt+N`).

**Diferencial:**

* Roda scripts **sem abrir terminal manualmente**.
* Muito útil para testar funções pequenas em segundos.

---

### 🔹 7. **Error Lens**

Destaque visual de erros e warnings **diretamente no código**, linha por linha.

**Útil para:**

* Detectar erros **sem precisar olhar o terminal**.
* Ganhar tempo corrigindo antes de rodar.

---

### 🔹 8. **Bookmarks**

Adiciona marcadores em pontos do código (atalhos de navegação).

**Quando usar:**

* Em arquivos longos, você pode “voltar onde parou”.
* Excelente para revisar lógicas ou voltar para funções específicas.

---

### 🔹 9. **GitLens**

Se estiver usando **Git**, essa extensão mostra:

* Quem alterou cada linha do código.
* Histórico de commits diretamente no editor.
* Comparação entre versões.

---

### 🔹 10. **Path Intellisense**

Autocompleta **caminhos de arquivos** ao usar `open()`, `import`, etc.

**Facilita muito** trabalhar com arquivos externos, imagens, dados, etc.

---

### 🔹 11. **Better Comments**

Classifica comentários em categorias com cores: `// TODO`, `// FIXME`, `// NOTE`, etc.

**Vantagem real:**
Ajuda a **encontrar rapidamente** pontos importantes do seu raciocínio.

---

### ✅ Configurações recomendadas para mais fluidez:

```json
"editor.formatOnSave": true,
"python.linting.enabled": true,
"python.linting.pylintEnabled": true,
"editor.codeActionsOnSave": {
  "source.organizeImports": true
},
"python.analysis.typeCheckingMode": "basic"
```

---

### 🚫 O que **não recomendo agora**:

| Extensão                        | Por quê evitar (por enquanto)               |
| ------------------------------- | ------------------------------------------- |
| GitHub Copilot                  | Sugeriria código demais para sua fase atual |
| TabNine                         | Outra IA que compete com seu raciocínio     |
| Temas visuais/fonte customizada | Só estética, não ajuda na lógica            |

---

Se quiser, posso montar um **perfil de configuração leve** (JSON completo) com todas essas extensões e opções ativadas, pronto pra copiar e colar no seu `settings.json`.

Quer que eu faça isso?
