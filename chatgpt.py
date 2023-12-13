from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)




class GPT:
    default_promt = ".Give me a professional proposal in only 4 lines for this project. First of all, it must be hello\nAnd I have studied the details of this project and I would like to offer you my services for your project. I will do this as soon as possible, please message me so we can discuss further. And to see our portfolio, please write to https://drive.google.com/drive/folders/1MgmKqqH47ay42d0PG4G2pkrSGzDDemlK?usp=drive_link from our profile. A very short proposal without details and only in 4 lines. Our company name is Artistry Nexus Collective"

    def input(str_val):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{str_val}",
                }
            ],
            model="gpt-3.5-turbo",
        )
        c = chat_completion.choices[0].message.content
        if 'Hello' in c:
            a = c.replace('Hello,' , "Hello\n\n")
            b = c.replace('Hello!' , "Hello\n\n")
            if a == c:
                c = b
            else:
                c = a
            if 'https://drive' in c :
                None
                chat_GPT_ansewr = c
            else:
                chat_GPT_ansewr = c + "\n\nportfolio : https://drive.google.com/drive/folders/1MgmKqqH47ay42d0PG4G2pkrSGzDDemlK?usp=drive_link"
        else:
            if 'https://drive' in c :
                None
                chat_GPT_ansewr = c
            else:
                chat_GPT_ansewr = c + "\n\nportfolio : https://drive.google.com/drive/folders/1MgmKqqH47ay42d0PG4G2pkrSGzDDemlK?usp=drive_link"
        return chat_GPT_ansewr