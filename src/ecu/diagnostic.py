class DiagnosticService:
    def __init__(self):
        self.session = 0x01

    def change_session(self, session):
        if session not in (0x01, 0x02, 0x03):
            raise ValueError("Invalid diagnostic session")

        self.session = session
        return True

    def is_extended_session(self):
        return self.session == 0x03