from models import client
import openai


def make_question(question):
    print(f'Question: {question}')

    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # gpt-4-0314
        messages=[
            {
                'role': 'user',
                'content': f'{question}'
            }
        ]
    )

    print(f' Answer: {response.choices[0].message.content}')


if __name__ == '__main__':
    make_question('Cómo subir una carpeta a un bucket de s3')
