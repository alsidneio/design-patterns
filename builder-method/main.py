from email_builder import EmailBuilder


def main():
    email_message = (
        EmailBuilder()
        .add_from("example@intelligencia.com")
        .add_to("sender@sendmail.com")
        .add_cc("copied-sender@sendmail.com")
        .with_subject("Pretty dope builder pattern example")
        .with_body("The builder pattern magic is inside")
        .add_attachment("somefile.py")
        .build()
    )

    email_message.send()


if __name__ == "__main__":
    main()
