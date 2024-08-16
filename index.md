$$
\Huge\displaystyle \int _{a}^{b}f'(x)\,\mathrm{d}x  = f(b)-f(a)
$$
# Fourier Transform
$$
\begin{array}{rcccl}
\mathcal{F}\{f\}(\xi) &  =  & \hat{f}(\xi)  & = & \displaystyle \int_{-\infty}^{\infty} f(x) \cdot e^{-i 2 \pi \xi x} \, \mathrm{d}x  \\
\mathcal{F}^{-1}\{\hat{f}\}(x) &  =  & f(x) &  =  & \displaystyle\int_{-\infty}^{\infty} \hat{f}(\xi) \cdot e^{i2\pi\xi x} \, \mathrm{d}x 
\end{array}
$$
## Discrete Fourier Transform
$$
\begin{array}{rcccl}
\text{DFT}\{f\}(k) &  = &  \hat f(k)  & = &\displaystyle \sum_{n = 0}^{N - 1} f(x) \cdot e^{-\frac{i 2 \pi}{N} kn} \\
\text{IDFT}\{\hat{f}\}(n) &  = &  f(n) &  =  & \displaystyle\frac{1}{N} \sum_{k = 0}^{N-1} \hat{f}(k) \cdot e^{\frac{i 2 \pi}{N} kn}  
\end{array}
$$
# Euler's Identity
$$
e^{i\theta}=\cos\theta+i\sin\theta 
$$
## Proof
$$
\begin{array}{rcl}
e^{i\theta} & = &\displaystyle1 + i\theta + \frac{(i\theta)^{2}}{2!} + \frac{(i\theta)^{3}}{3!} + \frac{(i\theta)^{4}}{4!} + \frac{(i\theta)^{5}}{5!} + \frac{(i\theta)^{6}}{6!} + \frac{(i\theta)^{7}}{7!} + \cdots  \\
e^{i\theta} & = &\displaystyle1 + i\theta - \frac{\theta^{2}}{2!} - \frac{i\theta^{3}}{3!} + \frac{\theta^{4}}{4!} + \frac{i\theta^{5}}{5!} - \frac{\theta^{6}}{6!} - \frac{i\theta^{7}}{7!} + \cdots \\
e^{i\theta} & = & \displaystyle\left( 1 - \frac{\theta^{2}}{2!} + \frac{\theta^{4}}{4!} - \frac{\theta^{6}}{6!} + \cdots \right) + i\left( \theta - \frac{\theta^{3}}{3!} + \frac{\theta^{5}}{5!} - \frac{\theta^{7}}{7!} + \cdots\right) \\
e^{i\theta} & = & \cos \theta + i \sin \theta
\end{array}
$$
# Taylor Series
$$
f(x)=f(a)+\frac{f'(a)}{1!}(x-a)+\frac{f''(a)}{2!}(x-a)^{2}+\frac{f'''(a)}{3!}(x-a)^{3}+\cdots=\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^{n}
$$
$$
\begin{array}{rcl}
e^{x} & = &\displaystyle\sum_{n=0}^{\infty} \frac{x^{n}}{n!} \\
\displaystyle \frac{1}{1-x}  & = &\displaystyle\sum_{n=0}^{\infty}x^n \\
\sin x & = &\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n+1)!}x^{2n+1} \\
\cos x & = &\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^{n}}{(2n)!}x^{2n}
\end{array}
$$
$$
\begin{array}{rcl}
e^{x} & = &\displaystyle\int e^{x} \\
\displaystyle e^{x} - \int e^{x} & = & 0 \\
\displaystyle\left(1 - \int\right)e^{x} & = & 0 \\
e^{x} & = &\displaystyle\left(1 - \int\right)^{-1} 0 \\
& = &\displaystyle \frac{1}{\displaystyle1 - \int}0 \\
& = &\displaystyle\left(\left( \int \right)^{0} + \left( \int \right)^{1} + \left( \int \right)^{2} + \left( \int \right)^{3} + \cdots\right) 0 \\
& = &\displaystyle 0 + 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \cdots \\
& = &\displaystyle\sum_{n=0}^{\infty} \frac{x^{n}}{n!}
\end{array}
$$
# Limit Definition of Derivative
$$
\begin{array}{rcl}
\displaystyle\lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} & = &\displaystyle\frac{\mathrm{d}f}{\mathrm{d}x}  \\
\displaystyle\lim_{\Delta x \to 0} \frac{f(x+\Delta x, y,z)-f(x,y,z)}{\Delta x} & = & \displaystyle \frac{\partial f}{\partial x}  \\
\displaystyle\lim_{\Delta e_{i} \to 0} \frac{f(e_{0},\cdots,e_{i}+\Delta e_{i},\cdots,e_{n}) - f(e_{0},\cdots,e_{i},\cdots,e_{n})}{\Delta e_{i}} & = &\displaystyle\frac{\partial f}{\partial e_{i}} 
\end{array}
$$
# Quadratic Formula
$$
ax^{2}+bx+c=0 \iff x=\frac{-b\pm \sqrt{b^{2}-4ac}}{2a}
$$
## Proof
$$
\begin{array}{rcl}
ax^{2}+bx+c & = & 0 \\
\displaystyle x^{2}+\frac{b}{a}x+\frac{c}{a} & = & 0 \\
\displaystyle x^{2}+\frac{b}{a}x & = &\displaystyle -\frac{c}{a} \\
\displaystyle x^{2}+\frac{b}{a}x+\left( \frac{b}{2a} \right)^{2} & = &\displaystyle \left( \frac{b}{2a} \right)^{2}-\frac{c}{a} \\
\displaystyle \left( x+\frac{b}{2a} \right)^{2} & = &\displaystyle \frac{b^{2}-4ac}{4a^{2}} \\
\displaystyle \sqrt{\left( x+\frac{b}{2a} \right)^{2}} & = &\displaystyle \sqrt{\frac{b^{2}-4ac}{4a^{2}}}\\
\displaystyle x+\frac{b}{2a} & = &\displaystyle \frac{\pm\sqrt{b^{2}-4ac}}{2a} \\
x & = &\displaystyle \frac{-b\pm \sqrt{b^{2}-4ac}}{2a}
\end{array}
$$
# Gamma Function
$$
\Gamma(z)=\int_{0}^{\infty} t^{z-1}e^{-t} \, \mathrm{d}t = (z-1)!
$$
# Differintegral
$$
\begin{array}{c}
_{a}D^{p}_{t} f(t)=\left\{\begin{array}{lcl}
\displaystyle \frac{1}{\Gamma(\alpha)} \cdot \left( \frac{\mathrm{d}}{\mathrm{d}t}  \right)^k \int _{a}^{t} (t-x)^{\alpha-1} \cdot f(x) \, \mathrm{d}x & : & p>0 \\
f(t) & : & p=0 \\
\displaystyle \frac{1}{\Gamma(\lvert p \rvert )} \cdot \int _{a}^{t} (t-x)^{\lvert p \rvert -1} \cdot f(x) \, \mathrm{d}x  & : & p<0 
\end{array}\right. \\
\small\boxed{\text{where }p+a = k\text{ and }k \in \mathbb{Z}} 
\end{array}
$$
# Euler's Theorem
$$
\gcd(a,m) = 1 \implies a^{\varphi(m)}\equiv 1 \mod m
$$
## Proof
$$
\begin{array}{c} \\
\boxed{
\begin{array}{c}
\small \gcd(x,m) = gcd(y,m) = gcd(a,m) = 1  \\
\small ax \equiv ay \mod m \iff x \equiv y \mod m
\end{array}
} \\
A_{n} = \{x : x \in \mathbb{N}^{\leq n} \land \gcd(x,n)=1\} \\
\lvert A_{n} \rvert = \varphi(n) \\
\small \text{Let }a\text{ be a integer such that }\gcd(a,n)=1 \\
aA_{n} = \{ax : x \in A_{n}\} \\
aA_{n} \equiv A_{n} \mod n \\
\small\text{The reason for this is }{\large \forall}_{\! x  \in A_{n}}:{\large \exists!}_{x'  \in aA_{n}}: x \equiv x' \mod n \\
\displaystyle \prod_{x \in A_{n}}x \equiv \prod_{x \in A_{n}}ax \equiv a^{\varphi(n)}\prod_{x \in A_{n}}x \mod n \\
\displaystyle \cancel{\prod_{x \in A_{n}}x} \equiv a^{\varphi(n)}\cancel{\prod_{x \in A_{n}}x} \mod n \\
a^{\varphi(n)} \equiv 1 \mod n
\end{array}
$$
# Euler's Totient Function
$$
\begin{array}{rc}
 & \small \text{Let } n = p_{1}^{k_{1}}p_{2}^{k_{2}}\cdots p_{r}^{k_{r}} \\
1) & \displaystyle \varphi(n) = n \cdot \prod_{i=1}^{r}\left( 1-\frac{1}{p_{i}} \right) =  p_{1}^{k_{1}-1}(p_{1}-1) \cdot p_{2}^{k_{2}-1}(p_{2}-1)  \cdot \cdots \cdot p_{r}^{k_{r}-1}(p_{r}-1) \\
2) & \displaystyle \varphi(n) = \varphi(p_{1}^{k_{1}}) \cdot \varphi(p_{2}^{k_{2}}) \cdot\,\cdots\,\cdot \varphi(p_{r}^{k_{r}}) \\
3) & \displaystyle n = \sum_{d|n} \varphi(d) \\
4) & \displaystyle \varphi(n) = \sum_{k = 1}^{n} \gcd(k,n) \cdot \cos \frac{2\pi k}{n} \\
5) & \displaystyle A_{n} = \{k \in \mathbb{N} : \gcd(k,n) = 1\} \implies \lvert A_{n} \rvert  = \varphi(n)
\end{array}
$$
# Golden Ratio
```tikz
\usepackage{tikz}
\usepackage{xcolor}
\usetikzlibrary{decorations.pathreplacing}  
\definecolor{mcred}{RGB}{255,100,112}
\definecolor{mcgreen}{RGB}{153,196,122}
\definecolor{mcblue}{RGB}{104,171,223}
\begin{document}
\begin{tikzpicture}
\draw[mcred, ultra thick] (0,0) -- (5,0);
\draw[mcblue, ultra thick] (5.1,0) -- (13.1901699437,0);
\node[mcred, align=center, text width=4cm] at (2.5,-.5) {\huge $a$};
\node[mcblue, align=center, text width=4cm] at (9.14508497187,-.5) {\huge $b$};
\node[mcgreen, align=center, text width=4cm] at (6.595084972,1) {\huge $c$};
\draw [decorate, mcgreen, decoration = {brace,raise=5pt,amplitude=10pt}, ultra thick] (0,0) --  (13.1901699437,0);
\end{tikzpicture}
\end{document}
```
$$
\begin{array}{c}
\begin{array}{c}
\displaystyle \frac{{\color{#FF6470} a}}{{\color{#68ABDF} b}} = \frac{{\color{#68ABDF} b}}{{\color{#99C47A} c}} \implies {\color{#68ABDF} b} = \phi \cdot {\color{#FF6470} a} \\
\displaystyle \frac{{\color{#FF6470} a}}{{\color{#68ABDF} b}} = \frac{{\color{#68ABDF} b}}{{\color{#99C47A} c}} = \frac{{\color{#68ABDF} b}}{{\color{#FF6470} a}+{\color{#68ABDF} b}} \\
{\color{#FF6470} a}^{2}+{\color{#FF6470} a}{\color{#68ABDF} b}={\color{#68ABDF} b}^{2}\text{ then }{\color{#68ABDF} b}^{2}-{\color{#FF6470} a}{\color{#68ABDF} b}-{\color{#FF6470} a}^{2}=0 \\
\displaystyle {\color{#68ABDF} b} = {\color{#FF6470} a}\cdot\frac{1 \pm \sqrt{5}}{2}
\end{array} \\ \\
\hline \\
\begin{array}{c}
\displaystyle \phi = \frac{1+\sqrt{5}}{2} \text{ and } \psi = \frac{1-\sqrt{5}}{2} \\
\begin{array}{rcl|rcl}
\phi & = & -\psi^{-1} & \psi & = & -\phi^{-1}  \\
\phi + \psi  & = & 1 & \phi \cdot \psi  & = & -2 \\
\phi - \psi & = & \sqrt{5} & \psi - \phi & = & -\sqrt{5} \\
\displaystyle\frac{\phi}{\psi} & = & -\phi-1 & \displaystyle\frac{\psi}{\phi} & = & -\psi-1 \\
\phi^{2} & = & \phi+1 & \psi^{2} & = & \psi+1
\end{array}
\end{array}

\end{array}
$$
# Sequences
-tx-
| Fibonacci Sequence | Lucas Sequence | $\boldsymbol{\phi}$ | $\boldsymbol{\psi}$ |
| :------------------------: | :-------------------------: | :--: | :---------------------------------: |
|       $F_{n} = F_{n-1} + F_{n-2}$         |  $L_{n} = L_{n-1} + L_{n-2}$  |    $\phi^{n} = \phi^{n-1} + \phi^{n-2}$ |    $\psi^{n} = \psi^{n-1} + \psi^{n-2}$  |
| $\displaystyle F_{n} = \frac{\phi^{n} - \psi^{n}}{\phi - \psi}$ |      $L_{n} = \phi^{n} + \psi^{n}$     | $\phi^{n} = F_{n} \cdot \phi + F_{n-1}$ | $\psi^{n} = F_{n} \cdot \psi + F_{n-1}$ |
|     ^^                    |              ^^                  | $\displaystyle \phi^{n} = \frac{L_{n} \cdot \phi + L_{n-1}}{\sqrt{5}}$ | $\displaystyle \psi^{n} = \frac{L_{n} \cdot \psi + L_{n-1}}{\sqrt{5}}$ |
| $\displaystyle F_{n} = \frac{L_{n+1} + L_{n-1}}{5}$| $L_{n} = F_{n+1} + F_{n-1}$ | $\displaystyle \phi^{n} = \frac{\phi^{n+1} + \phi^{n-1}}{\sqrt{5}}$|$\displaystyle \psi^{n} = \frac{\psi^{n+1} + \psi^{n-1}}{\sqrt{5}}$|
$$
\begin{array}{c}
\begin{array}{rl}
\left.\begin{array}{c}
	S_{0} = a \\
S_{1} = b \\
S_{n} = S_{n-1} + S_{n-2}
\end{array}\right\} \implies S_{n} & = F_{n-1} \cdot a + F_{n} \cdot b \\
 & = \displaystyle \frac{\phi^{n}(b - \psi a) - \psi^{n}(b - \phi a)}{\phi - \psi}
\end{array} \\ \\
\hline \\
\begin{array}{c}
G_{0} = a,\ G_{1} = b \\
G_{n} = A \cdot G_{n-1} + B \cdot G_{n-2} \\
\displaystyle \alpha = \frac{A + \sqrt{A^{2} - 4B}}{2},\ \beta = \frac{A - \sqrt{A^{2} - 4B}}{2} \\
\displaystyle G_{n} = \frac{\alpha^{n}(b - \beta a) - \beta^{n}(b - \alpha a)}{\alpha - \beta}
\end{array}
\end{array}
$$
## Binet's Formula
$$
F_{n}  = \frac{\phi^{n}-\psi^{n}}{\phi-\psi} = \frac{\phi^{n}-\psi^{n}}{\sqrt{5}}
$$
### Proof
$$
\begin{array}{c}
F_{n}  = F_{n-1}+F_{n-2} \\
\small\text{Lets assume that }F_{n} = c^{n}\text{. Then} \\
c^{n} = c^{n-1}+c^{n-2} \longrightarrow c^{n}-c^{n-1}-c^{n-2} = 0 \\
c^{2}-c-1 = 0 \longrightarrow\displaystyle c = \frac{1\pm \sqrt{5}}{2} \\
\displaystyle c_{1}  =  \frac{1+\sqrt{5}}{2},\,c_{2} = \frac{1-\sqrt{5}}{2} \\
c^{n} = k_{1}c_{1}^{n}+k_{2}c_{2}^{n} \\
F_{0}=c_{0}=k_{1}+k_{2}=0 \longrightarrow k_{1} = -k_{2} \longrightarrow c^{n}=k_{1}(c_{1}^{n}-c_{2}^{n}) \\
\displaystyle F_{1}=c_{1}=k_{1}(c_{1}-c_{2})=1 \longrightarrow k_{1}= \frac{1}{c_{1}-c_{2}} \longrightarrow c^{n} = \frac{c_{1}^{n}-c_{2}^{n}}{c_{1}-c_{2}} \\
\displaystyle F_{n}=\frac{c_{1}^{n}-c_{2}^{n}}{c_{1}-c_{2}}=\frac{\phi^{n}-\psi^{n}}{\phi-\psi}
\end{array}
$$
# Convolution
$$
(f * g)(t) = (g * f)(t) = f(t) * g(t) = \int_{-\infty}^{\infty} f(\tau) \cdot g(t - \tau) \, \mathrm{d}\tau = \int_{-\infty}^{\infty} f(t - \tau) \cdot g(\tau) \, \mathrm{d}\tau 
$$
## Convolution Theorem
$$
\begin{array}{rcl}
\mathcal{F}\{f * g\}  & = &  \mathcal{F}\{f\} \cdot \mathcal{F}\{g\} \\
\mathcal{F}\{f \cdot g\}  & = & \mathcal{F}\{f\} * \mathcal{F}\{g\}
\end{array}
$$
```tikz
\usepackage{tikz-cd}
%%\definecolor{clr}{RGB}{196,138,105}
%% \definecolor{clr}{RGB}{0,0,0}
 \definecolor{clr}{RGB}{255,255,255}

\tikzcdset{scale cd/.style={every label/.append style={scale=#1},
    cells={nodes={scale=#1}}}}

\begin{document}
\begin{tikzcd}[color=clr, row sep=small, scale cd=2]

	& \mathrm{Time\ Domain} 
		&\\
f \arrow[r] \arrow[dr] \arrow[bend right, start anchor=south west, end anchor=north west]{ddd}[left]{\mathcal{F}}
	& \times \arrow[r]
		& f \times g \arrow[bend left, start anchor=south east, end anchor=north east]{dddd}[right]{\mathcal{F}} \\ 
g \arrow[r] \arrow[ur] \arrow[bend right]{ddd}[left, start anchor=south west, end anchor=north west]{\mathcal{F}}
	& * \arrow[r] 
		& f * g \arrow[bend left]{dd}[left, start anchor=south east, end anchor=north east]{\mathcal{F}} \\

	& \mathrm{Frequency\ Domain} 
		& \\
\hat{f} \arrow[r] \arrow[dr] 
	& \times \arrow[r]
		& \hat{f} \times \hat{g} \\ 
\hat{g} \arrow[r] \arrow[ur] 
	& * \arrow[r]
		& \hat{f} * \hat{g} \\
\end{tikzcd}
\end{document}
```
# Dirac Delta Function
$$
\begin{array}{c}
\delta(x) \simeq \left\{ \begin{array}{lcl}
	+\infty  & : & x = 0 \\
0 & : & x \neq 0
\end{array}\right. \\
\displaystyle \int_{-\infty}^{\infty} \delta(x) \, \mathrm{d}x = 1 \\
f * \delta = \delta * f = f
\end{array}
$$
# Statistics
$$
\begin{array}{c}
\small \text{Let }X\text{ be a random variable with density }f(x). \\
\begin{array}{rcccl}
\mu & = &\displaystyle\int_{-\infty}^{\infty} xf(x)\,\mathrm{d}x & = & \text{The mean of } X\\
\sigma & = & \displaystyle\sqrt{\int_{-\infty}^{\infty} (x - \mu)^{2} f(x)\,\mathrm{d}x} & = & \text{The standard deviation of }X
\end{array}
\end{array}
$$
## Normal Distribution
$$
\displaystyle f(x) = \frac{1}{\sigma \sqrt{2\pi}}e^{\Huge -\frac{1}{2}\left(\frac{x - \mu}{\sigma}\right)^{2}}
$$
# Aleph-naught
$$
\begin{array}{c}
\aleph_{0} = \lvert \mathbb{N} \rvert = \lvert \mathbb{Q} \rvert = \lvert \mathbb{Z} \rvert = \lvert A \rvert \\
\small \boxed{\text{Where }A \subseteq \mathbb{Z}}
\end{array}
$$
# Vector Calculus
## Gradient
$$
\begin{array}{c}
\nabla f(p) = \left[\begin{array}{c}
\displaystyle\frac{\partial f}{\partial x_{1}} (p) \\
\vdots \\
\displaystyle \frac{\partial f}{\partial x_{n}} (p)
\end{array}\right] \\
\small \boxed{\text{Where }p  \in \mathbb{R}^{n}} 
\end{array}
$$
## Vector Area
$$
\displaystyle\mathbf{S}  = \int \hat{\mathbf{n}}\,\mathrm{d}S 
$$
## Divergence
$$
\begin{array}{c}
\begin{array}{rcl}
\displaystyle\left. \mathrm{div}\mathbf{F}\right|_{x}  =  \nabla  \cdot \mathbf{F} &  = &\displaystyle\lim_{V \to 0} \frac{1}{\lvert V \rvert } \iint_{S} \mathbf{F} \cdot \hat{\mathbf{n}} \,\mathrm{d}S \\
& =  &\displaystyle\sum_{i = 1}^{n} \frac{\partial F_{i}}{\partial x_{i}} 
\end{array} \\
\small \boxed{\text{Where }\mathbf{F} = (F_{1},F_{2},\cdots,F_{n})} 
\end{array}
$$
## Curl
$$
(\nabla \times \mathbf{F})(p) = \lim_{V \to 0} \frac{1}{\lvert V \rvert } \oint_{S} \hat{\mathbf{n}} \times \mathbf{F}\,\mathrm{d}S
$$
## Surface Integral
### Scalar Field
$$
\begin{array}{c}
\displaystyle\iint_{S}f\,\mathrm{d}S = \iint_{T} f(\mathbf{r}(s,t)) \left\lVert  \frac{\partial \mathbf{r}}{\partial s}  \times \frac{\partial \mathbf{r}}{\partial t}   \right\rVert \mathrm{d}s\,\mathrm{d}t \\
\small\boxed{\text{Where }\mathbf{r}(s,t)\text{ is a parameterization of }S\text{ and }(s,t)\text{ varies in }T.} 
\end{array}
$$
### Vector Field
$$
\begin{array}{c}
\displaystyle\iint_{S} \mathbf{v} \cdot \mathrm{d}\mathbf{S} = \iint_{S} \mathbf{v} \cdot \hat{\mathbf{n}}\,\mathrm{d}S = \iint_{T}\mathbf{v}(\mathbf{r}(s,t)) \cdot \left( \frac{\partial r}{\partial s} \times \frac{\partial r}{\partial t} \right)\,\mathrm{d}s\,\mathrm{d}t \\
\small\boxed{\text{Where }\mathbf{r}(s,t)\text{ is a parameterization of }S\text{ and }(s,t)\text{ varies in }T.} 
\end{array}
$$
## Flux
$$
\Phi_{F}  = \iint_{A} F \cdot \hat{\mathbf{n}}\,\mathrm{d}A
$$
# Least Squares Formula
$$
\begin{array}{c}
\small \text{Let }p_{1}, p_{2}, \cdots, p_{n}\text{ be }n\text{ distinct points with coordinates }\\
\small p_{1} = (x_{1},y_{1}),\, p_{2} = (x_{2}, y_{2}),\,\cdots,\, p_{n} = (x_{n}, y_{n}). \\
\small \text{We want to find the line that best fits the points.} \\
\small \text{The line has the equation } y = ax+b \\
\mathbf{A} = \left[\begin{array}{cc}
1 & x_{1} \\
1 & x_{2} \\
\vdots & \vdots \\
1 & x_{n}
\end{array}\right],\,
\vec{x} = \left[ \begin{array}{c}
a \\
b
\end{array} \right],\,
\vec{b} = \left[ \begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array} \right]  \\
\small \text{Formally, we want to minimize } \lVert \mathbf{A}\vec{x}-\vec{b} \rVert ^{2} \\
\vec{x} = (\mathbf{A}^{\text{T}}\mathbf{A})^{-1}\mathbf{A}^{\text{T}}\vec{b} \\
\end{array}
$$
# Generating Natural Numbers
$$
\begin{array}{c}
\left.\begin{array}{c}
	0 \in \mathbb{N} \\
S: \mathbb{N} \mapsto \mathbb{N} \\
{\Huge \forall}_{\! n \in \mathbb{N}} : S(n) \neq 0 \\
{\Huge \forall}_{\! n,m \in \mathbb{N}} : (n = m) \iff (S(n) = S(m))
\end{array}\right\}\text{Axioms that generate }\mathbb{N} \\ \\
\hline  \\
\begin{array}{c}
S(x) \equiv x+1 \\
x + 0 = 0 \\
x + S(y) = S(x+y) \\
x \times 0 = 0 \\
x \times S(y) = x \times y + x
\end{array} 
\end{array}
$$
# Bézier Curves
$$
\begin{array}{rcl}
\mathbf{B}(t) & = &\displaystyle\sum_{i=0}^{n} \binom{n}{i} t^{n-i} (1 - t)^{i} \mathbf{a}_{i} \\
\mathbf{B}'(t) & = & \displaystyle\sum_{i=0}^{n} \binom{n}{i} \mathbf{a}_{i} t^{n-i-1} (1-t)^{i-1} (n(1-t) - i)
\end{array}
$$
$$
\frac{\mathrm{d}}{\mathrm{d}t} \lVert \mathbf{B}_{1}(t) - \mathbf{B}_{2}(t) \rVert = \frac{[\mathbf{B}_{1}(t) - \mathbf{B}_{2}(t)] \cdot [\mathbf{B}_{1}'(t) - \mathbf{B}_{2}'(t)]}{\lVert \mathbf{B}_{1}(t) - \mathbf{B}_{2}(t) \rVert}
$$
# Vector Products
## Dot (Scalar) Product
$$
\begin{array}{c}
\begin{array}{rcl}
\mathbf{u} \cdot \mathbf{v} & = & \lVert \mathbf{u} \rVert \cdot \lVert \mathbf{v} \rVert \cos\alpha \\
 & = & \mathbf{u}_{x}\mathbf{v}_{x} + \mathbf{u}_{y}\mathbf{v}_{y} \\
 &  =  &\displaystyle \sum_{i = 1}^{n} \mathbf{u}_{i}\mathbf{v}_{i}  \\
 &  & \small\boxed{\text{Where }\mathbf{u}\text{ and }\mathbf{v}\text{ are }n\text{ dimensional vectors.}} 
\end{array} \\
\end{array}
$$
### Proof
$$
\begin{array}{rcl}
\tan(m + n) & = & \displaystyle \frac{\tan m+\tan n}{1-\tan m\cdot \tan n} \\
\tan -a & = & -\tan a \\ \\
\hline \\
A & = & \arctan u - \arctan v\\
\tan A & = & \tan(\arctan u - \arctan v)\\
\tan A & = & \displaystyle \frac{\tan \arctan u - \tan \arctan v}{1 + \tan \arctan u \cdot \tan \arctan v}\\
\tan A & = & \displaystyle \frac{u-v}{1+uv} \\
\displaystyle \arctan \frac{u-v}{1+uv} & = & \arctan u - \arctan v
\end{array}
$$
```tikz
%%\definecolor{clr}{RGB}{196,138,105}
%% \definecolor{clr}{RGB}{0,0,0}
\definecolor{clr}{RGB}{255,255,255}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[color = clr]
\draw[ultra thick] (0,0) -- (6,0) -- (6,8) -- cycle;
\node[align=center, text width=4cm] at (3,-.5) {\huge $b$};
\node[align=center, text width=4cm] at (6.5, 4) {\huge $a$};
\node[align=center, text width=4cm, rotate=53.13] at (2.7, 4.4) {\huge $\sqrt{a^2 + b^2}$};
\draw[ultra thick] (1,0) arc (0:53.13:1);
\node[align=right, text width=4cm] at (1, .8) {\Large $\displaystyle \arctan \frac{a}{b}$};
\end{tikzpicture}
\end{document}
```
$$
\begin{array}{c}
\displaystyle\cos \left(\arctan \frac{a}{b}\right) = \frac{b}{\sqrt{a^{2}+b^{2}}}
\end{array}
$$
$$
\begin{array}{rcl}
\mathbf{u}_{x}\mathbf{v}_{x}+\mathbf{u}_{y}\mathbf{v}_{y} & = & \lVert \mathbf{u} \rVert \cdot \lVert \mathbf{v} \rVert \cos \alpha \\
 & = & \displaystyle\sqrt{\mathbf{u}_{x}^{2}+\mathbf{u}_{y}^{2}} \cdot \sqrt{\mathbf{v}_{x}^{2}+\mathbf{v}_{y}^{2}} \cos \left(\arctan \frac{\mathbf{u}_{y}}{\mathbf{u}_{x}} - \arctan \frac{\mathbf{v}_{y}}{\mathbf{v}_{x}}\right) \\
 & = &\displaystyle \sqrt{\mathbf{u}_{x}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{x}^{2}\mathbf{v}_{y}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{y}^{2}} \cos \left(\arctan \left(  \frac{\displaystyle\frac{\mathbf{u}_{y}}{\mathbf{u}_{x}} - \frac{\mathbf{v}_{y}}{\mathbf{v}_{x}}}{\displaystyle1+\frac{\mathbf{u}_{y}}{\mathbf{u}_{x}}\frac{\mathbf{v}_{y}}{\mathbf{v}_{x}}}\right)\right)  \\
 & = &\displaystyle\sqrt{\mathbf{u}_{x}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{x}^{2}\mathbf{v}_{y}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{y}^{2}} \cos \left(\arctan \left(\frac{\displaystyle \frac{\mathbf{u}_{y}\mathbf{v}_{x}-\mathbf{u}_{x}\mathbf{v}_{y}}{\cancel{\mathbf{u}_{x}\mathbf{v}_{x}}}}{\displaystyle \frac{\mathbf{u}_{x}\mathbf{v}_{x}+\mathbf{u}_{y}\mathbf{v}_{y}}{\cancel{\mathbf{u}_{x}\mathbf{v}_{x}}}}\right) \right) \\
 & = & \sqrt{\mathbf{u}_{x}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{x}^{2}\mathbf{v}_{y}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{y}^{2}} \cos \left(\arctan \left(\frac{\displaystyle \mathbf{u}_{y}\mathbf{v}_{x}-\mathbf{u}_{x}\mathbf{v}_{y}}{\displaystyle \mathbf{u}_{x}\mathbf{v}_{x}+\mathbf{u}_{y}\mathbf{v}_{y}}\right) \right)  \\
 & = &\displaystyle\sqrt{\mathbf{u}_{x}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{x}^{2}\mathbf{v}_{y}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{y}^{2}} \frac{\mathbf{u}_{x}\mathbf{v}_{x} + \mathbf{u}_{y}\mathbf{v}_{y}}{\displaystyle\sqrt{(\mathbf{u}_{y}\mathbf{v}_{x}-\mathbf{u}_{x}\mathbf{v}_{y})^{2}+(\mathbf{u}_{x}\mathbf{v}_{x}+\mathbf{u}_{y}\mathbf{v}_{y})^{2}}} \\
 & = &\displaystyle\sqrt{\mathbf{u}_{x}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{x}^{2}\mathbf{v}_{y}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{y}^{2}} \frac{\mathbf{u}_{x}\mathbf{v}_{x} + \mathbf{u}_{y}\mathbf{v}_{y}}{\displaystyle\sqrt{\mathbf{u}_{y}^{2}\mathbf{v}_{x}^{2}\cancel{-2\mathbf{u}_{x}\mathbf{u}_{y}\mathbf{v}_{x}\mathbf{v}_{y}}+\mathbf{u}_{x}^{2}\mathbf{v}_{y}^{2}+\mathbf{u}_{x}^{2}\mathbf{v}_{x}^{2}\cancel{+2\mathbf{u}_{x}\mathbf{u}_{y}\mathbf{v}_{x}\mathbf{v}_{y}}+\mathbf{u}_{y}^{2}\mathbf{v}_{y}^{2}}} \\
 & = & \cancel{\sqrt{\mathbf{u}_{x}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{x}^{2}\mathbf{v}_{y}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{y}^{2}}} \frac{\displaystyle\mathbf{u}_{x}\mathbf{v}_{x} + \mathbf{u}_{y}\mathbf{v}_{y}}{\displaystyle\cancel{\sqrt{\mathbf{u}_{y}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{x}^{2}\mathbf{v}_{y}^{2}+\mathbf{u}_{x}^{2}\mathbf{v}_{x}^{2}+\mathbf{u}_{y}^{2}\mathbf{v}_{y}^{2}}}} \\
\mathbf{u}_{x}\mathbf{v}_{x}+\mathbf{u}_{y}\mathbf{v}_{y} & = & \mathbf{u}_{x}\mathbf{v}_{x}+\mathbf{u}_{y}\mathbf{v}_{y}
\end{array}
$$
# Dyck Series
$$
\begin{array}{c}
\small \text{The number of all the series with elements 0 and 1} \\
\small \text{such that the number of ones never exceeds number of zeros is} \\
\displaystyle \binom{m+n}{m} \cdot \frac{m-n+1}{m+1} \\
\small \text{Where }m\text{ is the number of ones and }n\text{ is number of zeros}
\end{array}
$$
# Graph Theory
$$
\begin{array}{rc}
1) & \displaystyle\sum_{v \in V} \deg(v)=2\lvert E \rvert  \\
2) & \lvert V \rvert - \lvert E \rvert + \lvert F \rvert =2 \\
\text{3.a}) & \displaystyle G\text{ is connected} \implies \lvert V \rvert -1 \leq \lvert E \rvert \leq \frac{\lvert V \rvert (\lvert V \rvert + 1)}{2} \\
\text{3.b}) & \displaystyle G\text{ is unconnected} \implies \lvert E \rvert \leq \frac{(\lvert V \rvert -1)(\lvert V \rvert -2)}{2} \\
\text{4.a}) & {\Huge \forall}_{\! v \in V}  \deg(v)\text{ is even} \iff G\text{ has Euler cycle} \\
\text{4.b}) & {\Huge \exists!}_{\{u,v\} \subset V} \deg(u),\deg(v)\text{ is odd} \iff G\text{ has Euler path} \\
5) & {\Huge \exists}_{\{u,v\} \subset V}: \deg(u)=\deg(v) \\
6) & {\Huge \exists}_{B,R \subset V} : [B \cup R = V] \land [B \cap R = \emptyset] \land \left[{\Huge \forall}_{\! e \in E}\ e \in B \times R \cup R \times B\right] \implies G\text{ is bipartite}
\end{array}
$$
# Asymptotic Notation
$$
\begin{array}{rrcl}
1) & f(n) \in \mathcal{O}(g(n)) & \iff & {\Huge \exists}_{c>0,n_{0}} : {\Huge \forall}_{\! n>n_{0}} \ \lvert f(n) \rvert \leq c \cdot g(n) \\
2) & f(n) \in \Omega(g(n)) & \iff & {\Huge \exists}_{c>0,n_{0}} : {\Huge \forall}_{\! n>n_{0}} \ f(n) \geq c \cdot g(n) \\
3) & f(n) \in \Theta(g(n)) & \iff & {\Huge \exists}_{c_{1},c_{2}>0,n_{0}} : {\Huge \forall}_{\! n>n_{0}} \ c_{1} \cdot g(n) \leq f(n) \leq c_{2} \cdot g(n) \\
4) & f(n) \in \Theta(g(n)) & \iff & f(n) \in \mathcal{O}(g(n)) \land f(n) \in \Omega(g(n)) \\
5) & f(n) \in \Theta(g(n)) & \iff & f(n) \in \mathcal{O}(g(n)) \land g(n) \in \mathcal{O}(f(n))
\end{array}
$$
# Euclidean Algorithm
$$
\gcd(a,b) = \gcd(b, a \bmod b)
$$
## Extended Euclidean Algorithm
$$
\begin{array}{c}
\boxed{{\Huge \exists}_{x,y \in \mathbb{Z}} : a \cdot x+b \cdot y = \gcd(a,b) } \\
\small\text{Let }x',y'\text{ be the coefficients for }b\text{ and }a\bmod b. \\
\small\text{Then }x'\cdot b+y'\cdot(a \bmod b)=\gcd(a,b) \\
\small\displaystyle\text{We can write }a \bmod b\text{ as }a-\left\lfloor  \frac{a}{b}  \right\rfloor \cdot b  \\
\begin{array}{rcl}
\gcd(a,b) & = & \displaystyle x'\cdot b+y'\cdot\left( a-\left\lfloor  \frac{a}{b}  \right\rfloor \cdot b \right)  \\
 & = &\displaystyle x'\cdot b+y'\cdot a-y'\cdot \left\lfloor  \frac{a}{b}  \right\rfloor \cdot b \\
 & = &\displaystyle a \cdot y'+b \cdot \left( x'-y' \cdot \left\lfloor  \frac{a}{b}  \right\rfloor \right)
