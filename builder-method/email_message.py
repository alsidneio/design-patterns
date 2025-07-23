# Product
class EmailMessage:
    def __init__(self):
        # Private instance variables
        self._from = ""
        self._to = []
        self._cc = []
        self._bcc = []
        self._subject = ""
        self._body = ""
        self._attachments = []

    # Setters and Getters for private variables
    def set_from(self, from_address: str):
        self._from = from_address

    def set_subject(self, subject: str):
        self._subject = subject

    def set_body(self, body: str):
        self._body = body

    def get_to(self):
        return self._to

    def get_cc(self):
        return self._cc

    def get_bcc(self):
        return self._bcc

    def get_attachments(self):
        return self._attachments

    def send(self):
        print("Email successfully sent:")
        print("------------------------")
        print(f"From: {self._from}")
        print(f"To: {self._to}")
        print(f"CC: {self._cc} ")
        print(f"BCC: {self._bcc}")
        print(f"Subject: {self._subject} ")
        print(f"Body: {self._body} ")
        print(f"Attachements: {self._attachments}")
