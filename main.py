from flet import *

class Buildpage(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        # إنشاء الكونتينر
        self.Buildbox = Container(
            width=self.page.window.width,  # عرض الكونتينر يعتمد على عرض النافذة
            height=self.page.window.height,
            bgcolor=colors.AMBER,
          
        )
        

        # إنشاء الكونتينرات الداخلية مع نسب عرض مبدئية
            

        self.page.update()
    def add_appbar(self,e):
         self.y=Column([Container(Row([
                           Icon(icons.HOME),
                           Text("appbar"),
                           PopupMenuButton(items=
                                         [
                                            PopupMenuItem("home"),
                                             PopupMenuItem("login"),
                                              PopupMenuItem("home"),
                                         ]
                           )
                           
                           
                        ],width=self.page.window.width,alignment=MainAxisAlignment.SPACE_BETWEEN,),bgcolor=colors.WHITE)],width=self.page.window.width,expand=True)
         self.container2.content = self.y              
         self.page.update()

    def build(self):
        self.container1 = Container(bgcolor=colors.BLACK, expand=1)
        self.container2 = Container(bgcolor=colors.BLUE_700, expand=3)  
        self.x=Column([Row([
                        Text("appbar",color=colors.WHITE),
                        TextButton("appbar1",style=ButtonStyle(bgcolor=colors.WHITE),on_click=lambda e:self.add_appbar)
                        

                        ])])

        self.y=Column([Container(Row([
                           Icon(icons.HOME),
                           Text("appbar"),
                           PopupMenuButton(items=
                                         [
                                            PopupMenuItem("home"),
                                             PopupMenuItem("home"),
                                              PopupMenuItem("home"),
                                         ]
                           )
                           
                           
                        ],width=self.page.window.width,alignment=MainAxisAlignment.SPACE_BETWEEN,),bgcolor=colors.AMBER)],width=self.page.window.width,expand=True)
       
        self.container1.content=self.x
        self.container2.content=self.y
        self.Buildrow = Row([self.container1, self.container2], spacing=0,expand=True)

        self.Buildbox.content = self.Buildrow
        return self.Buildbox

# التطبيق الرئيسي
def main(page: Page):
    page.title = "osama"
    page.window.resizable = True  # تأكد من أن النافذة قابلة لتغيير الحجم
    page.padding=0
    page.spacing=0
    # تمرير كائن الصفحة إلى Buildpage
    buildpage = Buildpage(page)

    # إضافة Buildpage إلى الصفحة
    page.add(buildpage)
    page.update()

app(target=main,view=AppView.WEB_BROWSER)
