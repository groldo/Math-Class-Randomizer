---
title:  'Aufgaben'
author: ''
date: 15.01.2023
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

$$6 \cdot 6 =$$

$$5 \cdot 2 =$$

$$8 \cdot 3 =$$

$$8 \cdot 6 =$$

$$8 \cdot 3 =$$

$$4 \cdot 6 =$$

$$5 \cdot 2 =$$

$$7 \cdot 4 =$$

\end{multicols}

## Division

\begin{multicols}{2}

$$7 \colon 6 =$$

$$3 \colon 7 =$$

$$9 \colon 6 =$$

$$3 \colon 4 =$$

$$2 \colon 9 =$$

$$6 \colon 7 =$$

$$2 \colon 5 =$$

$$3 \colon 6 =$$

\end{multicols}
\newpage

## Dreisatz

### Aufgabe 1


Der Bäcker verkauft 1,5 Kilo Brot für 8 Euro. Wie viel kostet 1 Kilo Brot?

### Aufgabe 2


Kurt hat 100 Euro Weihnachtsgeld bekommen. Er gibt 40 Euro für eine neue Konsole aus und spart 25 Euro. Wie viel hat Kurt jetzt noch übrig?

\newpage

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
    \draw[black,very thick] (0, 4) rectangle (7, 0);
    \draw[black,xshift=0.5*7 cm] (0,0) -- (0,0) 
        node[below] { 350 };

    \draw[black,yshift=0.5*4 cm] (0,0) -- (0,0) 
        node[left] { 200 };

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
    \draw[black,very thick] (0, 7) rectangle (4, 0);
    \draw[black,xshift=0.5*4 cm] (0,0) -- (0,0) 
        node[below] { 320 };

    \draw[black,yshift=0.5*7 cm] (0,0) -- (0,0) 
        node[left] { 560 };

\end{scope}
\end{tikzpicture}
```
