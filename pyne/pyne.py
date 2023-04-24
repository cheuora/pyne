"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

class CondState(pc.State):

    item_dictionary={'show1':True, 'show2': False,
                     'menu_1_1':False, 'menu_1_2':False,
                     'menu_1_3':False, 'menu_2_1':False,
                     'menu_2_2':False, 'menu_3_1':False,
                     'menu_3_2':False, 'menu_3_3':False,
                     'menu_4_1':False}
    # for Buttons

    def change1(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['show1'] = True

    def change2(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['show2'] = True
    
    def change_to_menu_1_1(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['menu_1_1'] = True

    def change_to_menu_1_2(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['menu_1_2'] = True

    def change_to_menu_1_3(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['menu_1_3'] = True

    def change_to_menu_2_1(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['menu_2_1'] = True

    def change_to_menu_2_2(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['menu_2_2'] = True


    def change_to_menu_3_1(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['menu_3_1'] = True

    
    def change_to_menu_3_2(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['menu_3_2'] = True

    def change_to_menu_3_3(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['menu_3_3'] = True

    def change_to_menu_4_1(self):
        self.item_dictionary = {key : False for key,value in self.item_dictionary.items()}
        self.item_dictionary['menu_4_1'] = True



def index() -> pc.Component:
    return  pc.vstack(
            navbar(),
            pc.spacer(),pc.spacer(),pc.spacer(),pc.spacer(),pc.spacer(),pc.spacer(),pc.spacer(),pc.spacer(),
            
            pc.cond(
                CondState.item_dictionary['show1'],
                second_zone(),
                pc.cond(
                    CondState.item_dictionary['show2'],
                    main_zone(),
                    pc.cond(
                        CondState.item_dictionary['menu_1_1'],
                        pc.text("우리들의 이야기"),
                        pc.cond(
                            CondState.item_dictionary['menu_1_2'],
                            pc.text("직무 이야기"),
                            pc.cond(
                                CondState.item_dictionary['menu_1_3'],
                                pc.text("신규 입사자 이야기"),
                                pc.cond(
                                    CondState.item_dictionary['menu_2_1'],
                                    pc.text("채용정보"),
                                    pc.cond(
                                        CondState.item_dictionary['menu_2_2'],
                                        pc.text("상시채용정보"),
                                        pc.cond(
                                            CondState.item_dictionary['menu_3_1'],
                                            pc.text("우리들 소개"),
                                            pc.cond(
                                                CondState.item_dictionary['menu_3_2'],
                                                pc.text("우리들 문화"),
                                                pc.cond(
                                                    CondState.item_dictionary['menu_3_3'],
                                                    pc.text("우리들 뉴스"),
                                                    pc.cond(
                                                        CondState.item_dictionary['menu_4_1'],
                                                        pc.text("소통해요"),
                                                        pc.spacer()
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                )
                            )
                        )
                    ),
                ),
            ),

    )

def main_zone() -> pc.Component:
    return   pc.box(
                pc.vstack(
                    pc.heading("안녕하세요....!", font_size="4em"),
                    pc.heading("Hello World Korean Ver"),
                    pc.box("Get started by editing ", pc.code(filename, font_size="1em")),

                    pc.link(
                        "Check out our docs!",
                        href=docs_url,
                        border="0.1em solid",
                        padding="0.5em",
                        border_radius="0.5em",
                        _hover={
                            "color": "rgb(107,99,246)",
                        },
                    ),
                    spacing="1.5em",
                    font_size="1em",
                ),
        )

def second_zone() -> pc.Component:
    return   pc.box(
                pc.vstack(
                    pc.heading("こんにちは!", font_size="4em"),
                    pc.heading("Hello World Japanese Version"),
                    pc.box("Get started by editing ", pc.code(filename, font_size="1em")),

                    pc.link(
                        "Check out our docs!",
                        href=docs_url,
                        border="0.1em solid",
                        padding="0.5em",
                        border_radius="0.5em",
                        _hover={
                            "color": "rgb(107,99,246)",
                        },
                    ),
                    spacing="1.5em",
                    font_size="1em",
                ),
        )

def navbar() ->pc.Component:
    return pc.box(
        pc.hstack(
            pc.image(src="favicon.ico"),
            pc.heading("안녕하헤효!!", font_family="KIMM_Bold"),
            pc.spacer(),
            pc.spacer(),

            pc.menu(
                pc.menu_button("우리들의 이야기"),
                pc.menu_list(
                    pc.menu_item("우리들의 이야기",on_click=CondState.change_to_menu_1_1),
                    pc.menu_item("직무 이야기",on_click=CondState.change_to_menu_1_2),
                    pc.menu_item("신규 입사자 이야기", on_click=CondState.change_to_menu_1_3),
                ),
            ),
            pc.spacer(),
            pc.menu(
                pc.menu_button("함깨해요"),
                pc.menu_list(
                    pc.menu_item("채용정보", on_click=CondState.change_to_menu_2_1),
                    pc.menu_item("입사지원", on_click=CondState.change_to_menu_2_2),
                ),
            ),
            pc.spacer(),
            pc.menu(
                pc.menu_button("우리들 소식"),
                pc.menu_list(
                    pc.menu_item("우리들은?", on_click=CondState.change_to_menu_3_1),
                    pc.menu_item("우리들의 문화", on_click=CondState.change_to_menu_3_2),
                    pc.menu_item("뉴스", on_click=CondState.change_to_menu_3_3),
                ),
            ),
            pc.spacer(),
            pc.text("소통해요!", on_click=CondState.change_to_menu_4_1),
            pc.spacer(),
            pc.input(width="200px"),
            pc.icon(tag="search2"),

            pc.spacer(),
            pc.spacer(),
            pc.spacer(),


            pc.button_group(
                pc.button('日本語', on_click=CondState.change1),
                pc.button('한국어', on_click=CondState.change2)
            )


        ),

        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
        bg='lightgreen',
    )

# Add state and page to the app.
app = pc.App(state=CondState, stylesheets=['mapo.css'])
app.add_page(index)
app.compile()
