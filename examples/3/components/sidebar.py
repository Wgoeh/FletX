from typing import Optional, List, Callable
from flet import *
from dataclasses import dataclass, field

from fletx.core import (
    RxInt, RxBool, RxStr, RxList, FletXWidget
)
from fletx.decorators import reactive_control, watch


####
##      Navigation Sidebar Item Infos
#####
@dataclass
class SidebarItemInfo:
    """
    Represents an item in the sidebar with its properties.
    """
    index: int = 0  # Index of the item in the sidebar
    title: str = "Sidebar Item"
    icon: Optional[str] = None
    description: Optional[str] = None
    # is_active: bool = False  # Indicates if the item is currently active


####
##      Reactive Sidebar Item Component
####
@reactive_control(
    bindings = {
        # 'is_active': 'rx_is_active'
    }
)
class SidebarItem(Container):
    """ Represents an item in the sidebar. """

    # rx_is_active: RxBool
    is_open: RxBool  # Reactive state for sidebar open/close

    def __init__(
        self, 
        index: int, 
        item_info: SidebarItemInfo,
        is_open: RxBool = RxBool(True),
        is_active: bool = False,
        on_selection: Optional[Callable[[],int]] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        FletXWidget.__init__(self)

        # Reactives
        self._is_active = is_active  # Reactive state for active item
        self.is_hovered = RxBool(False)  # Reactive state for hover
        self.is_open = is_open

        self.item_info = item_info
        self.padding = padding.symmetric(horizontal = 15, vertical = 5)
        self.bgcolor = Colors.TRANSPARENT 
        self.border_radius = 5
        # self.height = 60
        self.index = index

        # Events
        self.on_hover = lambda e: self._handle_hover(e)
        self.on_click = self._handle_click
        self._select = on_selection

        self.content = self.build()

    def _handle_hover(self,e: ControlEvent) -> str:
        """ Returns the color for the active state of the sidebar item. """
        self.bgcolor = Colors.GREY_900 if e.data == "true" else Colors.TRANSPARENT
        self.update()

    def _handle_click(self, e):
        """ Handles click events on the sidebar item. """
        # Toggle active state
        self._is_active = True
        # Optionally, you can add more logic here, like navigation or state updates
        if self._select:
            self._select(self.index)

    # @watch(is_open)
    def update_content(self):
        self.content = self.build()

    def build(self) -> Control:
        """ Builds the sidebar item content. """
        if self.is_open.value:
            return Row(
                alignment = MainAxisAlignment.START,
                spacing = 10,
                vertical_alignment = CrossAxisAlignment.CENTER,
                controls = [
                    # Icon
                    Icon(
                        self.item_info.icon or Icons.LIST,
                        size = 24,
                        weight = FontWeight.W_400,
                        color = Colors.GREY_400 if not self._is_active else Colors.AMBER_700
                    ),
                    # Title
                    Text(
                        self.item_info.title,
                        size = 14,
                        weight = FontWeight.W_500,
                        color = Colors.GREY_400 if not self._is_active else Colors.AMBER_700
                    ),
                ]
            )

        # Then display Icon
        return Icon(
            self.item_info.icon,
            size = 30,
            weight = FontWeight.W_400,
            color = Colors.GREY_400 if not self._is_active else Colors.AMBER_700
        )


####
##      Reactive Sidebar Component
#####
@reactive_control(
    bindings = {
        'open': 'is_open',
        'index': 'current_index'
    }
)
class ReactiveSidebar(Container):
    """
    Reactive Sidebar component that integrates with FletX's reactivity system.
    """

    is_open: RxBool = RxBool(True)  # Reactive state for sidebar open/close
    current_index: RxInt

    def __init__(
            self,
            navs: RxList = RxList([]),
            **kwargs
        ):
        super().__init__(**kwargs)
        FletXWidget.__init__(self)

        # Reactive state for sidebar visibility
        self.is_open: RxBool = RxBool(True)
        self.current_index: RxInt = RxInt(0)  # Reactive state for current active index

        self.padding = padding.all(10)
        self.bgcolor = "#060606"
        self.border_radius = 0
        # self.width = 250
        # self.height = 800
        self.navs: RxList = navs

        # Bind the reactive property to the sidebar's visibility

        # Content of the sidebar
        self.content = self.build()

    def setup_listeners(self):

        # Sidebar Width
        self.is_open.listen(
            lambda: self.toggle_sidebar()
        )

    def toggle_sidebar(self):
        self.width = 250 if self.is_open.value else 70
        self.update()

    def build(self) -> Control:
        """ Builds the sidebar content. """
        return Column(
            expand = True,
            spacing = 35,

            # Contrls inside the sidebar
            controls = [
                # Header Row
                Row(
                    alignment = MainAxisAlignment.SPACE_BETWEEN,
                    controls = [
                        # LOGO AND TEXT
                        Row(
                            alignment = MainAxisAlignment.START,
                            spacing = 10,
                            controls = [
                                # LOGO
                                Icon(
                                    Icons.CODE_OFF_ROUNDED,
                                    size = 30,
                                    color = Colors.AMBER_700
                                ),

                                # TEXT
                                Text(
                                    "Code Zone",
                                    size = 20,
                                    weight = FontWeight.W_500,
                                    color = Colors.AMBER_700,
                                    visible = self.is_open.value
                                ),
                            ]
                        ),

                        # Colse Button
                        Container(
                            padding = padding.all(5),
                            on_click= lambda e: self.is_open.toggle(),
                            content = Icon(
                                Icons.CLOSE,
                                size = 20,
                                color = Colors.WHITE,
                                weight = FontWeight.W_300,
                            )
                        ),
                    ]
                ),

                # Sidebar content
                Column(
                    expand = True,
                    spacing = 10,
                    controls = [
                        Text(
                            "Welcome", 
                            size = 16, 
                            weight = FontWeight.W_400, 
                            color = Colors.GREY_400,
                            visible = self.is_open.value
                        ),
                        
                        # Sidebar Items
                        ListView(
                            expand = True,
                            spacing = 5,
                            controls = [
                                SidebarItem(
                                    index = idx,
                                    is_open = self.is_open,
                                    on_selection = lambda e: setattr(self.current_index,'value', e),
                                    is_active = self.current_index.value == idx,
                                    item_info = item
                                ) for idx, item in enumerate(self.navs)
                            ]
                        )
                    ]
                ),
                Text("This is a reactive sidebar.", color=Colors.GREY_600)
            ]
        )

    def toggle_sidebar(self, e):
        """ Toggles the sidebar open/close state. """
        self.is_open.value = not self.is_open.value