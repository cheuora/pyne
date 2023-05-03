import pynecone as pc
import pyne.pyne as pn



def question_form():
    return pc.box(
        pc.vstack(
            pc.heading(pn.CondState.color),
            pn.color_picker(
                on_change=pn.CondState.set_color
            ),
        ),
        background_color=pn.CondState.color,
        padding="5em",
        border_radius="1em",
    )


