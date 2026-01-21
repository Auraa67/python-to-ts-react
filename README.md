# python-to-ts-react

Ce module (printer.py) constitue le coeur du transpilateur. Contrairement à la première version qui consistait à implementer pretty.py qui reformate du Python, ce module parcourt l'arbre syntaxique abstrait (AST) du Mini-Python pour générer du code TypeScript sémantiquement équivalent.

## Fonctionnalités implémentées dans printer.py

## 1. Types (str_of_typ)
Conversion du système de types Python vers TypeScript :
* Primitifs : int → number, bool → boolean, str → string, None → undefined, Any → any.
* Composites : ListType → T[], TupleType → [T1, T2], UnionType → T1 | T2.
* Fonctions : Conversion en signatures de fonctions fléchées ((arg: T) => U).
* Génériques : Support des types paramétrés (ex: Tree<T>).

## 2. Expressions (str_of_exp)
Adaptation de la sémantique et des opérateurs :
* Valeurs : None → undefined, True/False → true/false.
* Opérateurs :
  * Égalité stricte : Is et Equal → ===.
  * Logique : And → &&, Or → ||, Not → !.
  * Ternaire : Cond → test ? val : else.
* Structures :
  * List et Tuple → Tableaux [...].
  * Record → Génération d'objets discriminants (Tagged Unions) sous la forme { kind: "ID", value: {...} } pour faciliter le typage.
  * Slice → Utilisation de .slice().
* Primitives : Mapping des fonctions natives Python vers JS (ex: print → console.log, str → .toString(), functools.reduce → .reduce()).

## 3. Commandes (str_of_comm)
Traduction des structures de contrôle et du pattern matching :
* Contrôle : Conversion de IfThenElse avec blocs { ... }.
* Pattern Matching :
  * MatchList : Transpilé en vérifications de longueur (.length === 0) et déstructuration (const hd = arr[0]).
  * MatchData : Transpilé en chaînes de if/else vérifiant la propriété discriminante .kind.
* Exceptions :
  * Raise → throw new Error(...).
  * TryExcept → Bloc try { ... } catch (e) { ... } avec vérification de type (instanceof).

## 4. Déclarations (str_of_decl)
Génération des définitions de variables et de types :
* Variables : InitVar → const (immuable par défaut), InitVars → let (pour le destructuring).
* Fonctions : FunDef → function name(args): RetType { ... }.
* Classes de données : DataClass → Transpilé en interface TypeScript pour définir la forme des objets.
* Alias : TypeAlias → type Name = ...;.
* Imports : Conversion vers la syntaxe ES modules (import { ... } from "./module";).
---
## Utilisation et Validation

Le module printer.py est le point d'entrée par défaut lors de l'exécution du programme principal.

## Guide Rapide

*1. Transpilation (Génération de TypeScript)*
Pour convertir un fichier source Python en TypeScript et afficher le résultat sur la sortie standard :

bash
python3 main.py examples/points.py