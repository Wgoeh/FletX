# PROJECT TEMPLATE
### Example of blog project
```bash
blog_projet/
├── breeze.json         # The project config (comme angular.json)
├── app/
│   ├── app.routing.py    # Définition globale des routes
│   ├── components/
│   │   ├── home/
│   │   │   ├── home.component.py
│   │   │   ├── home.component.html
│   │   ├── post/
│   │   │   ├── post.component.py
│   │   │   ├── post.component.html
│   ├── modules/
│   │   └── blog/
│   │       ├── blog.module.py
│   │       ├── blog.routing.py
│   │       └── components/...
├── assets/
│   ├── images/
│   └── fonts/
├── styles/
│   └── styles.css
├── routing.py             # Base file utilisé au build
├── main.py                # AppModule & démarrage
└── README.md

```