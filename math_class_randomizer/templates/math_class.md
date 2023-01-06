---
title:  ''
author: ''
date: 06.01.2023
keywords: []
aspectratio: 169
pagestyle: 'plain'
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
header-includes: |
    \usepackage{tikz}
    \usepackage{diagbox}
    \let\oldsection\section
    \renewcommand\section{\clearpage\oldsection}
    \usepackage{caption}
    \usepackage{multicol}
	\captionsetup[figure]{
        name=,
        labelsep=none,
        labelformat=empty}
section-titles: false
toc: false
lang: de
---

## Multiplikation

\begin{multicols}{2}

$$8 \cdot 7 =$$

$$7 \cdot 4 =$$

$$8 \cdot 6 =$$

$$5 \cdot 7 =$$

$$6 \cdot 7 =$$

$$4 \cdot 9 =$$

$$4 \cdot 3 =$$

$$9 \cdot 2 =$$

\end{multicols}

## Division

\begin{multicols}{2}

$$8 \colon 2 =$$

$$7 \colon 7 =$$

$$2 \colon 5 =$$

$$7 \colon 9 =$$

$$9 \colon 3 =$$

$$8 \colon 6 =$$

$$4 \colon 8 =$$

$$6 \colon 9 =$$

\end{multicols}

## Dreisatz

### Aufgabe 1

6 Stücke  Butter wiegen zusammen 300 Gramm. Wie viel Gramm wiegen 4 Stücke?

### Aufgabe 1

In 5 Dachböden leben 40 Mäuse. Wie viele Mäuse leben in 13 Dachböden?

## Flächenberechnung


### Aufgabe 1
Berechne die Fläche

```{=latex}
\begin{tikzpicture}[scale=.35]\footnotesize
\pgfmathsetmacro{\xone}{-.4}
\pgfmathsetmacro{\xtwo}{ 40.4}
\pgfmathsetmacro{\yone}{-.4}
\pgfmathsetmacro{\ytwo}{10.4}

\begin{scope}

    % grid
    \draw[step=1cm,gray,very thin] (\xone,\yone) grid (\xtwo,\ytwo);
    % axes
    %\draw[gray,thick,-] (\xone, 0) -- (\xtwo, 0) node[right] {};
    %\draw[gray,thick,-] (0, \yone) -- (0, \ytwo) node[above] {};
    % rectangle
    \draw[black,very thick] (0, 3) rectangle (9, 0);
    \draw[black,xshift=0.5*9 cm] (0,0) -- (0,0) 
        node[below] { 540 };

    \draw[black,yshift=0.5*3 cm] (0,0) -- (0,0) 
        node[left] { 180 };

\end{scope}
\end{tikzpicture}
```

### Aufgabe 2
Berechne die Fläche

```{=latex}
\begin{tikzpicture}[scale=.35]\footnotesize
\pgfmathsetmacro{\xone}{-.4}
\pgfmathsetmacro{\xtwo}{ 40.4}
\pgfmathsetmacro{\yone}{-.4}
\pgfmathsetmacro{\ytwo}{10.4}

\begin{scope}

    % grid
    \draw[step=1cm,gray,very thin] (\xone,\yone) grid (\xtwo,\ytwo);
    % axes
    %\draw[gray,thick,-] (\xone, 0) -- (\xtwo, 0) node[right] {};
    %\draw[gray,thick,-] (0, \yone) -- (0, \ytwo) node[above] {};
    % rectangle
    \draw[black,very thick] (0, 6) rectangle (8, 0);
    \draw[black,xshift=0.5*8 cm] (0,0) -- (0,0) 
        node[below] { 240 };

    \draw[black,yshift=0.5*6 cm] (0,0) -- (0,0) 
        node[left] { 180 };

\end{scope}
\end{tikzpicture}
```
