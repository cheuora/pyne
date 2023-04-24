import pynecone as pc

def question_form() -> pc.Component:
    pc.grid(
        pc.text("소통해요"),
        pc.text("감사해여")
    )