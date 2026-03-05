from transformers import pipeline

# load AI model
generator = pipeline(
    "text-generation",
    model="gpt2"
)


def ai_generate(task):

    print("🤖 AI Agent generating response...")

    try:
        result = generator(
            task,
            max_new_tokens=120,
            truncation=True,
            pad_token_id=50256,
            num_return_sequences=1
        )

        return result[0]["generated_text"]

    except Exception as e:
        return f"AI generation error: {e}"