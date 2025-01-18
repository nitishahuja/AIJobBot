import openai

class AIResponder:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, question, job_description):
        prompt = f"Job Description: {job_description}\nQuestion: {question}\nAnswer:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

if __name__ == "__main__":
    responder = AIResponder("your-openai-api-key")
    answer = responder.generate_response("Why do you want this job?", "A great Python Developer position.")
    print(answer)
