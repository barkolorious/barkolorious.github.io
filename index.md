---
title: "Fundamentals of Computer Graphics"
permalink: /
layout: default
---

<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>

# 1 Introduction
## 1.1 Graphics Areas
## 1.2 Major Applications
## 1.3 Graphics APIs
## 1.4 Graphics Pipeline
## 1.5 Numerical Issues
Three "special" values for real numbers in IEEE floating-point:
- **Infinity ($\boldsymbol{\infty}$):** A valid number that is greater than all other valid numbers.
- **Minus Infinity ($\boldsymbol{-\infty}$):** A valid number that is less than all other valid numbers.
- **Not a Number ($\textbf{NaN}$):** An invalid number that arises from an operation with undefined consequences, such as zero divided by zero.
Rules of IEEE floating point:
- $(\forall a > 0) \displaystyle\frac{+a}{\infty} = +0$
- $(\forall a > 0) \displaystyle\frac{-a}{\infty} = -0$
- $(\forall a > 0) \displaystyle\frac{+a}{-\infty} = -0$
- $(\forall a > 0) \displaystyle\frac{-a}{-\infty} = -0$
- $(\forall a > 0) \displaystyle\frac{+a}{+0} = \infty$
- $(\forall a > 0) \displaystyle\frac{-a}{+0} = -\infty$
- $(\forall a > 0) \displaystyle\frac{+a}{-0} = -\infty$
- $(\forall a > 0) \displaystyle\frac{-a}{-0} = \infty$
- $\infty + \infty = \infty$
- $\infty - \infty = \text{NaN}$
- $\infty \times \infty = \infty$
- $\displaystyle \frac{\infty}{\infty} = \text{NaN}$
- $(\forall a > 0) \displaystyle \frac{\infty}{a}=\infty$
- $\displaystyle \frac{\infty}{0}=\infty$
- $\displaystyle\frac{0}{0}=\text{NaN}$
- $(\forall a) a < \infty$
- $(\forall a) a > -\infty$
- Any arithmetic or Boolean expression that includes $\text{NaN}$ results in $\text{NaN}$.
## 1.6 Efficiency
## 1.7 Designing and Coding Graphics Programs
### 1.7.1 Class Design
### 1.7.2 Float vs. Double
### 1.7.3 Debugging Graphics Programming

# 2 Miscellaneous Math
## 2.1 Sets and Mappings
- $a \in \mathbf{S}$ can be read as "$a$ is a member of set $\mathbf{S}$".
- If $\mathbf{A}$ and $\mathbf{B}$ are sets then $\mathbf{A} \times \mathbf{B}$ is called the Cartesian product of $\mathbf{A}$ and $\mathbf{B}$.
	- $\mathbf{A} \times \mathbf{B} = \{(a,b) : a \in \mathbf{A} \wedge b \in \mathbf{B}\}$
	- We use $\mathbf{A}^{2}$ to denote $\mathbf{A} \times \mathbf{A}$.
- Common sets include:
	- **$\mathbb{R}$:** the real numbers
	- **$\mathbb{R}^{+}$:** the nonnegative real numbers (includes 0)
	- **$\mathbb{R}^{2}$:** the ordered pair in the real 2D plane
	- **$\mathbb{R}^{n}$:** the points in the $n$-dimensional Cartesian space
	- **$\mathbb{Z}$:** the integers
	- **$S^{2}$:** the set of 3D point (points in $R^{3}$) on the unit circle
- If a function $f$ maps elements of $\mathbf{A}$ to $\mathbf{B}$ then it can be represented as $f : \mathbf{A} \mapsto \mathbf{B}$.
	- $f$ is a function $\iff (\forall a\in\mathbf{A})(\exists!b\in\mathbf{B}): (a,b)\in f$
	- If $f:\mathbf{A}\mapsto \mathbf{B}$ then $\mathbf{A}$ is the domain of $f$ and $\mathbf{B}$ is the target of $f$.
	- ```integer f(real)``` is equivalent to $f: \mathbb{R} \mapsto \mathbb{Z}$
	- $f(a)$ is called the image of $a$ and the image of $f(\mathbf{A})$ is called the range of $f$.
		- $f(\mathbf{A}) = \{f(a) : a\in\mathbf{A}\} \wedge f(\mathbf{A}) \subseteq \mathbf{B}$
### 2.1.1 Inverse Mappings
