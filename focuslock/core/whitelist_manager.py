import json

class WhitelistManager:
    def __init__(self, settings_path='focuslock/config/settings.json'):
        self.settings_path = settings_path
        self.whitelist = self.load_whitelist()

    def load_whitelist(self):
        try:
            with open(self.settings_path, 'r') as f:
                settings = json.load(f)
                return settings.get('whitelist', [])
        except FileNotFoundError:
            return []

    def is_whitelisted(self, process_name):
        return process_name in self.whitelist

    def add_to_whitelist(self, process_name):
        if process_name not in self.whitelist:
            self.whitelist.append(process_name)
            self.save_whitelist()

    def remove_from_whitelist(self, process_name):
        if process_name in self.whitelist:
            self.whitelist.remove(process_name)
            self.save_whitelist()

    def save_whitelist(self):
        with open(self.settings_path, 'r+') as f:
            settings = json.load(f)
            settings['whitelist'] = self.whitelist
            f.seek(0)
            json.dump(settings, f, indent=2)
            f.truncate()
