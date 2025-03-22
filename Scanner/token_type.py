from enum import Enum

class TokenType(Enum):
    
   
    BOOLEAN = 'boolean'
    CLASS = 'class'
    EXTENDS = 'extends'
    PUBLIC = 'public'
    STATIC = 'static'
    VOID = 'void'
    MAIN = 'main'
    STRING = 'String'
    RETURN = 'return'
    INT = 'int'
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    SYSTEM_OUT_PRINTLN = 'System.out.println'
    LENGTH = '.length'
    TRUE = 'true'
    FALSE = 'false'
    THIS = 'this'
    NEW = 'new'
    NEW_INT = 'new int'
    NULL = 'null'
    

    ID = 'id'
    NUM = 'num'
    STR = 'str'
    
  
    MINUS = '-'
    PLUS = '+'
    TIMES = '*'
    AND = '&&'
    EQUAL = '='
    DOUBLE_EQUAL = '=='
    LESS_THEN = '<'
    GREATER_THEN = '>'
    LESS_EQUAL = '<='
    GREATER_EQUAL = '>='
    NOT = '!'
    NOT_EQUAL = '!='
    SEMICOLON = ';'
    COMMA = ','
    PERIOD = '.'
    
 
    LEFT_PAR = '('
    RIGHT_PAR = ')'
    LEFT_BRACKET = '['
    RIGHT_BRACKET = ']'
    LEFT_CURLY = '{'
    RIGHT_CURLY = '}'

    EOF = '$' 
