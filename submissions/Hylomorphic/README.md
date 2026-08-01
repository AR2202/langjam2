# Hylomorphic 
Hylomorphic is an interactive, visual programming language that graphically builds and evaluates Abstract Syntax Trees. Its syntax, naming, and semantics are explicitly inspired by category theory.

## Hylomorphism
In category theory, a hylomorphism is an anamorphism (corecursion) followed by a catamorphism (recursion). In this sense, unfolding an AST from a seed structure is corecursive, while evaluating that AST down to a single value is recursive. An interpreter, therefore, is fundamentally a hylomorphism.

## The rest of the weird naming
As you might have guessed, the rest of the weired naming is also inspired by category theory. 

## Building the AST
Hylomorphic has a fundamentally different concept from normal text-based languages. Instead of writing source code, the user builds an AST graphically and evaluates it. The AST can have nodes and terminals (leafs). Each fully saturated node has 2 children.

### Node types
* Product: a product node
* Coproduct: a coproduct (sum) node

### Leaf types
Hylomorphic supports 2 types of terminals:
* integers
* booleans

The tree is extended when the user enters a node or leaf type they would like to enter. The new node or leaf is always appended to the leftmost empty space. If the tree has only terminals in all final layers, it is fully saturated. Nothing can be added to it. It can only be evaluated.

## Evaluating the AST
Evaluation happens by depth-first traversal. Only fully saturated nodes can be evaluated. Nodes which aren't fully saturated will remain as-is. The tree can be evaluated to another tree or a terminal, depending on whether it is fully saturated. 

### Evaluation rules
A product node with 2 integer children multiplies the integers. A categorical coproduct in corresponds to a sum in the sense of "sum types". A coproduct node is therefore a sum node. It sums its integer children.
A product node with 2 boolean children performs AND, as AND is the product in the Bool category. A coproduct node performs OR on 2 boolean children for the equivalent reason.

A node with mixed children casts the boolean to an integer as follows:
TRUE corresponds to 1, as TRUE is the terminal object in the Bool category and 1 (the singleton set) is the terminal object in Set.
FALSE corresponds to 0, as FALSE is the initial object in the Bool category and 0 (the empty set) is the initial object in Set.


## TUI
Although Hylomorphic is intended as a visual programming language, it currently only has a TUI, due to LoC restriction and no-dependencies challenge of the jam. The graphical representation of the tree is an ASCII string in the terminal.

### Example of an AST


## How Hylomprphic fits the lang jam theme (Corecursion)
As outlined above, a Hylomorphism is an anamorphism (corecursion) followed by a catamorphism (recursion). In this sense, building an AST is corecursion. Both the name and the idea of visualizing an AST are related to corecursion.

There is yet another link to corecursion: Hylomorphic is implemented in Claro, a language developed by Jason Steving, who was also one of the organizers of the first programming language jam. Although Claro was not developed in the jam, this shows how the jam's languages inspire other languages and therefore corecursively unfold new programming language ideas.

## AI usage

AI was used to help with the MODULE.bazel initial setup


### Run these commands from some dir in the project tree.
bazel build //example:Hylomorphic_bin
bazel run //example:Hylomorphic_bin