\end{array} \\
\small\displaystyle\text{Then }x=y'\text{ and }y=\left( x'-y' \cdot \left\lfloor  \frac{a}{b}  \right\rfloor  \right)
\end{array}
$$
# Group Theory
## Pólya Counting
$$
\begin{array}{c}
\small\text{Let }X\text{ be a finite set and }G\text{ be a finite symmetry that acts on }X \\
\small\text{Suppose }Y\text{ is a finite set of colors and }Y^{X}\text{ the set of functions }X \to Y. \\
\small\text{The number of distinct colorings under the symmetries }G\text{ is:} \\
\displaystyle\lvert Y^{X}/G \rvert = \frac{1}{\lvert G \rvert }\sum_{g\in G}\lvert Y \rvert ^{c(g)}  \\
\small\boxed{\text{Where }c(g)\text{ is the cycle of }g.} 
\end{array} 
$$
## Lagrange's Theorem
$$
\lvert G / H \rvert = \left[G:H\right]  \cdot \lvert H \rvert 
$$
## Orbits and Quotients
$$
\begin{array}{c}
\small\text{Let }X\text{ be a set and }G\text{ be a group acting on }X. \\
\small\text{Then the orbit of a }x \in X\text{ is:} \\
G \cdot x = \{g \cdot x: g \in G\}  \\
\small\text{Let } Y\text{ be a subset of }X. \text{ Then:}\\
G \cdot Y = \{g \cdot y: g \in G \land y \in Y\}  \\
\small\text{The quotient of the group }G\text{ is:} \\
X / G = \{G \cdot x: x \in X\}  \\
\lvert X / G \rvert\text{ is the number of distinct elements of }X\text{ under }G \\
x \sim y \iff G \cdot x = G \cdot y \\
\end{array}
$$
## Fixed Points, Invariant and Stabilizer Subgroups
$$
\begin{array}{c}
\small\text{Let }X\text{ be a set and }G\text{ be a group acting on }X. \\
x\text{ is fixed under }g \iff g \cdot x = x\ \small(x \in X, g \in G) \\
\small\text{Let }Y\subset X \\
Y\text{ is invariant under }G \iff G \cdot Y = Y \\
Y\text{ is fixed under }G \iff {\Huge \forall}_{\! g \in G,y \in Y} g \cdot y=y \\
Y\text{ is fixed under }G \implies Y\text{ is invariant under }G \\
\small\text{The stabilizer subgroup of }G\text{ respect to }x\text{ is:} \\
G_{x}=\{g: g \in G\land g \cdot x=x\}
\end{array}
$$
# Rendering Equation
$$
L_{o}(\mathbf{x},w_{o},\lambda,t)=L_{e}(\mathbf{x},w_{o},\lambda,t)+\int _{\Omega}f_{r}(\mathbf{x},w_{i},w_{o},\lambda,t)L_{i}(\mathbf{x},w_{i},\lambda,t)(w_{i} \cdot \mathbf{n})\,\mathrm{d}w_{i} 
$$
