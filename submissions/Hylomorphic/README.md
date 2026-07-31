# Hylomorphic 
Hylomorphic is an interactive, visual programming language that graphically builds and evaluates Abstract Syntax Trees. Its syntax, naming, and semantics are explicitly inspired by category theory.

## Hylomorphism
In category theory, a hylomorphism is an anamorphism (corecursion) followed by a catamorphism (recursion). In this sense, unfolding an AST from a seed structure is corecursive, while evaluating that AST down to a single value is recursive. An interpreter, therefore, is fundamentally a hylomorphism.

## The rest of the weird naming
As you might have guessed, the rest of the weired naming is also inspired by category theory. 

## How Hylomprphic fits the lang jam theme (Corecursion)
As outlined above, a Hylomorphism is an anamorphism (corecursion) followed by a catamorphism (recursion). In this sense, building an AST is corecursion.

There is yet another link to corecursion: Hylomorphic is implemented in Claro, a language developed by Jason Steving, who was also one of the organizers of the first programming language jam. Although Claro was not developed in the jam, this shows how the jam's languages inspire other languages and therefore corecursively unfold new programming language ideas.

## AI usage

AI was used to help with the MODULE.bazel initial setup


### Run these commands from some dir in the project tree.
bazel build //example:Hylomorphic_bin
bazel run //example:Hylomorphic_bin
