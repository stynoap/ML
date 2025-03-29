# La regressione

## introduzione
la regressione lineare è uno dei più semplici algoritmi di machine learning ed è usato per modellare la relazione tra una variabile dipendente (y) e una o più variabili indipendenti (x). L'obiettivo della regressione lineare è trovare la retta migliore che descriva l'andamento dei dati in modo da poter fare delle previsioni per nuovi valori. 

**formula della regressione lineare**

 la regressione lineare semplice ha questa formula matematica
**Y = mx + b**

**y** è il valore predetto 
**x** è la variabile indipendente
**m** è la pendenza della retta o anche coefficiente
**b** è l'intercetta (il valore di **y** quando **x=0**)

**nel caso avessimo più di una variabile indipendente** si usa invece la **regressione lineare multipla** la cui formula diventa Y=b0 + b1x1 + b2x2 + ... bnxn, in cui ogni **bn** è un coefficiente, un peso che il modello apprende dai dati 

Per una regressione lineare semplice, i coefficienti possono essere calcolati con le seguenti formule:

- **m = Σ((xᵢ - x̄)(yᵢ - ȳ)) / Σ((xᵢ - x̄)²)**
- **b = ȳ - m * x̄**
- 
Dove:
- **x̄** è la media dei valori di **x**
- **ȳ** è la media dei valori di **y**


### Esempio pratico

Riprendendo l'esempio precedente, calcoliamo i coefficienti per i dati forniti:

- Superfici in metri quadrati: [50, 80, 100, 150]
- Prezzi corrispondenti: [150.000, 200.000, 250.000, 350.000]

1. Calcoliamo le medie:
   - **x̄ = (50 + 80 + 100 + 150) / 4 = 95**
   - **ȳ = (150.000 + 200.000 + 250.000 + 350.000) / 4 = 237.500**

2. Calcoliamo **m**:
   - Numeratore: Σ((xᵢ - x̄)(yᵢ - ȳ)) = (50-95)(150.000-237.500) + ... = 12.500.000
   - Denominatore: Σ((xᵢ - x̄)²) = (50-95)² + ... = 2500
   - **m = 12.500.000 / 2500 = 50**

3. Calcoliamo **b**:
   - **b = ȳ - m * x̄ = 237.500 - 50 * 95 = -237.500**

La retta risultante è quindi:
**Y = 50x - 237.500**

### Visualizzazione

Tracciando i dati e la retta risultante su un grafico, possiamo osservare come il modello approssima la relazione tra superficie e prezzo.

### m (pendenza o coefficiente angolare):

Indica quanto cambia il valore predetto Y per ogni unità di incremento della variabile indipendente x.
In altre parole, rappresenta la "ripidità" della retta e la direzione della relazione tra x e y:
Se m > 0, la relazione è positiva: all'aumentare di x, anche y aumenta.
Se m < 0, la relazione è negativa: all'aumentare di x, y diminuisce.
Se m = 0, non c'è relazione tra x e y (la retta è orizzontale).
Esempio: Se m = 50, significa che per ogni incremento di 1 unità in x, il valore di Y aumenta di 50.

b (intercetta):

È il valore di Y quando x = 0.
Rappresenta il punto in cui la retta interseca l'asse Y.
Concettualmente, è il valore iniziale di Y prima che x inizi a influenzarlo.
Esempio: Se b = -237.500, significa che quando x = 0, il valore predetto di Y è -237.500.

Relazione tra m e b:
m controlla l'inclinazione della retta, mentre b sposta la retta verso l'alto o verso il basso sull'asse Y.
Insieme, determinano completamente la posizione e l'orientamento della retta nel piano cartesiano.


** vedi regression .py per un esempio concreto **
## Cosa puoi capire dalla regressione lineare?

La regressione lineare è uno strumento potente che ti permette di capire e modellare la relazione tra una variabile dipendente (**Y**) e una o più variabili indipendenti (**X**). Ecco cosa puoi capire dalla regressione lineare:

### 1. Relazione tra le variabili
- Ti aiuta a determinare se esiste una relazione tra la variabile indipendente (**X**) e la variabile dipendente (**Y**).
- Ad esempio, puoi capire se all'aumentare della superficie di una casa (X), il prezzo (Y) aumenta, diminuisce o rimane invariato.

### 2. Direzione della relazione
- **Coefficiente angolare (m)**:
  - Se **m > 0**, la relazione è positiva: all'aumentare di **X**, anche **Y** aumenta.
  - Se **m < 0**, la relazione è negativa: all'aumentare di **X**, **Y** diminuisce.
  - Se **m = 0**, non c'è relazione tra **X** e **Y**.

### 3. Forza della relazione
- La pendenza della retta (**m**) indica quanto **Y** cambia per ogni unità di incremento in **X**.
- Una pendenza più ripida (valore assoluto di **m** maggiore) indica una relazione più forte tra le variabili.

### 4. Valore iniziale di Y
- **Intercetta (b)**:
  - Ti dice il valore di **Y** quando **X = 0**.
  - Questo è utile per capire il punto di partenza della relazione.

### 5. Fare previsioni
- Una volta calcolata l'equazione della retta (**Y = mx + b**), puoi usarla per fare previsioni su nuovi valori di **X**.
- Ad esempio, puoi stimare il prezzo di una casa con una superficie che non è presente nei dati originali.

### 6. Identificare tendenze
- La regressione lineare ti permette di identificare tendenze nei dati, come l'andamento generale di un mercato o il comportamento di una variabile nel tempo.

### 7. Valutare l'accuratezza del modello
- Puoi calcolare metriche come l'errore quadratico medio (MSE) o il coefficiente di determinazione (**R²**) per valutare quanto bene il modello si adatta ai dati.
- **R²** indica la percentuale di variazione di **Y** spiegata da **X**:
  - **R² = 1**: il modello spiega perfettamente i dati.
  - **R² = 0**: il modello non spiega nulla.

### 8. Individuare anomalie
- Analizzando i residui (le differenze tra i valori osservati e quelli predetti), puoi individuare anomalie o outlier nei dati.

### Applicazioni pratiche
- **Economia**: Prevedere i prezzi di mercato.
- **Finanza**: Analizzare il rendimento di un investimento in base a fattori economici.
- **Medicina**: Studiare la relazione tra dosaggio di un farmaco e risposta del paziente.
- **Ingegneria**: Modellare il comportamento di un sistema fisico.

In sintesi, la regressione lineare ti permette di comprendere, quantificare e prevedere relazioni tra variabili, rendendola uno strumento fondamentale in molte discipline.
### Come calcolare **R²**

Il coefficiente di determinazione **R²** misura quanto bene il modello di regressione lineare si adatta ai dati. Indica la proporzione della variazione della variabile dipendente (**Y**) che è spiegata dalla variabile indipendente (**X**) attraverso il modello.

#### Formula di **R²**
**R² = 1 - (SS_res / SS_tot)**

Dove:
- **SS_res** (Somma dei quadrati dei residui): La somma delle differenze al quadrato tra i valori osservati (**yᵢ**) e quelli predetti (**ŷᵢ**):
  **SS_res = Σ(yᵢ - ŷᵢ)²**
- **SS_tot** (Somma totale dei quadrati): La somma delle differenze al quadrato tra i valori osservati (**yᵢ**) e la media dei valori osservati (**ȳ**):
  **SS_tot = Σ(yᵢ - ȳ)²**

#### Interpretazione di **R²**
- **R² vicino a 1**: Il modello spiega bene i dati.
- **R² vicino a 0**: Il modello non spiega i dati.
- **R² negativo**: Può accadere se il modello è molto scarso (ad esempio, se non è lineare).
