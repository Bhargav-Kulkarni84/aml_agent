from src.profiles.account_profile import AccountProfile

class ProfileManager:

    def __init__(self):
        self.profiles = {}

    def get_profile(self, account_id):

        if account_id not in self.profiles:
            self.profiles[account_id] = AccountProfile(account_id)

        return self.profiles[account_id]