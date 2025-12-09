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

Tests et Validation

Le projet compile et s'exécute avec succès via le Makefile. La validation a été effectuée à la fois sur les tests fournis et sur mes tests personnels (dans le répertoire my_test), qui ont tous été passés avec succès.

Voici un guide rapide à ajouter à votre documentation ou pour votre propre usage :

Guide de Tests Rapide

NB: les tests se trouvent dans le dossier Examples.

1. Lancer la suite de tests fournie (Makefile) Pour exécuter automatiquement la validation sur les fichiers de tests par défaut :

make

Cela génère les sorties et vérifie la correspondance des arbres syntaxiques (AST).

2. Lancer les tests personnels (my_test/):

Visualiser le code généré :

python3 main.py --pretty my_test/points.py

Vérifier et exécuter le résultat (Test complet) :

python3 main.py --pretty my_test/points.py | python3
