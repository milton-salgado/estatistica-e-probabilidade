# Probest Cheat Sheet

> [!note] Axiomas
> 1. $0\leq \Bbb{P}(A)\leq 1$
> 2. $\Bbb{P}(\Omega)=1$
> 3. Dados $A_{i}$ **disjuntos dois a dois**, então:
> $$
> \Bbb{P}\left( \bigcup_{i=1}^{\infty}A_{i} \right)=\sum_{i=1}^{\infty}\Bbb{P}(A_{i})
> $$

> [!tip] Mutuamente Exclusivos
> Eventos que não podem ocorrer **simultaneamente**, isto é, $A\cap B=\emptyset$.

> [!tip] Independência
> Dois eventos $A$ e $B$ são **independentes** se a ocorrência do evento não altera a probabilidade do outro, isto é,
> 
> $$
> \Bbb{P}(A\cap B)=\Bbb{P}(A)\Bbb{P}(B)
> $$

> [!note] Teorema da Soma
> Se $A$ e $B$ são eventos **mutuamente exclusivos**, então:
> 
> $$
> \Bbb{P}(A\cup B)=\Bbb{P}(A)+\Bbb{P}(B) 
> $$

> [!note] Regra da Multiplicação
> Se $A$ e $B$ são eventos com **probabilidade positiva**, então:
> 
> $$
> \Bbb{P}(A\cap B)=\Bbb{P}(A)\Bbb{P}(B\mid A)=\Bbb{P}(B)\Bbb{P}(A\mid B)
> $$
>
> Ou também, **generalizando** temos
> 
> $$
> \Bbb{P}\left( \bigcap_{i=1}^{n}A_{i} \right)=\Bbb{P}(A_{1})\Bbb{P}(A_{2}\mid A_{1})\Bbb{P}(A_{3}\mid A_{1}\cap A_{2})\dots \Bbb{P}(A_{n}\mid A_{1}\cap\dots \cap A_{n-1})
> $$

> [!note] Probabilidade Condicional
> Dado dois eventos $A$ e $B$ com $\Bbb{P}(B)=0$, a **probabilidade condicional** é definida como
> 
> $$
> \Bbb{P}(A\mid B)=\frac{\Bbb{P}(A\cap B)}{\Bbb{P}(B)}
> $$

> [!tip] Partição
> Eventos que formam uma partição são **mutuamente exclusivos** e sua união cobre todo $\Omega$.

> [!note] Lei da Probabilidade Total
> Considere que $A_{1},\dots,A_{n}$ formem uma partição de $\Omega$. Para todo evento $B$ temos que
> 
> $$
> \Bbb{P}(B)=\Bbb{P}(A_{1})\Bbb{P}(B\mid A_{1})+\dots+\Bbb{P}(A_{n})\Bbb{P}(B\mid A_{n})
> $$

> [!note] Teorema de Bayes
> Se $A$ e $B$ são eventos com **probabilidade positiva**, então
> 
> $$
> \Bbb{P}(B\mid A)=\frac{\Bbb{P}(A\mid B)\Bbb{P}(B)}{\Bbb{P}(A)}=\frac{\Bbb{P}(A\mid B)\Bbb{P}(B)}{\Bbb{P}(A\mid B)\Bbb{P}(B)+\Bbb{P}(A\mid B^{c})\Bbb{P}(B^{c})}
> $$

> [!note] Lei de Morgan
> Se $A_{1},\dots,A_{n}$ são eventos em $\Omega$, então
> 
> $$
> \left( \bigcup_{i=1}^{\infty}A_{i} \right)^{c}=\bigcap_{i=1}^{\infty}A_{i}^{c}\quad \text{e}\quad \left( \bigcap_{i=1}^{\infty}A_{i} \right)^{c}=\bigcup_{i=1}^{\infty}A_{i}^{c}  
> $$