#!/usr/bin/env python3

import os

PATH_TO_PLUGIN = os.path.abspath(os.path.dirname(__file__))

# These folders are all mentioned in ../MANIFEST.in to ensure they are copied into the installed plugin
PATH_TO_TEMPLATES = os.path.join(PATH_TO_PLUGIN, "templates")
PATH_TO_STATIC = os.path.join(PATH_TO_PLUGIN, "static")
PATH_TO_AGENT_I18N = os.path.join(PATH_TO_PLUGIN, "agent/i18n")
PATH_TO_I18N = os.path.join(PATH_TO_PLUGIN, "i18n")

class KeyValueParser:
    """
    Helper class for parsing strings on the form
    id="hello there", age = 25, "cool key" = "cool \"value\"" ,key,key2

    Each entry is either a key=value pair, or just a key.
    whitespace around commas and equals signs are ignored.

    A key or value can either be unquoted or quoted.
    An unqouted string can not contain any spaces, commas, equals-signs, backslashes or quotes.
    In a quoted string, literal quotes can be escaped using \", and backslashes using \\

    A trailing comma at the end of the options list is allowed.
    """

    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.peek = None
        self.pop()

    def pop(self):
        c = self.peek
        self.pos += 1
        self.peek = self.text[self.pos] if self.pos < len(self.text) else None
        return c

    def skip_whitespace(self):
        while self.peek == " " or self.peek == "\t":
            self.pop()

    def readuntil(self, chars):
        """
        Reads until one of the provided chars is encountered.
        Does not read the stop char. Also stops at the end of the string.
        """
        read = ""
        while self.peek is not None and self.peek not in chars:
            read += self.pop()
        return read

    def parse_string(self):
        """
        Parses either a key or a value, ignoring leading spaces
        """
        self.skip_whitespace()
        if self.peek == '"':
            # We are parsing a quoted string
            self.pop() # Consume starting quoute
            string = ""
            while True:
                part = self.readuntil('"\\')
                string = string + part
                if self.peek == '"':
                    # Quoted string is over, return
                    self.pop() # Consume ending quote
                    return string
                elif self.peek == '\\':
                    self.pop() # Consume \
                    if self.peek == '"':
                        self.pop() # Consume escaped "
                        string = string + '"'
                    elif self.peek == '\\':
                        self.pop() # Consume escaped \
                        string = string + '\\'
                    else:
                        # The user had a rouge backslash, just include it verbatim
                        string = string + '\\'
                else:
                    raise ValueError(f"Expected '\"', got EOL, while parsing string \"{string} ...")
        elif self.peek is None:
            return None
        else:
            string = self.readuntil('" \t=,\\')
            if string == "":
                raise ValueError(f"Expected a non-empty string before character: '{self.peek}'")
            return string

    def extract(self):
        """ Extracts one (key,) or (key,value) tuple, or None if parsing is finished """

        key = self.parse_string()
        if key is None:
            return None

        self.skip_whitespace()
        if self.peek == "," or self.peek is None:
            # We are a key without a value
            self.pop() # Consume ,
            return (key,)
        elif self.peek != "=":
            raise ValueError(f"Expected a , or a = after key '{key}', got '{self.peek}'")

        self.pop() # Consume =
        value = self.parse_string()
        if value is None:
            raise ValueError(f"Expceted a value for key '{key}', got EOL")

        if self.peek != "," and self.peek is not None:
            raise ValueError(f"Expected a , or EOL after '{value}', got '{self.peek}'")

        self.pop() # Consume the ',', if there was one

        return (key, value)

    def extract_all(self):
        """ Extracts all (key,) and (key,value) tuples into a list """
        extracted = []
        while True:
            extract = self.extract()
            if extract is not None:
                extracted.append(extract)
            else:
                return extracted
