# EXAMPLE GRAMMAR
#  EXPR := "(" BOOL OP BOOL ")"
#  BOOL := "TRUE" | "FALSE"
#  OP := "AND" | "OR"

# PROGRAM SOURCE CODE
PROGRAM = "((TRUE OR FALSE) AND TRUE)";

# TOKENIZED PROGRAM
TOKENS = ["(", "(", "TRUE", "OR", "FALSE", ")", "AND", "TRUE", ")"]

# PARSED AST
# Your language is NOT REQUIRED to have a parser. If your interpreter only
# consumes raw AST nodes that's perfectly acceptable.
MATH_EXPRESSION = {
  "type": "OP",
  "name": "AND",
  "left": {
    "type": "OP",
    "name": "OR",
    "left": { "type": "BOOL", "value": True },
    "right": { "type": "BOOL", "value": False },
  },
  "right": { "type": "BOOL", "value": True },
};

# INTERPRETER
# evaluates AST expression
def interpreter(expr):
    match expr["type"]:
        case "OP":
            match expr["name"]:
                case "AND":
                    return interpreter(expr["left"]) and interpreter(expr["right"])
                case "OR":
                    return interpreter(expr["left"]) or interpreter(expr["right"])
        case "BOOL":
            return expr["value"]

# TESTS
assert(True == interpreter(MATH_EXPRESSION))

FALSY_EXPRESSION = {
  "type": "OP",
  "name": "OR",
  "left": {
    "type": "OP",
    "name": "AND",
    "left": { "type": "BOOL", "value": True },
    "right": { "type": "BOOL", "value": False },
  },
  "right": { "type": "BOOL", "value": False },
};
assert(False == interpreter(FALSY_EXPRESSION))
