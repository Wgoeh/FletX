from flet import * 
from fletx import FletX
from fletx.core import FletXPage, FletXRouter
from components.sidebar import ReactiveSidebar, SidebarItemInfo

class HomePage(FletXPage):
    def __init__(self):
        super().__init__()
        self.title = "Home Page"
        self.adaptive = True  # Enable adaptive mode

    def build(self):
        return Container(
            expand = True,
            padding = padding.all(1),
            content= Row(
                expand = True,
                controls = [
                    ReactiveSidebar(
                        width = 250,
                        height = 800,
                        navs = [
                            SidebarItemInfo(
                                title = "My Feed",
                                icon = Icons.FEED_OUTLINED,
                                description = "Go to Feed page",
                            ),
                            SidebarItemInfo(
                                title = "Groups",
                                icon = Icons.GROUP_OUTLINED,
                                description = "Groups page",
                            ),
                            SidebarItemInfo(
                                title = "Messages",
                                icon = Icons.MESSENGER_OUTLINE_OUTLINED,
                                description = "Messages page",
                            ),
                            SidebarItemInfo(
                                title = "Bookmarks",
                                icon = Icons.BOOKMARK_BORDER_OUTLINED,
                                description = "Bookmarks page",
                            ),
                            SidebarItemInfo(
                                title = "More",
                                icon = Icons.MORE_HORIZ_OUTLINED,
                                description = "More Action",
                            ),
                            SidebarItemInfo(
                                title = "Notifications",
                                icon = Icons.NOTIFICATIONS_NONE_OUTLINED,
                                description = "Notifications page",
                            ),
                            SidebarItemInfo(
                                title = "Settings",
                                icon = Icons.SETTINGS_OUTLINED,
                                description = "Settings page",
                            ),
                        ]
                    ),  # Add the reactive sidebar component
                    Column(
                        expand = True,
                        controls = [
                            Text("Welcome to the Home Page!", size=30, weight="bold"),
                            Text("This is a simple example of a reactive sidebar.", size=20)
                        ]
                    )
                ]
            )
        )