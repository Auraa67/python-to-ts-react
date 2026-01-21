# python-to-ts-react

Un outil de conversion de code Python typé vers TypeScript/React.

## Description

Ce projet implémente un compilateur qui analyse du code Python typé et le convertit en TypeScript. L'outil utilise un Pretty-Printer pour analyser la structure d'arbre syntaxique abstrait (AST) et générer du code TypeScript idiomatique.

## Prérequis

- Python 3.10 ou supérieur (pour le support de la syntaxe moderne avec `match/case` et génériques)
- Aucune dépendance externe requise (utilise uniquement la bibliothèque standard Python)

## Installation

```bash
# Cloner le repository
git clone https://github.com/Auraa67/python-to-ts-react.git
cd python-to-ts-react
```

## Usage

### Conversion Python → TypeScript

Pour convertir un fichier Python en TypeScript :

```bash
python3 main.py <fichier.py>
```

**Exemple :**
```bash
python3 main.py Examples/test0.py
```

**Sortie TypeScript :**
```typescript
function compose<A, B, C>(f: (arg0: A) => B, g: (arg0: B) => C): (arg0: A) => C {
    return ((x) => g(f(x)));
}
```

### Pretty-Printing Python

Pour reformater et afficher un fichier Python :

```bash
python3 main.py --pretty <fichier.py>
```

**Exemple :**
```bash
python3 main.py --pretty Examples/test0.py
```

### Autres Options

- `--parse` : Afficher l'AST d'un fichier source
- `--regions` : Afficher l'AST avec les régions
- `--check` : Vérifier que deux fichiers ont le même AST

```bash
# Afficher l'AST
python3 main.py --parse Examples/test0.py

# Comparer deux fichiers (vérifier que l'AST est identique)
python3 main.py --check Examples/test0.py Examples/PY/test0.py
```

## Fonctionnalités Supportées

### 1. Types (str_of_typ)
- **Primitifs** : `IntType`, `BoolType`, `StrType`, `AnyType`, `NoneType`
- **Composites et Génériques** : `ListType`, `TypeName` (classes/alias), `ParamType` (ex: `Tree[int]`)

### 2. Expressions (str_of_exp)
- **Constantes** : `None`, entiers, chaînes, booléens
- **Opérations Binaires** : Arithmétique (`+`, `-`, `*`), Comparaisons (`==`, `<`, etc.), Logique (`and`, `or`)
- **Opérations Unaires** : `not`, spread (`...`)
- **Structures de données** : Listes, tuples, records, subscript, slice
- **Fonctionnel** : Appels de fonction, lambda, expressions conditionnelles

### 3. Commandes (str_of_comm)
- **Flux de contrôle** : `if/then/else`, `return`
- **Pattern Matching** : Matching sur listes et classes
- **Exceptions** : `try/except`, `raise`

### 4. Déclarations (str_of_decl)
- **Structures** : Définitions de fonctions typées, `@dataclass`, alias de types
- **Environnement** : `import`, `from...import`, variables typées, variables d'initialisation

## Tests

Les fichiers de test se trouvent dans le dossier `Examples/`.

### Exécuter la suite complète de tests

```bash
cd Examples
make
```

Cette commande :
1. Génère les fichiers Python formatés dans `PY/`
2. Génère les fichiers TypeScript convertis dans `TS/`
3. Vérifie la correspondance des AST

### Tester un fichier spécifique

```bash
# Visualiser le code généré
python3 main.py --pretty Examples/test0.py

# Vérifier et exécuter le résultat
python3 main.py --pretty Examples/test0.py | python3

# Convertir en TypeScript
python3 main.py Examples/test0.py > output.ts
```

## Structure du Projet

```
.
├── main.py           # Point d'entrée principal
├── parsers.py        # Analyseur syntaxique Python
├── pretty.py         # Pretty-Printer pour Python
├── printer.py        # Générateur de code TypeScript
├── absyn.py          # Définitions de l'AST
├── util.py           # Utilitaires
├── error.py          # Gestion des erreurs
└── Examples/         # Fichiers de test et exemples
    ├── test*.py      # Tests unitaires
    └── Makefile      # Automation des tests
```

## Validation

Le projet a été validé avec succès sur l'ensemble des tests fournis. Tous les tests passent et la génération de code TypeScript est fonctionnelle.
