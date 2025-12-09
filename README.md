# python-to-ts-react

Cette première version du projet consiste à implémenter un Pretty-Printer
L'outil est capable d'analyser une structure d'arbre syntaxique abstrait (AST) et de générer du code Python indenté et typé, avec pour objectif final la conversion vers TypeScript/React.

Implémentation de diverses fonctionnalités au sein de pretty.py:

1. Types (str_of_typ)
Primitifs : IntType, BoolType, StrType, AnyType, NoneType.

Composites et Génériques : ListType, TypeName (classes/alias), ParamType (ex: Tree[int]).

2. Expressions (str_of_exp)
Constantes : NoneCst, IntCst, StrCst, BoolCst.

Opérations Binaires : Arithmétique (Plus, Minus, Times), Comparaisons (Equal, Less...), Logique (And, Or).

Opérations Unaires : Not, Spread.

Structures de données : List, Tuple, Record, Subscript, Slice.

Fonctionnel : Call, Lambda, Cond.

3. Commandes (str_of_comm)
Flux de contrôle : IfThenElse, Return.

Pattern Matching : MatchList (sur listes), MatchData (sur classes).

Exceptions : TryExcept, Raise.

4. Déclarations (str_of_decl)
Structures : FunDef (fonctions typées), DataClass (@dataclass), TypeAlias.

Environnement : Import, ImportFrom, TypedVar, InitVar.

Prérequis
Python 3.10 ou supérieur (requis pour le support natif du match).

Tests et Validation
Le projet a été validé sur une suite de fichiers de tests complexes fournit et a compilé avec succès via Makefile