<img alt="Infografico" src="infografico.png" style="margin: 15px 0" />

# Desvendando a Sliding Window: Sua Primeira Janela para o Gerenciamento de Contexto

## 1. Introdução: O Desafio do Contexto Infinito
Para uma Inteligência Artificial, "contexto" é tudo. É a sua memória de trabalho. Gerenciar um contexto que cresce infinitamente é um dos grandes desafios da área, pois consome recursos computacionais valiosos.

É aqui que entra a **Sliding Window** (ou Janela Deslizante), *"uma técnica direta para gerenciamento de contexto"* que mantém o foco da IA no que é mais importante: o presente.

---

## 2. O Conceito Central: Como a Janela "Desliza"
A regra fundamental da Sliding Window é incrivelmente simples e se baseia em um movimento contínuo para manter apenas as informações mais atuais na memória ativa.

* **A Regra Principal:** A janela de contexto sempre mantém a versão mais recente do texto, dentro de um limite pré-definido (ex: últimos 3.000 tokens).
* **O Movimento Contínuo:** À medida que novos dados entram, os dados mais antigos "caem" para fora da janela, sendo removidos do foco imediato.

---

## 3. A Analogia Visual: Enxergando a Janela em Ação
A forma mais intuitiva de entender como a Sliding Window funciona é imaginá-la em movimento.

> **A Analogia:**
> *Imagine uma caixa rosa posicionada sobre a linha do tempo de uma conversa. Conforme novas mensagens chegam, essa caixa se move para a direita. O conteúdo novo entra no foco (rosa), e o conteúdo antigo fica para trás (cinza).*

**Nota para Desenvolvedores:** É o mesmo princípio dos algoritmos de janela deslizante encontrados em desafios de programação (como no LeetCode), onde se processa um subarray de tamanho fixo.

---

## 4. Uma Escolha Estratégica: O Que Fazer com o Passado?
O que acontece com os dados que "caem" da janela não é apenas um detalhe técnico, mas uma decisão estratégica de design.

| Opção | Benefício Principal |
| :--- | :--- |
| **🗑️ Descartar** | **Eficiência máxima.** Libera recursos computacionais instantaneamente e simplifica o sistema (Stateless). |
| **🗄️ Arquivar** | **Preservação de conhecimento.** Permite revisitar ou sumarizar o histórico posteriormente (Memória de Longo Prazo / RAG). |

---

## 5. Conclusão: Foco Total no "Agora"
Em essência, a técnica da Sliding Window é uma poderosa ferramenta de gerenciamento de foco.

Ela garante que a IA esteja sempre olhando para o "agora", mantendo as interações mais recentes em sua memória ativa enquanto o passado é movido para fora do processamento imediato.

### [Assista ao resumo em vídeo](https://github.com/user-attachments/assets/4d36ada9-538c-4ec3-99a2-118f25f36d05)
