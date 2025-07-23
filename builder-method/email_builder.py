from email_message import EmailMessage

# Builder


class EmailBuilder:
    def __init__(self):
        self._email_message = EmailMessage()

    # methods that fall within the build part
    def build(self):
        return self._email_message

    # methods that deal with the add part of the pattern
    def add_from(self, from_address: str):
        self._email_message.set_from(from_address)
        return self

    def add_to(self, to: str):
        self._email_message.get_to().append(to)
        return self

    def add_cc(self, cc: str):
        self._email_message.get_cc().append(cc)
        return self

    def add_attachment(self, attachment: str):
        self._email_message.get_attachments().append(attachment)
        return self

    def add_bcc(self, bcc: str):
        self._email_message.get_bcc().append(bcc)
        return self

    def with_subject(self, subject: str):
        self._email_message.set_subject(subject)
        return self

    def with_body(self, body: str):
        self._email_message.set_body(body)
        return self
