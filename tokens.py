import re

CLEAN_TOKEN_STEP1 = r'[\=;\\"\<\>,)(]'
CLEAN_TOKEN_STEP2 = r"[']"

class Token:
    def __init__(self, name, regex, blacklist=None, display_order=1):
        self.name = name
        self.regex = regex
        self.blacklist = blacklist or []
        self.display_order = display_order
    
    def get_name(self):
        return self.name
    
    def get_regex(self):
        return self.regex

    def get_blacklist(self):
        return self.blacklist

    def get_display_order(self):
        return self.display_order

class TokenCombo:
    def __init__(self, name, tokens_list=None):
        self.tokens_list = tokens_list or []
        self.name = name
    
    def get_tokens(self):
        return self.tokens_list
    
    def get_name(self):
        return self.name

def init_tokens_map():
    tokens_list = [
        Token('AMAZON_AWS', r'([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}', ['EXAMPLE']),
        Token('AZURE_SERVICE_PRINCIPAL', r'([0-9a-f]{40}-[0-9a-f]{12}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}-[0-9a-f]{12})'),
        # Add more tokens...
    ]

    tokens_combo = [
        TokenCombo('AZURE_CREDENTIALS', [
            Token('AZURE_TENANT_ID', r'(tenant="?[0-9a-f]{36}"?)', None, 1),
            Token('AZURE_CLIENT_ID', r'(client_id="?[0-9a-f]{32}"?)', None, 2)
        ]),
        # Add more token combos...
    ]
 
    return tokens_list, tokens_combo

def clean_tokens(tokens):
    cleaned_tokens = []
    for token in tokens:
        cleaned_token = re.sub(CLEAN_TOKEN_STEP1, '', token)
        cleaned_token = re.sub(CLEAN_TOKEN_STEP2, '', cleaned_token)
        cleaned_tokens.append(cleaned_token)
    return cleaned_tokens

if __name__ == "__main__":
    tokens_list, tokens_combo = init_tokens_map()
    print(tokens_list)
    print(tokens_combo)
