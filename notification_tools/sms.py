import json

from twilio.rest import Client


def sms(message=None, *, twillo_pars=None):
    if not twillo_pars:
        twillo_pars = "C:/Users/seang/OneDrive/api_keys/twillo.json"
    if type(twillo_pars) == str:
        with open(twillo_pars) as pars:
            pars = json.load(pars)
    client = Client(pars.get("accountSID"), pars.get("authToken"))

    for phone in pars.get("out_phones"):
        client.messages.create(
            body=message,
            from_=pars.get("my_num"),
            to=phone
        )


def google_voice(message=None):
    from_ = "18024480775"
    to_ = "18024480775"
    address = f"{from_}.{to_}.sGr3RBLd-1@txt.voice.google.com"
    print(address)


if __name__ == '__main__':
    google_voice("Test Message Plz Ignore")
