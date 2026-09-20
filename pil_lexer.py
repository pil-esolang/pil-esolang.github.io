from pygments.lexer import RegexLexer
from pygments.token import *

class PilLexer(RegexLexer):
   name = 'PIL'
   aliases = ['pil']
   filenames = ['*.pil']

   tokens = {
      'root': [
         (r';.*$', Comment.Single),
         (r'"', String.Double, 'string'),
         (r"'", String.Single, 'char'),
         (r'@[a-zA-Z][a-zA-Z0-9_-]*', Keyword.Pseudo),
         (r'[rR]?\$[0-9]+\b', Name.Variable.Magic),
         (r'\b(return|let|const)\b', Keyword),
         (r'[a-zA-Z][a-zA-Z0-9_-]*(?=\s*:)', Name.Variable),
         (r'[a-zA-Z][a-zA-Z0-9_.-]*(?=\s*\()', Name.Function),
         (r'[0-9]+\.[0-9]+', Number.Float),
         (r'[0-9]+', Number.Integer),
         (r'[a-zA-Z][a-zA-Z0-9_-]*', Name.Variable),
         (r'\s+', Whitespace),
         (r'.', Text),
      ],
      'string': [
         (r'\\.', String.Escape),
         (r'\{\}', String.Escape),
         (r'\$\{.*?\}', String.Interpol),
         (r'\$\[.*?\]', String.Interpol),
         (r'"', String.Double, '#pop'),
         (r'[^\\"]+', String.Double),
      ],
      'char': [
         (r'\\.', String.Escape),
         (r"'", String.Single, '#pop'),
         (r"[^\\']+", String.Single),
      ],
   }