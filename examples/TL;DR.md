# HOW TO WRITE A PL

```
SOURCE CODE -> AST -> ANALYSIS -> { EVALUATED
   \__PARSING__/     (OPTIONAL)   { VM BYTE CODE
                                  { MACHINE CODE
                                  { TRANSPILED SOURCE CODE
```

There are textbooks dedicated to each step in this pipeline. Focus on the one
you're most excited about.

### CONCEPT

figure out what your language does -- it can be any kind of computation you want.

We're going to flesh out an absurd little language where the unary operators 'P' and 'M' act on unit 'A'.

### PARSING
- identify the grammar

```
OPERATOR := 'P' | 'M'
UNIT := 'A'
EXPRESSION := { UNIT | UNIT OPERATOR }
```

a program might look like `AAAPAMAPP`.

- identify the data structure for the abstract syntax tree (AST).

 ```
EXPR :: ENUM(UNIT, TUPLE(OPERATOR, UNIT))
PROGRAM :: LIST[EXPR]
 ```

our ast might look like `[A, A, {P, A}, {M, A}, {P, {P, A}}]`.

- implementation in psuedo code

```
function tokenize(src) :: tokens {
    return string_to_array(src).reverse()
}

function parse(tokens, ast) :: ast {
    if (tokens.length === 0) return ast
    if (tokens.head == 'A') return parse(tokens.tail, prepend(tokens.head, ast))
    return parse(tokens.tail, prepend({tokens.head, ast.head}, ast.tail))
}
```

### EVALUATION v1

Here's where we interpret our AST -- that is to say, assign "meaning". I'm
deciding that 'A' means 1 Apple, 'P' means add an apple, and 'M' means remove
1 apple.

taking our sample ast above, the output should be `AAAAAAA`. fascinating, I know.

- implementation in psuedo code

```
function evaluate(ast) {
    if (ast.head == {'P', expr}) return prepend('A', evaluate(expr)).concat(evaluate(ast.tail))
    if (ast.head == {'M', expr}) return evaluate(expr).tail.concat(ast.tail)
    return prepend('A', evaluate(tail(ast)))
}
```

### EVALUATION v2

The shrewd programmer will have realized that the grammar for this PL is so
simple that evaluation can be performed directly on the tokens. If you can get
away with it, there's nothing wrong with this.

- simplified evaluation pseudo code

```
function evaluate(src) {
    return string_to_array(src).fold(function (accumulator, token) {
        if (token.head == 'A' or 'P') return prepend('A', accumulator)
        if (token.head == 'M') return return accumulator.tail
    }, [])
}
```
